#!/usr/bin/env python3
"""Utilities for managing DROIX wiki source ingestion.

The tool is intentionally conservative: it scans and validates the corpus,
builds a canonical ingest queue, writes a ledger page, and runs structural
lint checks. It does not attempt to summarize sources into the wiki.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RAW_INGEST = ROOT / "raw" / "ingest"
SUPPLIER_RESOURCES = ROOT / "archive" / "supplier-resources"
WIKI = ROOT / "wiki"
LEDGER = WIKI / "analysis" / "ingest-ledger.md"

RAW_TO_WIKI_TYPE = {
    "review-blog": "review-blog",
    "product-page": "product-page",
    "kb-article": "kb-article",
    "kb-faq": "kb-faq",
    "resource-bundle": "resource-bundle",
}

BRAND_ALIASES = {
    "droix": ["droix"],
    "gpd": ["gpd"],
    "ayaneo": ["ayaneo", "aya-neo", "aya neo"],
    "onexplayer": ["onexplayer", "one-netbook", "one netbook", "onexgpu", "onexfly"],
    "ayn": ["ayn", "odin", "thor", "loki"],
    "retroid": ["retroid"],
    "anbernic": ["anbernic", "rg35", "rg40", "rg353", "rg351", "rg505", "rg552", "win-600"],
    "konkr": ["konkr"],
    "beelink": ["beelink"],
    "minisforum": ["minisforum"],
    "geekom": ["geekom"],
    "gmktec": ["gmktec", "nucbox"],
    "acepc": ["acepc"],
    "chuwi": ["chuwi"],
    "asus": ["asus"],
    "aokzoe": ["aokzoe"],
    "maxtang": ["maxtang"],
    "miyoo": ["miyoo"],
    "rocktek": ["rocktek"],
}

CATEGORY_HINTS = [
    ("mini-pc", ["mini-pc", "mini pc", "desktop pc", "nuc", "beelink", "minisforum", "geekom", "gmktec", "acepc", "chuwi", "maxtang"]),
    ("android-handheld", ["android handheld", "android gaming", "odin", "retroid", "rg", "pocket s", "pocket ace", "pocket ds", "pocket vert"]),
    ("handheld-pc", ["handheld gaming pc", "windows gaming handheld", "win 5", "win 4", "win mini", "win max", "onexplayer", "onexfly", "ayaneo 2"]),
    ("umpc", ["umpc", "pocket 3", "pocket 4", "micro pc", "micropc", "mini laptop"]),
    ("egpu", ["egpu", "external gpu", "graphics dock", "g1", "ag01", "onexgpu"]),
    ("accessory", ["dock", "docking station", "case", "keyboard", "monitor", "hub", "ssd"]),
    ("android-tv-box", ["android tv box", "tv box", "rocktek"]),
]

TECH_HINTS = {
    "amd": ["ryzen", "radeon", "amd"],
    "intel": ["intel", "core i", "celeron", "pentium", "n95", "n97", "n100", "n250", "n300"],
    "qualcomm": ["snapdragon", "qualcomm"],
    "unisoc": ["unisoc", "t820", "t618"],
    "nvidia": ["nvidia", "geforce", "rtx", "gtx"],
}


@dataclass(frozen=True)
class SourceRecord:
    path: str
    corpus: str
    title: str
    source_url: str
    source_site: str
    raw_type: str
    subtype: str
    date: str
    brand: str
    product: str
    variant: str
    category: str
    technologies: tuple[str, ...]
    status: str
    issues: tuple[str, ...]
    sort_key: tuple[str, str, str]


def repo_rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def normalize_product_slug(slug: str) -> str:
    replacements = {
        "aya-neo-": "ayaneo-",
        "one-xplayer-": "onexplayer-",
        "one-netbook-": "onexplayer-",
    }
    for old, new in replacements.items():
        if slug.startswith(old):
            return new + slug.removeprefix(old)
    return slug


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        data[key.strip()] = value
    return data


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def existing_slugs(folder: str) -> set[str]:
    base = WIKI / folder
    return {path.stem for path in base.glob("*.md")} if base.exists() else set()


def load_product_titles() -> dict[str, str]:
    products: dict[str, str] = {}
    for path in (WIKI / "products").glob("*.md"):
        meta = parse_frontmatter(read_text(path))
        slug = meta.get("slug", path.stem)
        products[slug] = meta.get("title", slug)
    return products


def infer_brand(path: Path, title: str, body: str, source_site: str) -> str:
    rel = repo_rel(path).lower()
    haystack = f"{rel} {title}".lower()
    if "gpdstore" in haystack:
        return "gpd"
    for brand, aliases in BRAND_ALIASES.items():
        if brand == "droix":
            continue
        if any(alias in haystack for alias in aliases):
            return brand
    if re.search(r"(^|[-\s])droix[-\s]", haystack):
        return "droix"
    body_head = body[:2000].lower()
    for brand, aliases in BRAND_ALIASES.items():
        if brand == "droix":
            continue
        if any(alias in body_head for alias in aliases):
            return brand
    return ""


def infer_product(path: Path, title: str, brand: str, product_slugs: set[str]) -> str:
    candidates = sorted(product_slugs, key=len, reverse=True)
    haystack = f"{repo_rel(path)} {title}".lower().replace("_", "-")
    for slug in candidates:
        if slug in haystack:
            return slug
        if brand and slug.startswith(f"{brand}-"):
            model = slug.removeprefix(f"{brand}-")
            if model in haystack:
                return slug
    filename_slug = normalize_product_slug(slugify(path.stem))
    if brand and filename_slug.startswith(f"{brand}-"):
        return filename_slug
    for known_brand in BRAND_ALIASES:
        if known_brand != "droix" and filename_slug.startswith(f"{known_brand}-"):
            return filename_slug
    if brand:
        cleaned = slugify(re.sub(r"(?i)\b(review|with video|unboxing|demo|guide|faq|product)\b", " ", title))
        if cleaned.startswith(f"{brand}-"):
            return cleaned
        return f"{brand}-{cleaned}" if cleaned else ""
    return slugify(title)


def infer_category(title: str, body: str, path: Path) -> str:
    haystack = f"{repo_rel(path)} {title} {body[:2500]}".lower()
    for category, hints in CATEGORY_HINTS:
        if any(hint in haystack for hint in hints):
            return category
    return ""


def infer_technologies(title: str, body: str) -> tuple[str, ...]:
    haystack = f"{title} {body[:6000]}".lower()
    return tuple(vendor for vendor, hints in TECH_HINTS.items() if any(hint in haystack for hint in hints))


def raw_files() -> Iterable[Path]:
    for path in sorted(RAW_INGEST.rglob("*.md")):
        if path.name == "MANIFEST.md":
            continue
        yield path
    if SUPPLIER_RESOURCES.exists():
        for path in sorted(SUPPLIER_RESOURCES.rglob("*.md")):
            if path.name == "source-pages.md":
                continue
            yield path


def raw_type_from_path(path: Path, meta: dict[str, str]) -> str:
    if "type" in meta:
        return meta["type"]
    rel = repo_rel(path)
    if rel.startswith("archive/supplier-resources/"):
        return "resource-bundle"
    if "/kb/" in rel:
        return "kb-article"
    if "/product/" in rel:
        return "product-page"
    if "/blog/" in rel:
        return "review-blog"
    return ""


def source_date(meta: dict[str, str], body: str, raw_type: str) -> str:
    for key in ("date", "published", "release_date", "retrieved"):
        if key in meta:
            match = re.search(r"\d{4}-\d{2}-\d{2}", meta[key])
            if match:
                return match.group(0)
    if raw_type == "product-page":
        return ""
    match = re.search(r"\b(20\d{2})[-/](\d{2})[-/](\d{2})\b", body[:2000])
    return match.group(0).replace("/", "-") if match else ""


def make_record(path: Path, product_slugs: set[str]) -> SourceRecord:
    body = read_text(path)
    meta = parse_frontmatter(body)
    title = meta.get("title") or re.sub(r"[-_]+", " ", path.stem).strip().title()
    source_site = meta.get("source_site", "")
    raw_type = raw_type_from_path(path, meta)
    subtype = RAW_TO_WIKI_TYPE.get(raw_type, raw_type)
    date = source_date(meta, body, raw_type)
    brand = infer_brand(path, title, body, source_site)
    product = infer_product(path, title, brand, product_slugs)
    variant = ""
    category = infer_category(title, body, path)
    technologies = infer_technologies(title, body)
    issues: list[str] = []
    if not raw_type:
        issues.append("missing-type")
    if not brand:
        issues.append("unresolved-brand")
    if not product:
        issues.append("unresolved-product")
    if not category and subtype != "resource-bundle":
        issues.append("unresolved-category")
    if subtype in {"review-blog", "kb-article", "kb-faq"} and not date:
        issues.append("missing-date")
    if product and product not in product_slugs:
        issues.append("product-not-onboarded")

    rel = repo_rel(path)
    corpus = "supplier-resources" if rel.startswith("archive/supplier-resources/") else "raw-ingest"
    dated = date or "9999-99-99"
    tier = "3-legacy" if category == "android-tv-box" else "1-main"
    if subtype == "product-page":
        tier = "0-product"
    elif subtype == "resource-bundle":
        tier = "2-resource"
    status = "pending"
    return SourceRecord(
        path=rel,
        corpus=corpus,
        title=title,
        source_url=meta.get("source_url", ""),
        source_site=source_site,
        raw_type=raw_type,
        subtype=subtype,
        date=date,
        brand=brand,
        product=product,
        variant=variant,
        category=category,
        technologies=technologies,
        status=status,
        issues=tuple(issues),
        sort_key=(tier, dated, rel),
    )


def scan_records() -> list[SourceRecord]:
    product_slugs = existing_slugs("products")
    return [make_record(path, product_slugs) for path in raw_files()]


def print_summary(records: list[SourceRecord]) -> None:
    print(f"sources: {len(records)}")
    for label, values in [
        ("corpus", [r.corpus for r in records]),
        ("subtype", [r.subtype or "(none)" for r in records]),
        ("brand", [r.brand or "(unresolved)" for r in records]),
        ("category", [r.category or "(unresolved)" for r in records]),
    ]:
        print(f"\n{label}:")
        for value, count in Counter(values).most_common():
            print(f"  {value}: {count}")
    issue_counts = Counter(issue for r in records for issue in r.issues)
    print("\nissues:")
    if issue_counts:
        for issue, count in issue_counts.most_common():
            print(f"  {issue}: {count}")
    else:
        print("  none")


def canonical_queue(records: list[SourceRecord]) -> list[SourceRecord]:
    return sorted(records, key=lambda r: r.sort_key)


def markdown_table(records: list[SourceRecord]) -> str:
    lines = [
        "| Status | Source | Type | Date | Brand | Product | Category | Issues |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in records:
        issues = ", ".join(r.issues) if r.issues else ""
        lines.append(
            "| "
            + " | ".join(
                [
                    r.status,
                    f"`{r.path}`",
                    r.subtype,
                    r.date,
                    r.brand,
                    r.product,
                    r.category,
                    issues,
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def write_ledger(records: list[SourceRecord]) -> None:
    today = os.environ.get("WIKI_DATE", dt.date.today().isoformat())
    counts = Counter(r.subtype for r in records)
    issue_counts = Counter(issue for r in records for issue in r.issues)
    body = [
        "---",
        "title: Ingest Ledger",
        "type: analysis",
        "slug: ingest-ledger",
        f"created: {today}",
        f"updated: {today}",
        "sources: []",
        "tags: [ingest, ledger]",
        "---",
        "",
        "# Ingest Ledger",
        "",
        "Tracks staged raw sources and archived supplier resource bundles awaiting full wiki ingestion. Status values are managed manually after each completed batch.",
        "",
        "## Summary",
        "",
        f"- Total pending records: {len(records)}",
    ]
    body.extend(f"- {subtype or '(none)'}: {count}" for subtype, count in counts.most_common())
    body.append("")
    body.append("## Open Issues")
    body.append("")
    if issue_counts:
        body.extend(f"- {issue}: {count}" for issue, count in issue_counts.most_common())
    else:
        body.append("- None")
    body.extend(["", "## Canonical Queue", "", markdown_table(canonical_queue(records)), ""])
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text("\n".join(body), encoding="utf-8")


def validate(records: list[SourceRecord]) -> int:
    errors = [r for r in records if r.issues]
    for r in errors[:200]:
        print(f"{r.path}: {', '.join(r.issues)}", file=sys.stderr)
    if len(errors) > 200:
        print(f"... {len(errors) - 200} more records with issues", file=sys.stderr)
    print(f"records={len(records)} records_with_issues={len(errors)}")
    return 1 if errors else 0


def extract_wikilinks(text: str) -> list[str]:
    links: list[str] = []
    for match in re.finditer(r"\[\[([^\]#]+)", text):
        target = match.group(1).split("|", 1)[0].strip()
        target = target.rstrip("\\").strip()
        links.append(target)
    return links


def parse_listish(value: str) -> list[str]:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"').strip("'") for item in inner.split(",")]
    return [value] if value else []


def wiki_pages() -> list[Path]:
    return sorted(WIKI.rglob("*.md"))


def lint_wiki() -> int:
    pages = wiki_pages()
    slugs = {path.stem for path in pages}
    product_slugs = existing_slugs("products")
    entity_slugs = existing_slugs("entities")
    source_slugs = existing_slugs("sources")
    findings: list[str] = []
    inbound: Counter[str] = Counter()

    for path in pages:
        rel = repo_rel(path)
        text = read_text(path)
        if re.search(r"\bDroiX\b|\bDroix\b", text):
            findings.append(f"{rel}: bad DROIX capitalization")
        if re.search(r"\]\((?:\.\./)?(?:raw|archive)/", text):
            findings.append(f"{rel}: links to raw/archive path")
        if path != LEDGER and len(text.splitlines()) > 500:
            findings.append(f"{rel}: page over 500 lines")
        for link in extract_wikilinks(text):
            inbound[link] += 1
            if link not in slugs:
                findings.append(f"{rel}: broken wikilink [[{link}]]")

        meta = parse_frontmatter(text)
        page_type = meta.get("type", "")
        if page_type == "source":
            product = meta.get("product", "")
            variant = meta.get("variant", "")
            if product and product not in product_slugs:
                findings.append(f"{rel}: source product does not exist: {product}")
            if variant and variant != "null" and variant not in product_slugs:
                findings.append(f"{rel}: source variant does not exist: {variant}")
        if page_type == "variant":
            parent = meta.get("parent_product", "")
            if parent and parent not in product_slugs:
                findings.append(f"{rel}: missing parent product {parent}")
        if page_type == "product":
            brand = meta.get("brand", "")
            category = meta.get("category", "")
            if brand and brand not in entity_slugs:
                findings.append(f"{rel}: missing brand entity {brand}")
            if category and category not in entity_slugs:
                findings.append(f"{rel}: missing category entity {category}")
            if "## Resources" not in text:
                findings.append(f"{rel}: product hub missing Resources section")

    for path in (WIKI / "products").glob("*.md"):
        slug = path.stem
        text = read_text(path)
        meta = parse_frontmatter(text)
        if meta.get("type") != "product":
            continue
        brand = meta.get("brand")
        category = meta.get("category")
        if brand:
            brand_path = WIKI / "entities" / f"{brand}.md"
            if brand_path.exists() and f"[[{slug}]]" not in read_text(brand_path):
                findings.append(f"{repo_rel(path)}: product not linked from brand page [[{brand}]]")
        if category:
            category_path = WIKI / "entities" / f"{category}.md"
            if category_path.exists() and f"[[{slug}]]" not in read_text(category_path):
                findings.append(f"{repo_rel(path)}: product not linked from category page [[{category}]]")
        if f"[[{slug}]]" not in read_text(WIKI / "index.md"):
            findings.append(f"{repo_rel(path)}: product not linked from index")

    resource_current: defaultdict[tuple[str, str], list[str]] = defaultdict(list)
    for path in (WIKI / "sources").glob("*.md"):
        meta = parse_frontmatter(read_text(path))
        subtype = meta.get("subtype", "")
        if not subtype.startswith("resource-"):
            continue
        product = meta.get("product", "")
        kind = subtype.removeprefix("resource-")
        if product and "current" in read_text(path).lower():
            resource_current[(product, kind)].append(path.stem)
    for (product, kind), releases in resource_current.items():
        if len(releases) > 1:
            findings.append(f"multiple current {kind} resources for {product}: {', '.join(releases)}")

    for slug in sorted(slugs - {"index", "log"}):
        if inbound[slug] == 0 and slug != "ingest-ledger":
            findings.append(f"{slug}: orphan page (no inbound wikilinks)")

    if findings:
        for finding in findings:
            print(f"- {finding}")
        print(f"\nfindings={len(findings)}")
        return 1
    print("findings=0")
    return 0


def write_report(records: list[SourceRecord], limit: int) -> None:
    queue = canonical_queue(records)[:limit]
    print("# Batch Candidate Report")
    print()
    print(f"Candidate count: {len(queue)}")
    print()
    print(markdown_table(queue))
    print()
    blocked = [r for r in queue if r.issues]
    print("## Unresolved Classifications")
    print()
    if blocked:
        for r in blocked:
            print(f"- `{r.path}`: {', '.join(r.issues)}")
    else:
        print("- None")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan", help="scan sources and print a summary")
    scan.add_argument("--json", action="store_true", help="emit full JSON records")
    batch = sub.add_parser("batch", help="print the next canonical batch")
    batch.add_argument("-n", "--limit", type=int, default=20)
    sub.add_parser("ledger", help="write wiki/analysis/ingest-ledger.md")
    sub.add_parser("validate", help="validate inferred classifications")
    sub.add_parser("lint", help="run wiki structural lint checks")
    report = sub.add_parser("report", help="print a batch report")
    report.add_argument("-n", "--limit", type=int, default=20)
    args = parser.parse_args()

    if args.command == "lint":
        return lint_wiki()

    records = scan_records()
    if args.command == "scan":
        if args.json:
            print(json.dumps([asdict(r) for r in records], indent=2))
        else:
            print_summary(records)
        return 0
    if args.command == "batch":
        print(markdown_table(canonical_queue(records)[: args.limit]))
        return 0
    if args.command == "ledger":
        write_ledger(records)
        print(repo_rel(LEDGER))
        return 0
    if args.command == "validate":
        return validate(records)
    if args.command == "report":
        write_report(records, args.limit)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Extract GPD resource pages into raw Markdown sources.

The GPD site serves a tiny HTML shell that loads page content from static
Head.js/Body.js files containing document.write payloads. This script decodes
those payloads and preserves the visible resource text plus outbound URLs.
"""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import html
from html.parser import HTMLParser
import re
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin
from urllib.request import Request, urlopen


GPD_SOURCE_PAGES = [
    ("gpd-win-5", "GPD WIN 5", "https://www.gpd.hk/gpdwin5firmwaredriver"),
    ("gpd-micropc-2", "GPD MicroPC 2", "https://www.gpd.hk/gpdmicropc2firmwaredriver"),
    ("gpd-win-mini-2025", "GPD WIN Mini 2025", "https://www.gpd.hk/gpdwinmini2025firmwaredriver"),
    ("gpd-win-max-2-2025", "GPD WIN Max 2 2025", "https://www.gpd.hk/gpdwinmax22025firmware"),
    ("gpd-win-4-2025", "GPD WIN 4 2025", "https://www.gpd.hk/gpdwin42025firmwaredriver"),
    ("gpd-pocket-4", "GPD Pocket 4", "https://www.gpd.hk/gpdpocket4firmware"),
    ("gpd-duo", "GPD DUO", "https://www.gpd.hk/gpdduofirmwaredriver"),
    ("gpd-win-mini-2024", "GPD WIN Mini / 2024", "https://www.gpd.hk/gpdwinminifirmwaredriver"),
    ("gpd-win-4-2023", "GPD WIN 4 2023 / 2024", "https://www.gpd.hk/gpdwin42023firmwaredriver"),
    ("gpd-g1", "GPD G1", "https://www.gpd.hk/gpdg1firmwaredriver"),
    ("gpd-win-max-2-2023", "GPD WIN Max 2 2023 / 2024", "https://www.gpd.hk/gpdwinmax22023firmwaredriver"),
    ("gpd-win-4", "GPD WIN 4", "https://www.gpd.hk/gpdwin4firmwaredriver"),
    ("gpd-win-max-2", "GPD WIN Max 2", "https://www.gpd.hk/gpdwinmax2firmwareanddriver"),
    ("gpd-xp-plus", "GPD XP Plus", "https://www.gpd.hk/gpdxpplusfirmware"),
    ("gpd-p2-max-2022", "GPD P2 Max 2022", "https://www.gpd.hk/gpdp2max2022firmwaredriverbios"),
    ("gpd-pocket-3", "GPD Pocket 3", "https://www.gpd.hk/gpdpocket3firmware"),
    ("gpd-xp", "GPD XP", "https://www.gpd.hk/gpdxpfirmware"),
    ("gpd-win-max-2021", "GPD WIN Max 2021", "https://www.gpd.hk/gpdwinmax2021firmwaredriver"),
    ("gpd-win-3", "GPD WIN 3", "https://www.gpd.hk/gpdwin3firmwaredriverbios"),
    ("gpd-win-max", "GPD WIN Max", "https://www.gpd.hk/gpdwinmaxfirmware"),
    ("gpd-p2-max", "GPD P2 Max", "https://www.gpd.hk/gpdp2maxfirmwaredriverbios"),
    ("gpd-micropc", "GPD MicroPC", "https://www.gpd.hk/gpd_micropc_firmware_driver_bios"),
    ("gpd-pocket-2", "GPD Pocket 2", "https://www.gpd.hk/gpdp2firmware"),
    ("gpd-win-2", "GPD WIN 2", "https://www.gpd.hk/gpdwin2firmware"),
    ("gpd-pocket", "GPD Pocket", "https://www.gpd.hk/gpdpocketfirmware"),
    ("gpd-win", "GPD WIN", "https://www.gpd.hk/gpdwinfirmware"),
    ("gpd-xd-plus", "GPD XD Plus", "https://www.gpd.hk/gpdxdplusfirmware"),
    ("gpd-xd", "GPD XD", "https://www.gpd.hk/gpdxdfirmware"),
]


USER_AGENT = "Mozilla/5.0 (compatible; raw-resource-extractor/1.0)"


class VisibleHTMLParser(HTMLParser):
    """Collect visible-ish text and anchors from decoded static page HTML."""

    BLOCK_TAGS = {"p", "div", "li", "br", "h1", "h2", "h3", "h4", "tr"}
    SKIP_TAGS = {"script", "style", "svg"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.text_parts: list[str] = []
        self.links: list[dict[str, str]] = []
        self.current_link: dict[str, object] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v or "" for k, v in attrs}
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in self.BLOCK_TAGS:
            self.text_parts.append("\n")
        if tag == "a" and "href" in attrs_dict:
            self.current_link = {"href": attrs_dict["href"], "parts": []}

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "a" and self.current_link is not None:
            parts = self.current_link["parts"]
            assert isinstance(parts, list)
            label = normalize_inline("".join(parts))
            self.links.append({"label": label, "href": str(self.current_link["href"])})
            self.current_link = None
        if tag in self.BLOCK_TAGS:
            self.text_parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if data.strip():
            self.text_parts.append(data)
            if self.current_link is not None:
                parts = self.current_link["parts"]
                assert isinstance(parts, list)
                parts.append(data)


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=45) as response:
        return response.read().decode("utf-8", "replace")


def decode_document_write(script_text: str) -> str:
    match = re.match(r"\s*document\.write\('(.*)'\);\s*$", script_text, re.S)
    if not match:
        return script_text
    decoded = ast.literal_eval("'" + match.group(1) + "'")
    return html.unescape(decoded)


def normalize_inline(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text).replace("\xa0", " ")).strip()


def decode_web_text(text: str) -> str:
    if "\\u" in text:
        try:
            text = text.encode("utf-8").decode("unicode_escape")
        except UnicodeDecodeError:
            pass
    return normalize_inline(text)


def normalize_multiline(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [normalize_inline(line) for line in text.split("\n")]
    compact: list[str] = []
    for line in lines:
        if line:
            compact.append(line)
    return "\n".join(compact)


def extract_visible(segment: str) -> tuple[str, list[dict[str, str]]]:
    parser = VisibleHTMLParser()
    parser.feed(segment)
    return normalize_multiline("".join(parser.text_parts)), parser.links


def first_match(pattern: str, text: str) -> str:
    match = re.search(pattern, text, re.S | re.I)
    return decode_web_text(match.group(1)) if match else ""


def extract_script_urls(page_url: str, outer_html: str) -> tuple[str, str]:
    head = first_match(r"""<script\s+src=['"]([^'"]*Head\.js[^'"]*)['"]""", outer_html)
    body = first_match(r"""<script\s+src=['"]([^'"]*Body\.js[^'"]*)['"]""", outer_html)
    return urljoin(page_url, head), urljoin(page_url, body)


def extract_tab_labels(body_html: str) -> dict[str, str]:
    labels: dict[str, str] = {}
    pattern = re.compile(
        r'<li[^>]*data-area="([^"]+)"[^>]*>\s*<a[^>]*class="[^"]*f-ellipsis[^"]*"[^>]*>(.*?)</a>',
        re.S,
    )
    for area, label_html in pattern.findall(body_html):
        label = normalize_inline(re.sub(r"<[^>]+>", " ", label_html))
        if label:
            labels[area] = label
    return labels


def extract_tab_segments(body_html: str) -> list[dict[str, str]]:
    starts = [
        match
        for match in re.finditer(r'<div class="smAreaC" id="smc_([^"]+)" cid="(con_\d+_\d+)"', body_html)
        if match.group(1).startswith("tabArea")
    ]
    segments: list[dict[str, str]] = []
    for index, match in enumerate(starts):
        if index + 1 < len(starts):
            end = starts[index + 1].start()
        else:
            # The final tab is followed by the closing tab-list markup and
            # then the tab widget's initialization script. Stopping at the
            # closing marker avoids pulling in site footer/nav links while
            # preserving scripts that appear inside resource cards.
            tail = body_html[match.start():]
            end_match = re.search(r"</ul>\s*</div>\s*<script", tail, re.S)
            end = match.start() + end_match.start() if end_match else -1
            if end == -1:
                end = body_html.find("page-bottom--area", match.start())
        if end == -1:
            end = len(body_html)
        segments.append({"area": match.group(1), "html": body_html[match.start():end]})
    return segments


def extract_main_content_segment(body_html: str) -> str:
    start = body_html.find('id="smv_Main"')
    if start == -1:
        return body_html
    end = body_html.find("page-bottom--area", start)
    return body_html[start:end if end != -1 else len(body_html)]


def extract_top(style: str) -> int:
    match = re.search(r"\btop:\s*(-?\d+)px", style)
    return int(match.group(1)) if match else 0


def extract_resource_blocks(tab_html: str) -> list[dict[str, object]]:
    area_pattern = re.compile(
        r'<div id="(smv_con_[^"]+)" ctype="area"[^>]*style="([^"]*)"[^>]*>',
        re.S,
    )
    matches = list(area_pattern.finditer(tab_html))
    blocks: list[dict[str, object]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(tab_html)
        segment = tab_html[match.start():end]
        text, links = extract_visible(segment)
        if not text and not links:
            continue
        blocks.append(
            {
                "id": match.group(1),
                "top": extract_top(match.group(2)),
                "text": text,
                "links": links,
            }
        )
    blocks.sort(key=lambda block: (int(block["top"]), str(block["id"])))
    return blocks


def extract_text_blocks(segment_html: str) -> list[dict[str, object]]:
    text_pattern = re.compile(
        r'<div id="(smv_con_[^"]+)" ctype="text"[^>]*style="([^"]*)"[^>]*>',
        re.S,
    )
    matches = list(text_pattern.finditer(segment_html))
    blocks: list[dict[str, object]] = []
    for index, match in enumerate(matches):
        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(segment_html)
        widget_end = segment_html.find("</script></div></div>", match.start())
        if widget_end != -1:
            widget_end += len("</script></div></div>")
            end = min(next_start, widget_end)
        else:
            end = next_start
        segment = segment_html[match.start():end]
        text, links = extract_visible(segment)
        if not text and not links:
            continue
        blocks.append(
            {
                "id": match.group(1),
                "top": extract_top(match.group(2)),
                "text": text,
                "links": links,
            }
        )
    blocks.sort(key=lambda block: (int(block["top"]), str(block["id"])))
    return blocks


def normalized_date(raw: str) -> str:
    raw = raw.strip()
    for fmt in ("%m/%d/%Y", "%m / %d / %Y", "%Y/%m/%d", "%Y / %m / %d"):
        try:
            return dt.datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            pass
    return ""


def extract_dates(text: str) -> list[tuple[str, str]]:
    dates: list[tuple[str, str]] = []
    seen: set[str] = set()
    for match in re.finditer(r"\b(?:\d{1,2}\s*/\s*\d{1,2}\s*/\s*\d{4}|\d{4}\s*/\s*\d{1,2}\s*/\s*\d{1,2})\b", text):
        raw = normalize_inline(match.group(0))
        if raw in seen:
            continue
        seen.add(raw)
        dates.append((raw, normalized_date(raw)))
    return dates


def classify_href(href: str) -> str:
    if not href:
        return "empty"
    lowered = href.lower()
    if lowered.startswith("javascript:"):
        return "javascript"
    if lowered.startswith("#"):
        return "fragment"
    return "url"


def clean_title_from_block(text: str) -> str:
    lines = [line for line in text.splitlines() if line and line.lower() not in {"download"}]
    if not lines:
        return ""
    for line in lines:
        if re.search(r"^[（(]\s*new\s*[）)]", line, re.I):
            title = re.sub(r"^[（(]\s*new\s*[）)]\s*", "", line, flags=re.I)
            return title[:160]
    title = re.sub(r"^[（(]\s*new\s*[）)]\s*", "", lines[0], flags=re.I)
    return title[:160]


def markdown_escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def render_inline_links(
    links: list[dict[str, str]],
    source_url: str,
) -> list[str]:
    lines: list[str] = []
    real_links: list[tuple[str, str, str]] = []

    for link in links:
        label = link["label"] or "(no label)"
        href = link["href"]
        kind = classify_href(href)
        if kind == "url":
            resolved = urljoin(source_url, href)
            real_links.append((label, href, resolved))

    if real_links:
        lines.append("- Links:")
        for label, href, resolved in real_links:
            if href == resolved:
                lines.append(f"  - {label}: {resolved}")
            else:
                lines.append(f"  - {label}: {href} -> {resolved}")

    return lines


def render_product_markdown(
    slug: str,
    product: str,
    source_url: str,
    outer_html: str,
    head_url: str,
    body_url: str,
    body_html: str,
    retrieved: str,
) -> str:
    page_title = first_match(r"<title>(.*?)</title>", outer_html) or product
    page_id = first_match(r'id=["\']pageinfo["\'][^>]*value=["\']([^"\']+)["\']', body_html)
    labels = extract_tab_labels(body_html)
    tab_segments = extract_tab_segments(body_html)
    if not tab_segments:
        tab_segments = [{"area": "main", "html": extract_main_content_segment(body_html), "fallback": "text"}]

    lines: list[str] = [
        f"# {product} Resources",
        "",
        "Raw supplier resource extraction from GPD. This file intentionally preserves source-page text and links for later wiki ingest.",
        "",
        "## Source Metadata",
        "",
        f"- Product slug: `{slug}`",
        f"- Source URL: {source_url}",
        f"- Page title: {page_title}",
        f"- Page ID: `{page_id}`" if page_id else "- Page ID: not found",
        f"- Retrieved: {retrieved}",
        f"- Head script: {head_url}",
        f"- Body script: {body_url}",
        "- Download policy: URLs only; firmware, driver, BIOS, archive, and executable files were not downloaded.",
        "",
        "## Tabs",
        "",
    ]

    real_link_rows: list[tuple[str, str, str, str, str]] = []
    non_url_rows: list[tuple[str, str, str, str]] = []
    all_tab_text: list[str] = []

    for index, tab in enumerate(tab_segments, 1):
        area = tab["area"]
        label = labels.get(area.replace("smc_", ""), labels.get(area, f"Tab {index}"))
        if tab.get("fallback") == "text":
            label = "Resources"
        text, tab_links = extract_visible(tab["html"])
        all_tab_text.append(text)
        blocks = extract_text_blocks(tab["html"]) if tab.get("fallback") == "text" else extract_resource_blocks(tab["html"])
        lines.extend([f"### {label}", "", f"- Tab area: `{area}`", f"- Resource blocks detected: {len(blocks)}", ""])

        if blocks:
            for block_index, block in enumerate(blocks, 1):
                block_text = str(block["text"])
                title = clean_title_from_block(block_text) or f"Resource block {block_index}"
                dates = extract_dates(block_text)
                lines.extend([f"#### {block_index}. {title}", ""])
                lines.append(f"- Block ID: `{block['id']}`; visual top: `{block['top']}px`")
                if dates:
                    rendered_dates = ", ".join(
                        f"{raw} -> {iso}" if iso else raw for raw, iso in dates
                    )
                    lines.append(f"- Dates found: {rendered_dates}")
                inline_link_lines = render_inline_links(block["links"], source_url)
                lines.extend(inline_link_lines)
                for link in block["links"]:
                    kind = classify_href(link["href"])
                    if kind == "url":
                        abs_url = urljoin(source_url, link["href"])
                        real_link_rows.append((label, title, link["label"] or "(no label)", link["href"], abs_url))
                    else:
                        non_url_rows.append((label, title, link["label"] or "(no label)", link["href"]))
                lines.extend(["", block_text or "(No visible text extracted.)", ""])
        else:
            inline_link_lines = render_inline_links(tab_links, source_url)
            for link in tab_links:
                kind = classify_href(link["href"])
                title = label
                if kind == "url":
                    abs_url = urljoin(source_url, link["href"])
                    real_link_rows.append((label, title, link["label"] or "(no label)", link["href"], abs_url))
                else:
                    non_url_rows.append((label, title, link["label"] or "(no label)", link["href"]))
            lines.extend(["#### Raw Tab Text", ""])
            lines.extend(inline_link_lines)
            lines.extend(["", text or "(No visible text extracted.)", ""])

    combined_text = "\n".join(all_tab_text)
    sha1_values = sorted(set(re.findall(r"\b[A-Fa-f0-9]{40}\b", combined_text)))
    password_lines = [
        normalize_inline(line)
        for line in combined_text.splitlines()
        if re.search(r"\b(password|WinRAR extraction password|Unzip Password)\b", line, re.I)
    ]

    lines.extend(["## Extracted Checksums", ""])
    if sha1_values:
        for value in sha1_values:
            lines.append(f"- SHA1: `{value.upper()}`")
    else:
        lines.append("- No SHA1-style checksums detected.")
    lines.append("")

    lines.extend(["## Password / Archive Notes", ""])
    if password_lines:
        for line in dict.fromkeys(password_lines):
            lines.append(f"- {line}")
    else:
        lines.append("- No password lines detected.")
    lines.append("")

    lines.extend(["## Link Table", ""])
    lines.append("| Tab | Resource context | Link label | Original href | Resolved URL |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in real_link_rows:
        lines.append("| " + " | ".join(markdown_escape_table(value) for value in row) + " |")
    lines.append("")

    lines.extend(["## Non-URL / Placeholder Links", ""])
    if non_url_rows:
        lines.append("| Tab | Resource context | Link label | Href |")
        lines.append("| --- | --- | --- | --- |")
        for row in non_url_rows:
            lines.append("| " + " | ".join(markdown_escape_table(value) for value in row) + " |")
    else:
        lines.append("- None detected.")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_manifest(status_rows: Iterable[tuple[str, str, str, str, str, str]], retrieved: str) -> str:
    lines = [
        "# GPD Supplier Resource Pages",
        "",
        "Raw manifest for GPD firmware, driver, BIOS, tool, and OS resource pages.",
        "",
        f"- Retrieved/status checked: {retrieved}",
        "- Download policy: URLs only; linked binaries are not downloaded.",
        "",
        "| Product slug | Product | Source URL | HTTP/status | Page ID | Static JS pattern |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in status_rows:
        lines.append("| " + " | ".join(markdown_escape_table(value) for value in row) + " |")
    return "\n".join(lines).rstrip() + "\n"


def fetch_page_metadata(slug: str, product: str, url: str) -> tuple[str, str, str, str, str, str, str]:
    outer_html = fetch_text(url)
    head_url, body_url = extract_script_urls(url, outer_html)
    page_id = ""
    static_pattern = "missing"
    if body_url:
        body_js = fetch_text(body_url)
        body_html = decode_document_write(body_js)
        page_id = first_match(r'id=["\']pageinfo["\'][^>]*value=["\']([^"\']+)["\']', body_html)
        static_pattern = "Head.js/Body.js" if head_url else "Body.js"
    else:
        body_html = ""
    return slug, product, url, outer_html, head_url, body_url, page_id, static_pattern


def resource_filename(slug: str) -> str:
    return f"{slug.upper().replace('-', '-')}-Resources.md"


def write_product(output_root: Path, slug: str, product: str, url: str, retrieved: str) -> None:
    outer_html = fetch_text(url)
    head_url, body_url = extract_script_urls(url, outer_html)
    body_html = decode_document_write(fetch_text(body_url))
    markdown = render_product_markdown(slug, product, url, outer_html, head_url, body_url, body_html, retrieved)
    product_dir = output_root / slug
    product_dir.mkdir(parents=True, exist_ok=True)
    (product_dir / resource_filename(slug)).write_text(markdown, encoding="utf-8")


def write_products(output_root: Path, retrieved: str, only_slug: str | None = None) -> None:
    for slug, product, url in GPD_SOURCE_PAGES:
        if only_slug and slug != only_slug:
            continue
        write_product(output_root, slug, product, url, retrieved)


def write_manifest(output_root: Path, retrieved: str) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, str, str, str, str, str]] = []
    for slug, product, url in GPD_SOURCE_PAGES:
        try:
            _, _, _, outer_html, head_url, body_url, page_id, static_pattern = fetch_page_metadata(slug, product, url)
            http_status = "200 fetched"
            if not body_url:
                static_pattern = "missing Body.js"
            elif not head_url:
                static_pattern = "missing Head.js"
            rows.append((slug, product, url, http_status, page_id or "", static_pattern))
        except Exception as exc:  # noqa: BLE001 - preserve manifest failure details.
            rows.append((slug, product, url, f"error: {type(exc).__name__}: {exc}", "", "unknown"))
    (output_root / "source-pages.md").write_text(render_manifest(rows, retrieved), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-root",
        default="raw/supplier-resources/gpd",
        help="Directory where extracted raw supplier resources are written.",
    )
    parser.add_argument(
        "--retrieved",
        default=dt.date.today().isoformat(),
        help="Retrieval date to stamp into generated Markdown.",
    )
    parser.add_argument(
        "--skip-manifest",
        action="store_true",
        help="Only write product resource files.",
    )
    parser.add_argument(
        "--only",
        help="Only write one product slug, e.g. gpd-win-5.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_root = Path(args.output_root)
    if not args.skip_manifest:
        write_manifest(output_root, args.retrieved)
    write_products(output_root, args.retrieved, args.only)


if __name__ == "__main__":
    main()

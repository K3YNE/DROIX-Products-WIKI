#!/usr/bin/env python3
"""Extract AYANEO download resources into raw Markdown sources.

AYANEO's support/download page renders resources from JSON endpoints. This
script preserves the API data as a raw supplier source and writes one Markdown
file per top-level category or child product category.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE_URL = "https://ayaneo.com"
SOURCE_PAGE_URL = f"{BASE_URL}/support/download"
TOP_LIST_PATH = "/download/download/top-list"
ITEM_LIST_PATH = "/download/download/item-list"
USER_AGENT = "Mozilla/5.0 (compatible; raw-resource-extractor/1.0)"


def fetch_json(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    url = BASE_URL + path
    if params:
        url += "?" + urlencode(params)
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=45) as response:
        return json.loads(response.read().decode("utf-8"))


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "untitled"


def resource_filename(title: str) -> str:
    safe = slugify(title).upper()
    return f"{safe}-Resources.md"


def iso_from_epoch(value: Any) -> str:
    if value in ("", None):
        return ""
    try:
        timestamp = int(value)
    except (TypeError, ValueError):
        return ""
    return dt.datetime.fromtimestamp(timestamp, tz=dt.timezone.utc).isoformat().replace("+00:00", "Z")


def markdown_escape_table(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", "<br>")


def render_item(item: dict[str, Any]) -> list[str]:
    updated_iso = iso_from_epoch(item.get("updated_at"))
    lines = [
        f"### {item.get('title') or '(Untitled resource)'}",
        "",
        f"- ID: `{item.get('id', '')}`",
        f"- Type ID: `{item.get('type_id', '')}`",
        f"- Version: {item.get('version') or ''}",
        f"- Description: {item.get('desc') or ''}",
        f"- Raw updated_at: `{item.get('updated_at', '')}`",
        f"- Updated UTC: {updated_iso}",
        f"- Link type: `{item.get('type', '')}`",
        f"- Show: `{item.get('show', '')}`",
        f"- Sort: `{item.get('sort', '')}`",
    ]
    download_url = item.get("download_url") or ""
    if download_url:
        lines.extend(["- Links:", f"  - Download: {download_url}"])
    else:
        lines.append("- Links: none")
    lines.append("")
    return lines


def render_resource_file(
    title: str,
    slug: str,
    type_id: int,
    retrieved: str,
    items: list[dict[str, Any]],
    parent_title: str | None,
    parent_id: int | None,
    page_count: int,
    total_count: int,
) -> str:
    lines = [
        f"# {title} Resources",
        "",
        "Raw supplier resource extraction from AYANEO. This file preserves API-provided text and download URLs for later wiki ingest.",
        "",
        "## Source Metadata",
        "",
        f"- Source page: {SOURCE_PAGE_URL}",
        f"- API endpoint: {BASE_URL}{ITEM_LIST_PATH}?type_id={type_id}&page=<page>",
        f"- Type ID: `{type_id}`",
        f"- Slug: `{slug}`",
        f"- Parent category: {parent_title or '(top-level category)'}",
        f"- Parent ID: `{parent_id}`" if parent_id is not None else "- Parent ID: none",
        f"- Retrieved: {retrieved}",
        "- Download policy: URLs only; linked firmware, driver, archive, and executable files were not downloaded.",
        "",
        "## API Counts",
        "",
        f"- Resource records in this file: {len(items)}",
        f"- API totalCount for this type: {total_count}",
        f"- API pageCount for this type: {page_count}",
        "",
        "## Resources",
        "",
    ]
    if items:
        for item in items:
            lines.extend(render_item(item))
    else:
        lines.append("- No resources currently returned by the AYANEO API for this type.")
        lines.append("")

    lines.extend(
        [
            "## Link Table",
            "",
            "| ID | Title | Version | Updated UTC | Download URL |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in items:
        lines.append(
            "| "
            + " | ".join(
                markdown_escape_table(value)
                for value in [
                    item.get("id", ""),
                    item.get("title", ""),
                    item.get("version", ""),
                    iso_from_epoch(item.get("updated_at")),
                    item.get("download_url", ""),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def fetch_all_items(type_id: int) -> tuple[list[dict[str, Any]], dict[str, Any], list[dict[str, Any]]]:
    first = fetch_json(ITEM_LIST_PATH, {"type_id": type_id, "page": 1})
    if first.get("status") != 200:
        raise RuntimeError(f"item-list failed for type_id={type_id}: {first}")
    data = first["data"]
    page_count = int(data.get("pageCount") or 0)
    all_items = list(data.get("download_list") or [])
    child_types = list(data.get("child_types") or [])
    for page in range(2, page_count + 1):
        response = fetch_json(ITEM_LIST_PATH, {"type_id": type_id, "page": page})
        if response.get("status") != 200:
            raise RuntimeError(f"item-list failed for type_id={type_id}, page={page}: {response}")
        all_items.extend(response["data"].get("download_list") or [])
    summary = {
        "pageCount": page_count,
        "totalCount": int(data.get("totalCount") or 0),
        "perPage": int(data.get("perPage") or 0),
        "currentPage": int(data.get("currentPage") or 1),
    }
    return all_items, summary, child_types


def split_items_by_type(items: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    grouped: dict[int, list[dict[str, Any]]] = {}
    for item in items:
        grouped.setdefault(int(item["type_id"]), []).append(item)
    for group in grouped.values():
        group.sort(key=lambda item: (-int(item.get("sort") or 0), -int(item.get("updated_at") or 0), int(item.get("id") or 0)))
    return grouped


def render_manifest(snapshot: dict[str, Any], retrieved: str) -> str:
    lines = [
        "# AYANEO Supplier Resource Pages",
        "",
        "Raw manifest for AYANEO support/download resources.",
        "",
        f"- Source page: {SOURCE_PAGE_URL}",
        f"- Top-list API: {BASE_URL}{TOP_LIST_PATH}",
        f"- Item-list API: {BASE_URL}{ITEM_LIST_PATH}?type_id=<id>&page=<page>",
        f"- Retrieved/status checked: {retrieved}",
        "- Download policy: URLs only; linked binaries are not downloaded.",
        "",
        "## Summary",
        "",
        f"- Top categories: {len(snapshot['categories'])}",
        f"- Unique resource IDs: {len(snapshot['unique_resource_ids'])}",
        "",
        "| Type ID | Category/Product | Parent | API totalCount | Fetched records | Pages | Output |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in snapshot["outputs"]:
        lines.append(
            "| "
            + " | ".join(
                markdown_escape_table(value)
                for value in [
                    entry["type_id"],
                    entry["title"],
                    entry.get("parent_title") or "",
                    entry["api_total_count"],
                    entry["fetched_count"],
                    entry["page_count"],
                    entry["path"],
                ]
            )
            + " |"
        )
    return "\n".join(lines).rstrip() + "\n"


def build_snapshot() -> dict[str, Any]:
    top_response = fetch_json(TOP_LIST_PATH)
    if top_response.get("status") != 200:
        raise RuntimeError(f"top-list failed: {top_response}")

    categories = top_response["data"]
    all_outputs: list[dict[str, Any]] = []
    raw_categories: list[dict[str, Any]] = []
    unique_resource_ids: set[int] = set()

    for category in categories:
        category_id = int(category["id"])
        category_items, category_summary, child_types = fetch_all_items(category_id)
        grouped = split_items_by_type(category_items)

        raw_category = {
            "category": category,
            "summary": category_summary,
            "child_types": child_types,
            "items": category_items,
        }
        raw_categories.append(raw_category)

        parent_items = grouped.get(category_id, [])
        for item in parent_items:
            unique_resource_ids.add(int(item["id"]))
        all_outputs.append(
            {
                "type_id": category_id,
                "title": category["title"],
                "slug": slugify(category["title"]),
                "parent_id": None,
                "parent_title": None,
                "items": parent_items,
                "page_count": category_summary["pageCount"],
                "api_total_count": len(parent_items) if child_types else category_summary["totalCount"],
            }
        )

        for child in child_types:
            child_id = int(child["id"])
            child_items, child_summary, _ = fetch_all_items(child_id)
            for item in child_items:
                unique_resource_ids.add(int(item["id"]))
            all_outputs.append(
                {
                    "type_id": child_id,
                    "title": child["title"],
                    "slug": slugify(child["title"]),
                    "parent_id": category_id,
                    "parent_title": category["title"],
                    "items": child_items,
                    "page_count": child_summary["pageCount"],
                    "api_total_count": child_summary["totalCount"],
                }
            )

    return {
        "source_page": SOURCE_PAGE_URL,
        "top_list_endpoint": BASE_URL + TOP_LIST_PATH,
        "item_list_endpoint": BASE_URL + ITEM_LIST_PATH,
        "categories": raw_categories,
        "outputs": all_outputs,
        "unique_resource_ids": sorted(unique_resource_ids),
    }


def write_outputs(output_root: Path, retrieved: str) -> None:
    snapshot = build_snapshot()
    output_root.mkdir(parents=True, exist_ok=True)

    serializable_snapshot = {
        **snapshot,
        "retrieved": retrieved,
    }
    (output_root / "catalog.json").write_text(
        json.dumps(serializable_snapshot, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    for entry in snapshot["outputs"]:
        parent_slug = slugify(entry["parent_title"]) if entry.get("parent_title") else slugify(entry["title"])
        target_dir = output_root / parent_slug
        if entry.get("parent_title"):
            target_dir = target_dir / entry["slug"]
        target_dir.mkdir(parents=True, exist_ok=True)
        filename = resource_filename(entry["title"])
        relative_path = target_dir / filename
        relative_path.write_text(
            render_resource_file(
                entry["title"],
                entry["slug"],
                entry["type_id"],
                retrieved,
                entry["items"],
                entry.get("parent_title"),
                entry.get("parent_id"),
                entry["page_count"],
                entry["api_total_count"],
            ),
            encoding="utf-8",
        )
        entry["path"] = str(relative_path.relative_to(output_root))
        entry["fetched_count"] = len(entry["items"])

    (output_root / "source-pages.md").write_text(render_manifest(snapshot, retrieved), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-root",
        default="raw/supplier-resources/ayaneo",
        help="Directory where extracted raw AYANEO supplier resources are written.",
    )
    parser.add_argument(
        "--retrieved",
        default=dt.date.today().isoformat(),
        help="Retrieval date to stamp into generated Markdown.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    write_outputs(Path(args.output_root), args.retrieved)


if __name__ == "__main__":
    main()

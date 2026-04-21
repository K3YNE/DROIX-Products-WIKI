#!/usr/bin/env python3
"""Extract ONEXPLAYER resources and FAQs into raw Markdown sources.

The ONEXPLAYER support page is Shopify HTML. Driver resources are rendered as
model options in a select.tutorial-down element with matching hidden
.tutorial-MAG2 panels. This script preserves the visible text and outbound URLs
without downloading linked firmware, driver, BIOS, archive, or executable files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup, Comment
from bs4.element import NavigableString, Tag


SOURCE_URL = "https://onexplayerstore.com/pages/drivers-and-faqs"
USER_AGENT = "Mozilla/5.0 (compatible; raw-resource-extractor/1.0)"
FAQ_SECTION_IDS = ["general-faqs", "onexsugar", "onexplayer-g1", "onexgpu-2"]


@dataclass
class FetchResult:
    url: str
    status: int
    text: str


@dataclass
class LinkRecord:
    context: str
    label: str
    href: str
    resolved_url: str


@dataclass
class ResourceBlock:
    number: str
    title: str
    body_markdown: str
    links: list[LinkRecord]


@dataclass
class ModelResources:
    label: str
    value: str
    panel_id: str
    slug: str
    output_path: str
    blocks: list[ResourceBlock]


def fetch_page(url: str) -> FetchResult:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=45) as response:
        return FetchResult(
            url=response.geturl(),
            status=int(response.status),
            text=response.read().decode("utf-8", "replace"),
        )


def slugify(value: str) -> str:
    value = html.unescape(value).lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "untitled"


def resource_filename(title: str) -> str:
    return f"{slugify(title).upper()}-Resources.md"


def normalize_inline(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text).replace("\xa0", " ")).strip()


def markdown_escape_table(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", "<br>")


def clean_soup(soup: BeautifulSoup) -> None:
    for comment in soup.find_all(string=lambda value: isinstance(value, Comment)):
        comment.extract()
    for tag in soup(["script", "style", "svg"]):
        tag.decompose()


def page_title(soup: BeautifulSoup) -> str:
    if not soup.title:
        return ""
    return normalize_inline(soup.title.get_text(" ", strip=True))


def node_to_markdown(node: Tag | NavigableString, base_url: str) -> list[str]:
    if isinstance(node, NavigableString):
        text = normalize_inline(str(node))
        return [text] if text else []

    if not isinstance(node, Tag):
        return []

    if node.name == "br":
        return [""]

    if node.name == "a":
        label = normalize_inline(node.get_text(" ", strip=True)) or "(no label)"
        href = node.get("href", "")
        if href:
            return [f"[{label}]({urljoin(base_url, href)})"]
        return [label]

    child_parts: list[str] = []
    for child in node.children:
        child_parts.extend(node_to_markdown(child, base_url))

    inline_tags = {"span", "strong", "b", "em", "i", "small"}
    if node.name in inline_tags:
        text = normalize_inline(" ".join(part for part in child_parts if part))
        return [text] if text else []

    if node.name == "li":
        text = normalize_inline(" ".join(part for part in child_parts if part))
        return [f"- {text}"] if text else []

    lines: list[str] = []
    text = normalize_inline(" ".join(part for part in child_parts if part))
    if text:
        lines.append(text)
    return lines


def element_markdown(element: Tag | None, base_url: str) -> str:
    if element is None:
        return ""
    lines: list[str] = []
    for child in element.children:
        child_lines = node_to_markdown(child, base_url)
        for line in child_lines:
            if line or (lines and lines[-1]):
                lines.append(line)
    compact: list[str] = []
    for line in lines:
        normalized = normalize_inline(line)
        if normalized:
            compact.append(normalized)
    return "\n".join(compact)


def extract_link_records(element: Tag | None, base_url: str, context: str) -> list[LinkRecord]:
    if element is None:
        return []
    records: list[LinkRecord] = []
    for link in element.find_all("a", href=True):
        href = str(link.get("href", ""))
        label = normalize_inline(link.get_text(" ", strip=True)) or "(no label)"
        records.append(LinkRecord(context=context, label=label, href=href, resolved_url=urljoin(base_url, href)))
    return records


def title_from_tutorial_li(tag: Tag) -> tuple[str, str]:
    number_tag = tag.find("em")
    number = normalize_inline(number_tag.get_text(" ", strip=True)) if number_tag else ""
    title = normalize_inline(tag.get_text(" ", strip=True))
    if number and title.startswith(number):
        title = normalize_inline(title[len(number) :])
    return number, title


def extract_resource_blocks(panel: Tag, base_url: str) -> list[ResourceBlock]:
    blocks: list[ResourceBlock] = []
    for item in panel.select(".tutorial-li"):
        number, title = title_from_tutorial_li(item)
        content = item.find_next_sibling("div", class_="hideDownloadContent")
        body = element_markdown(content, base_url)
        links = extract_link_records(content, base_url, title)
        blocks.append(ResourceBlock(number=number, title=title, body_markdown=body, links=links))
    return blocks


def extract_models(soup: BeautifulSoup, base_url: str) -> list[ModelResources]:
    select = soup.select_one("select.tutorial-down")
    if select is None:
        raise RuntimeError("Could not find select.tutorial-down on ONEXPLAYER source page")

    options = select.select("option")
    panels = soup.select(".tutorial-MAG2")
    if len(options) != len(panels):
        raise RuntimeError(f"Model option/panel mismatch: {len(options)} options, {len(panels)} panels")

    models: list[ModelResources] = []
    for option, panel in zip(options, panels):
        label = normalize_inline(option.get_text(" ", strip=True))
        value = normalize_inline(str(option.get("value", "")))
        slug = slugify(label)
        output_path = f"{slug}/{resource_filename(label)}"
        models.append(
            ModelResources(
                label=label,
                value=value,
                panel_id=str(panel.get("id", "")),
                slug=slug,
                output_path=output_path,
                blocks=extract_resource_blocks(panel, base_url),
            )
        )
    return models


def render_model_markdown(model: ModelResources, source_url: str, page_title_text: str, status: int, retrieved: str) -> str:
    link_rows: list[LinkRecord] = [link for block in model.blocks for link in block.links]
    lines = [
        f"# {model.label} Resources",
        "",
        "Raw supplier resource extraction from ONEXPLAYER. This file preserves source-page text and download URLs for later wiki ingest.",
        "",
        "## Source Metadata",
        "",
        f"- Source URL: {source_url}",
        f"- HTTP status: {status}",
        f"- Page title: {page_title_text}",
        f"- Retrieved: {retrieved}",
        f"- Model label: {model.label}",
        f"- Model value: `{model.value}`",
        f"- Panel ID: `{model.panel_id}`",
        f"- Model slug: `{model.slug}`",
        "- Download policy: URLs only; linked BIOS, driver, firmware, system-pack, executable, archive, Google Drive, OneDrive, AMD, and Intel files were not downloaded.",
        "",
        "## Resources",
        "",
    ]

    if not model.blocks:
        lines.append("- No resource blocks detected for this model.")
        lines.append("")
    for index, block in enumerate(model.blocks, 1):
        title = block.title or f"Resource block {index}"
        lines.extend([f"### {index}. {title}", ""])
        lines.append(f"- Source item number: `{block.number or index}`")
        if block.links:
            lines.append("- Links:")
            for link in block.links:
                lines.append(f"  - {link.label}: {link.resolved_url}")
        else:
            lines.append("- Links: none")
        lines.append("")
        lines.append(block.body_markdown or "(No visible instructions extracted.)")
        lines.append("")

    lines.extend(
        [
            "## Link Table",
            "",
            "| Resource context | Link label | Original href | Resolved URL |",
            "| --- | --- | --- | --- |",
        ]
    )
    for link in link_rows:
        lines.append(
            "| "
            + " | ".join(markdown_escape_table(value) for value in [link.context, link.label, link.href, link.resolved_url])
            + " |"
        )
    if not link_rows:
        lines.append("|  |  |  |  |")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def extract_faq_sections(soup: BeautifulSoup, base_url: str) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    for section_id in FAQ_SECTION_IDS:
        section = soup.find(id=section_id)
        if not isinstance(section, Tag):
            continue
        heading = section.find("h3")
        entries: list[dict[str, str]] = []
        for item in section.select(".drives-faqs-item"):
            question = item.select_one(".drives-faqs-question")
            answer = item.select_one(".drives-faqs-answer")
            entries.append(
                {
                    "question": normalize_inline(question.get_text(" ", strip=True)) if question else "",
                    "answer": element_markdown(answer, base_url),
                }
            )
        sections.append(
            {
                "id": section_id,
                "title": normalize_inline(heading.get_text(" ", strip=True)) if heading else section_id,
                "entries": entries,
            }
        )
    return sections


def render_faq_markdown(
    sections: list[dict[str, Any]],
    source_url: str,
    page_title_text: str,
    status: int,
    retrieved: str,
) -> str:
    total = sum(len(section["entries"]) for section in sections)
    lines = [
        "# ONEXPLAYER FAQs",
        "",
        "Raw supplier FAQ extraction from ONEXPLAYER. This file preserves FAQ questions and answers for later wiki ingest.",
        "",
        "## Source Metadata",
        "",
        f"- Source URL: {source_url}",
        f"- HTTP status: {status}",
        f"- Page title: {page_title_text}",
        f"- Retrieved: {retrieved}",
        f"- FAQ sections: {len(sections)}",
        f"- FAQ Q&A items: {total}",
        "",
        "## FAQs",
        "",
    ]
    for section in sections:
        lines.extend([f"### {section['title']}", "", f"- Section ID: `{section['id']}`", f"- Q&A items: {len(section['entries'])}", ""])
        for index, entry in enumerate(section["entries"], 1):
            lines.extend([f"#### {index}. {entry['question']}", "", entry["answer"] or "(No answer text extracted.)", ""])
    return "\n".join(lines).rstrip() + "\n"


def render_manifest(
    models: list[ModelResources],
    faq_sections: list[dict[str, Any]],
    source_url: str,
    page_title_text: str,
    status: int,
    retrieved: str,
) -> str:
    resource_total = sum(len(model.blocks) for model in models)
    link_total = sum(len(block.links) for model in models for block in model.blocks)
    faq_total = sum(len(section["entries"]) for section in faq_sections)
    lines = [
        "# ONEXPLAYER Supplier Resource Pages",
        "",
        "Raw manifest for ONEXPLAYER driver, firmware, BIOS, system-pack, tool, and FAQ resources.",
        "",
        f"- Source page: {source_url}",
        f"- HTTP status: {status}",
        f"- Page title: {page_title_text}",
        f"- Retrieved/status checked: {retrieved}",
        "- Download policy: URLs only; linked binaries are not downloaded.",
        "",
        "## Summary",
        "",
        f"- Model options: {len(models)}",
        f"- Model resource blocks: {resource_total}",
        f"- Model download links: {link_total}",
        f"- FAQ sections: {len(faq_sections)}",
        f"- FAQ Q&A items: {faq_total}",
        "",
        "## Model Outputs",
        "",
        "| Model value | Model label | Panel ID | Resource blocks | Download links | Output |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for model in models:
        links = sum(len(block.links) for block in model.blocks)
        lines.append(
            "| "
            + " | ".join(
                markdown_escape_table(value)
                for value in [model.value, model.label, model.panel_id, len(model.blocks), links, model.output_path]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## FAQ Outputs",
            "",
            "| Section ID | Section | Q&A items |",
            "| --- | --- | --- |",
        ]
    )
    for section in faq_sections:
        lines.append(
            "| "
            + " | ".join(markdown_escape_table(value) for value in [section["id"], section["title"], len(section["entries"])])
            + " |"
        )
    lines.extend(["", "- FAQ output: faqs/ONEXPLAYER-FAQs.md", ""])
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(output_root: Path, retrieved: str) -> dict[str, int]:
    fetched = fetch_page(SOURCE_URL)
    soup = BeautifulSoup(fetched.text, "html.parser")
    clean_soup(soup)
    title = page_title(soup)
    source_url = fetched.url

    models = extract_models(soup, source_url)
    faq_sections = extract_faq_sections(soup, source_url)

    for model in models:
        product_dir = output_root / model.slug
        product_dir.mkdir(parents=True, exist_ok=True)
        (product_dir / resource_filename(model.label)).write_text(
            render_model_markdown(model, source_url, title, fetched.status, retrieved),
            encoding="utf-8",
        )

    faq_dir = output_root / "faqs"
    faq_dir.mkdir(parents=True, exist_ok=True)
    (faq_dir / "ONEXPLAYER-FAQs.md").write_text(
        render_faq_markdown(faq_sections, source_url, title, fetched.status, retrieved),
        encoding="utf-8",
    )

    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "source-pages.md").write_text(
        render_manifest(models, faq_sections, source_url, title, fetched.status, retrieved),
        encoding="utf-8",
    )

    return {
        "models": len(models),
        "resource_blocks": sum(len(model.blocks) for model in models),
        "download_links": sum(len(block.links) for model in models for block in model.blocks),
        "faq_sections": len(faq_sections),
        "faq_items": sum(len(section["entries"]) for section in faq_sections),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract ONEXPLAYER resources and FAQs to raw Markdown.")
    parser.add_argument(
        "--output-root",
        default="raw/supplier-resources/onexplayer",
        help="Directory where ONEXPLAYER raw supplier resources should be written.",
    )
    parser.add_argument(
        "--retrieved",
        default=dt.date.today().isoformat(),
        help="ISO date to record as the retrieval date.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    counts = write_outputs(Path(args.output_root), args.retrieved)
    print(
        "Extracted "
        f"{counts['models']} models, "
        f"{counts['resource_blocks']} resource blocks, "
        f"{counts['download_links']} download links, "
        f"{counts['faq_sections']} FAQ sections, "
        f"{counts['faq_items']} FAQ Q&A items."
    )


if __name__ == "__main__":
    main()

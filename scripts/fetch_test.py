#!/usr/bin/env python3
"""Phase 1: Test fetch — 1 article/product per source to validate quality."""

import html
import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

INGEST = Path(__file__).parent.parent / "raw" / "ingest"
BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


# ── Helpers ───────────────────────────────────────────────────────────────

def slugify(text):
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def clean_title(text):
    return html.unescape(text).strip()


def parse_date(date_str):
    if not date_str:
        return datetime.now().strftime("%Y-%m-%d")
    s = date_str.strip()
    if len(s) >= 10 and s[4] == "-":
        return s[:10]
    for fmt in ("%d %B %Y", "%B %d, %Y", "%d %b %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return datetime.now().strftime("%Y-%m-%d")


def clean_html(soup_el):
    """Remove noise elements: style/script, review widgets, images."""
    # Remove style/script/noscript
    for tag in soup_el(["style", "script", "noscript"]):
        tag.decompose()
    # Remove droix review widget (star ratings, pros/cons summary block)
    for tag in soup_el.select(".review-wrapper, [class*='wp-review'], [class*='wpr-']"):
        tag.decompose()
    # Remove all images (alt text creates noise in markdown)
    for tag in soup_el.find_all("img"):
        tag.decompose()
    return soup_el


def html_to_md(html_str):
    soup = BeautifulSoup(html_str, "html.parser")
    clean_html(soup)
    return md(str(soup), heading_style="ATX").strip()


def save_md(path, frontmatter: dict, body: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, str) and any(c in v for c in [':', '#', '"', "'"]):
            v = json.dumps(v)
        fm_lines.append(f"{k}: {v}")
    fm_lines.append("---")
    path.write_text("\n".join(fm_lines) + "\n\n" + body, encoding="utf-8")
    print(f"  Saved: {path.relative_to(Path(__file__).parent.parent)}")


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Saved: {path.relative_to(Path(__file__).parent.parent)}")


# ── 1A: gpdstore.net review ───────────────────────────────────────────────

def fetch_gpdstore_review():
    print("\n[1A] gpdstore.net — 1 review post")
    url = "https://gpdstore.net/wp-json/wp/v2/posts?categories=56&per_page=1&orderby=date&order=desc&_fields=id,title,link,date,content"
    r = requests.get(url, headers=BROWSER_HEADERS, timeout=30)
    r.raise_for_status()
    posts = r.json()
    if not posts:
        print("  ERROR: No posts returned"); return
    p = posts[0]
    title = clean_title(p["title"]["rendered"])
    date = p["date"][:10]
    fm = {"title": title, "source_url": p["link"], "source_site": "gpdstore.net",
          "type": "review-blog", "date": date, "wp_id": p["id"]}
    save_md(INGEST / "blog" / "gpdstore-reviews" / f"{date}-{slugify(title)}.md",
            fm, html_to_md(p["content"]["rendered"]))


# ── 1B: gpdstore.net KB ──────────────────────────────────────────────────

def fetch_gpdstore_kb():
    print("\n[1B] gpdstore.net — 1 KB article")
    url = "https://gpdstore.net/wp-json/wp/v2/docs?per_page=1&orderby=date&order=desc&_fields=id,title,link,date,content,doc_category"
    r = requests.get(url, headers=BROWSER_HEADERS, timeout=30)
    r.raise_for_status()
    docs = r.json()
    if not docs:
        print("  ERROR: No docs returned"); return
    d = docs[0]
    title = clean_title(d["title"]["rendered"])
    date = d["date"][:10]
    fm = {"title": title, "source_url": d["link"], "source_site": "gpdstore.net",
          "type": "kb-article", "date": date, "wp_id": d["id"]}
    save_md(INGEST / "kb" / "gpdstore-kb" / f"{slugify(title)}.md",
            fm, html_to_md(d["content"]["rendered"]))


# ── 1C: droix.net KB ─────────────────────────────────────────────────────

def fetch_droix_kb():
    print("\n[1C] droix.net — 1 KB article")
    url = "https://droix.net/knowledge-base/wp-json/wp/v2/kb?per_page=1&orderby=date&order=desc&_fields=id,title,link,date,content"
    r = requests.get(url, headers=BROWSER_HEADERS, timeout=30)
    r.raise_for_status()
    articles = r.json()
    if not articles:
        print("  ERROR: No articles returned"); return
    a = articles[0]
    title = clean_title(a["title"]["rendered"])
    date = a["date"][:10]
    fm = {"title": title, "source_url": a["link"], "source_site": "droix.net",
          "type": "kb-article", "date": date, "wp_id": a["id"]}
    save_md(INGEST / "kb" / "droix-kb" / f"{slugify(title)}.md",
            fm, html_to_md(a["content"]["rendered"]))


# ── 1D: droix.net review via scraping ────────────────────────────────────

def fetch_droix_review():
    print("\n[1D] droix.net — 1 review post (scraping)")
    listing_url = "https://droix.net/blogs/category/reviews/"
    r = requests.get(listing_url, headers=BROWSER_HEADERS, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    # Review cards are .p-grid inside .content-inner (sidebar uses .p-list — skip those)
    card = soup.select_one(".content-inner .p-wrap")
    if not card:
        print("  ERROR: Could not find review card on listing page"); return

    link_el = card.select_one("a.p-flink")
    title_el = card.select_one("a.p-url")
    date_el = card.select_one("abbr.date.published")

    article_url = link_el["href"] if link_el else None
    listing_title = clean_title(title_el.get_text()) if title_el else None
    listing_date = parse_date(date_el.get_text(strip=True) if date_el else None)

    if not article_url:
        print("  ERROR: No article link in review card"); return
    print(f"  Found: {article_url}  [{listing_date}]")

    r2 = requests.get(article_url, headers=BROWSER_HEADERS, timeout=30)
    r2.raise_for_status()
    soup2 = BeautifulSoup(r2.text, "html.parser")

    h1 = soup2.select_one("h1")
    title = clean_title(h1.get_text()) if h1 else (listing_title or "Unknown")

    body_el = soup2.select_one("article .entry-content") or soup2.select_one("article")
    body = html_to_md(str(body_el)) if body_el else ""

    fm = {"title": title, "source_url": article_url, "source_site": "droix.net",
          "type": "review-blog", "date": listing_date}
    save_md(INGEST / "blog" / "droix-reviews" / f"{listing_date}-{slugify(title)}.md", fm, body)


# ── 1E: Shop products — gpdstore.net (1 page) + droix.net (1 page, no GPD dupes) ──

def scrape_shop_page(url):
    """Return list of {title, href, instock} from a WooCommerce shop listing page."""
    r = requests.get(url, headers=BROWSER_HEADERS, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    products = []
    for li in soup.select("li.product"):
        link = li.select_one("a[href*='/product/']")
        title_el = li.select_one(".woocommerce-loop-product__title, h2")
        if not link or not title_el:
            continue
        products.append({
            "title": clean_title(title_el.get_text()),
            "href": link["href"].split("?")[0].rstrip("/"),
            "instock": "instock" in li.get("class", []),
        })
    return products


def fetch_shop_products():
    print("\n[1E] Shop products — 1 page each from gpdstore + droix (dedup test)")

    # gpdstore page 1
    gpd_products = scrape_shop_page("https://gpdstore.net/shop/")
    print(f"  gpdstore page 1: {len(gpd_products)} products")

    # Build dedup key set from gpdstore (normalised title)
    gpd_keys = {slugify(p["title"]) for p in gpd_products}
    # Also deduplicate on URL slug (last path segment)
    gpd_slugs = {p["href"].rstrip("/").split("/")[-1] for p in gpd_products}

    # droix page 1 — skip any product whose normalised title or URL slug matches gpdstore
    droix_products_raw = scrape_shop_page("https://droix.net/shop/")
    droix_products = []
    skipped = []
    for p in droix_products_raw:
        url_slug = p["href"].rstrip("/").split("/")[-1]
        if slugify(p["title"]) in gpd_keys or url_slug in gpd_slugs:
            skipped.append(p["title"])
        else:
            droix_products.append(p)

    print(f"  droix page 1: {len(droix_products_raw)} products — kept {len(droix_products)}, skipped {len(skipped)} (duplicates)")
    if skipped:
        print(f"  Skipped: {skipped[:5]}{'...' if len(skipped)>5 else ''}")

    # Save combined sample
    out = {
        "fetched": datetime.now().strftime("%Y-%m-%d"),
        "gpdstore_sample": gpd_products[:5],
        "droix_sample": droix_products[:5],
        "droix_skipped_sample": skipped[:5],
    }
    save_json(INGEST / "product" / "shop-products" / "sample-products.json", out)


# ── Main ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Phase 1: Test fetch — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    fetch_gpdstore_review()
    fetch_gpdstore_kb()
    fetch_droix_kb()
    fetch_droix_review()
    fetch_shop_products()
    print("\nDone. Review files in raw/ingest/ before proceeding to Phase 2.")

#!/usr/bin/env python3
"""
Phase 2: Full fetch of all sources into raw/ingest/.

Order of operations (matters for dedup):
  1. gpdstore reviews      (WP REST API)
  2. gpdstore KB           (WP REST API)
  3. gpdstore shop         (HTML scrape, pages 1-6)
  4. droix KB              (WP REST API, paginated — skip GPD dupes)
  5. droix reviews         (HTML scrape, listing pages 1-11)
  6. droix shop            (HTML scrape, pages 1-16 — skip GPD + gpdstore dupes)
  7. MANIFEST.md
"""

import html
import json
import re
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

INGEST = Path(__file__).parent.parent / "raw" / "ingest"
BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}
DELAY = 0.5  # seconds between requests

# Tracks everything for the manifest
stats = {
    "gpdstore_reviews": 0,
    "gpdstore_kb": 0,
    "gpdstore_shop": 0,
    "droix_kb": 0,
    "droix_kb_skipped": 0,
    "droix_reviews": 0,
    "droix_shop": 0,
    "droix_shop_skipped": 0,
    "errors": [],
}


# ── Helpers ───────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def clean_title(text: str) -> str:
    return html.unescape(text).strip()


def parse_date(date_str: str) -> str:
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
    """Strip scripts, styles, review widgets, and images. Convert iframes to links."""
    for tag in soup_el(["style", "script", "noscript"]):
        tag.decompose()
    for tag in soup_el.select(".review-wrapper, [class*='wp-review'], [class*='wpr-']"):
        tag.decompose()
    for tag in soup_el.find_all("img"):
        tag.decompose()
    # Convert iframes (YouTube embeds etc.) to plain links so markdownify keeps them
    for tag in soup_el.find_all("iframe"):
        src = tag.get("src", "")
        if src:
            # Normalise embed URLs: youtube.com/embed/ID -> youtu.be/ID
            yt_match = re.search(r"youtube\.com/embed/([^?&]+)", src)
            if yt_match:
                src = f"https://youtu.be/{yt_match.group(1)}"
            tag.replace_with(BeautifulSoup(f'<p><a href="{src}">{src}</a></p>', "html.parser"))
        else:
            tag.decompose()
    return soup_el


def html_to_md(html_str: str) -> str:
    soup = BeautifulSoup(html_str, "html.parser")
    clean_html(soup)
    return md(str(soup), heading_style="ATX").strip()


def save_md(path: Path, frontmatter: dict, body: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, str) and any(c in v for c in [':', '#', '"', "'"]):
            v = json.dumps(v)
        fm_lines.append(f"{k}: {v}")
    fm_lines.append("---")
    path.write_text("\n".join(fm_lines) + "\n\n" + body, encoding="utf-8")


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def get(url: str, **kwargs) -> requests.Response:
    time.sleep(DELAY)
    r = requests.get(url, headers=BROWSER_HEADERS, timeout=30, **kwargs)
    r.raise_for_status()
    return r


# ── 1: gpdstore.net reviews ───────────────────────────────────────────────

def fetch_gpdstore_reviews():
    print("\n[1] gpdstore.net reviews — WP REST API")
    out_dir = INGEST / "blog" / "gpdstore-reviews"
    page = 1
    while True:
        url = (
            f"https://gpdstore.net/wp-json/wp/v2/posts"
            f"?categories=56&per_page=100&page={page}"
            f"&orderby=date&order=desc&_fields=id,title,link,date,content"
        )
        try:
            posts = get(url).json()
        except Exception as e:
            stats["errors"].append(f"gpdstore reviews page {page}: {e}")
            break
        if not posts:
            break
        for p in posts:
            title = clean_title(p["title"]["rendered"])
            date = p["date"][:10]
            slug = f"{date}-{slugify(title)}"
            fm = {
                "title": title,
                "source_url": p["link"],
                "source_site": "gpdstore.net",
                "type": "review-blog",
                "date": date,
                "wp_id": p["id"],
            }
            save_md(out_dir / f"{slug}.md", fm, html_to_md(p["content"]["rendered"]))
            stats["gpdstore_reviews"] += 1
            print(f"  [{stats['gpdstore_reviews']}] {date} {title[:60]}")
        if len(posts) < 100:
            break
        page += 1
    print(f"  → {stats['gpdstore_reviews']} reviews saved")


# ── 2: gpdstore.net KB ───────────────────────────────────────────────────

def fetch_gpdstore_kb():
    print("\n[2] gpdstore.net KB — WP REST API")
    out_dir = INGEST / "kb" / "gpdstore-kb"
    page = 1
    while True:
        url = (
            f"https://gpdstore.net/wp-json/wp/v2/docs"
            f"?per_page=100&page={page}"
            f"&orderby=date&order=desc&_fields=id,title,link,date,content,doc_category"
        )
        try:
            docs = get(url).json()
        except Exception as e:
            stats["errors"].append(f"gpdstore KB page {page}: {e}")
            break
        if not docs:
            break
        for d in docs:
            title = clean_title(d["title"]["rendered"])
            date = d["date"][:10]
            fm = {
                "title": title,
                "source_url": d["link"],
                "source_site": "gpdstore.net",
                "type": "kb-article",
                "date": date,
                "wp_id": d["id"],
            }
            save_md(out_dir / f"{slugify(title)}.md", fm, html_to_md(d["content"]["rendered"]))
            stats["gpdstore_kb"] += 1
            print(f"  [{stats['gpdstore_kb']}] {title[:70]}")
        if len(docs) < 100:
            break
        page += 1
    print(f"  → {stats['gpdstore_kb']} KB articles saved")


# ── 3: gpdstore.net shop ─────────────────────────────────────────────────

def scrape_shop_page(url: str):
    """Scrape a WooCommerce shop listing page, return list of product dicts."""
    soup = BeautifulSoup(get(url).text, "html.parser")
    products = []
    for li in soup.select("li.product"):
        link = li.select_one("a[href*='/product/']")
        title_el = li.select_one(".woocommerce-loop-product__title, h2")
        if not link or not title_el:
            continue
        href = link["href"].split("?")[0].rstrip("/")
        products.append({
            "title": clean_title(title_el.get_text()),
            "href": href,
            "url_slug": href.split("/")[-1],
            "instock": "instock" in li.get("class", []),
        })
    return products


def fetch_product_page(product_url: str, source_site: str, instock: bool) -> tuple:
    """
    Fetch an individual WooCommerce product page and return (frontmatter, body).
    Extracts: title, price, short description, full description tab, specs tab.
    Both gpdstore (cgkit-tab-* IDs) and droix (tab-* IDs) are handled.
    """
    soup = BeautifulSoup(get(product_url).text, "html.parser")
    clean_html(soup)

    # Title
    h1 = soup.select_one("h1.product_title, h1.entry-title, h1")
    title = clean_title(h1.get_text()) if h1 else product_url.rstrip("/").split("/")[-1]

    # Price
    price_el = soup.select_one(".summary .price, .price")
    price = re.sub(r"\s+", " ", price_el.get_text(strip=True))[:80] if price_el else ""

    # Short description
    short_desc_el = soup.select_one(
        ".woocommerce-product-details__short-description, "
        ".summary .short-description, .summary .product-short-description"
    )
    short_desc = html_to_md(str(short_desc_el)) if short_desc_el else ""

    # Full description tab — gpdstore uses cgkit-tab-* IDs, droix uses tab-*
    full_desc_el = soup.select_one(
        "[id*='tab-description'], [id*='tab_description'], "
        ".woocommerce-Tabs-panel--description, .commercekit-Tabs-panel--description"
    )
    full_desc = html_to_md(str(full_desc_el)) if full_desc_el else ""

    # Specs / additional info tab
    specs_el = soup.select_one(
        "[id*='tab-additional_information'], [id*='tab_additional'], "
        ".woocommerce-Tabs-panel--additional_information, "
        ".commercekit-Tabs-panel--additional_information"
    )
    specs = html_to_md(str(specs_el)) if specs_el else ""

    # Fallback: grab the whole .woocommerce-tabs panel set
    if not short_desc and not full_desc and not specs:
        tabs = soup.select(".woocommerce-tabs .panel")
        if tabs:
            full_desc = "\n\n".join(html_to_md(str(t)) for t in tabs[:2])
        else:
            product_div = soup.select_one("div.product, .product-details-wrapper, main")
            if product_div:
                full_desc = html_to_md(str(product_div))

    # Build body — skip tab content that is just nav links (< 150 chars)
    sections = []
    if short_desc:
        sections.append(short_desc)
    if full_desc and len(full_desc) > 150 and full_desc != short_desc:
        sections.append(full_desc)
    if specs and len(specs) > 150:
        sections.append("## Specifications\n\n" + specs)
    body = "\n\n".join(sections).strip()

    fm = {
        "title": title,
        "source_url": product_url,
        "source_site": source_site,
        "type": "product-page",
        "instock": str(instock).lower(),
        "price": price,
    }
    return fm, body


def fetch_gpdstore_shop():
    print("\n[3] gpdstore.net shop — HTML scrape (pages 1-6)")
    out_dir = INGEST / "product" / "gpdstore-shop"
    all_products = []
    for page in range(1, 7):
        url = f"https://gpdstore.net/shop/page/{page}/" if page > 1 else "https://gpdstore.net/shop/"
        try:
            products = scrape_shop_page(url)
        except Exception as e:
            stats["errors"].append(f"gpdstore shop page {page}: {e}")
            break
        if not products:
            print(f"  page {page}: no products (stopping)")
            break
        all_products.extend(products)
        print(f"  page {page}: {len(products)} products (total {len(all_products)})")

    # Fetch individual product pages and save as MD
    for p in all_products:
        try:
            fm, body = fetch_product_page(p["href"], "gpdstore.net", p["instock"])
            save_md(out_dir / f"{p['url_slug']}.md", fm, body)
            stats["gpdstore_shop"] += 1
            print(f"  [{stats['gpdstore_shop']}] {fm['title'][:70]}")
        except Exception as e:
            stats["errors"].append(f"gpdstore product page {p['href']}: {e}")
            print(f"  ERROR {p['href']}: {e}")

    print(f"  → {stats['gpdstore_shop']} product pages saved")
    return all_products


# ── 4: droix.net KB ──────────────────────────────────────────────────────

def fetch_droix_kb(gpdstore_kb_slugs: set):
    """
    Fetch droix KB articles. Skip any that are GPD-product articles already
    covered by gpdstore KB (matched by normalised title slug).
    Non-GPD articles (AYANEO, AYN, Anbernic, ONEXPLAYER, Retroid, etc.) are kept.
    """
    print("\n[4] droix.net KB — WP REST API (paginated, skipping GPD dupes)")
    out_dir = INGEST / "kb" / "droix-kb"
    page = 1
    while True:
        url = (
            f"https://droix.net/knowledge-base/wp-json/wp/v2/kb"
            f"?per_page=100&page={page}"
            f"&orderby=date&order=desc&_fields=id,title,link,date,content"
        )
        try:
            articles = get(url).json()
        except Exception as e:
            stats["errors"].append(f"droix KB page {page}: {e}")
            break
        if not articles:
            break
        for a in articles:
            title = clean_title(a["title"]["rendered"])
            title_slug = slugify(title)
            # Skip if this title slug already exists in gpdstore KB
            if title_slug in gpdstore_kb_slugs:
                stats["droix_kb_skipped"] += 1
                print(f"  SKIP (dupe) {title[:60]}")
                continue
            date = a["date"][:10]
            fm = {
                "title": title,
                "source_url": a["link"],
                "source_site": "droix.net",
                "type": "kb-article",
                "date": date,
                "wp_id": a["id"],
            }
            save_md(out_dir / f"{slugify(title)}.md", fm, html_to_md(a["content"]["rendered"]))
            stats["droix_kb"] += 1
            print(f"  [{stats['droix_kb']}] {title[:70]}")
        if len(articles) < 100:
            break
        page += 1
    print(f"  → {stats['droix_kb']} saved, {stats['droix_kb_skipped']} skipped (GPD dupes)")


# ── 5: droix.net reviews ─────────────────────────────────────────────────

def scrape_droix_listing_page(url: str):
    """Return list of {url, title, date} from a droix review listing page."""
    soup = BeautifulSoup(get(url).text, "html.parser")
    items = []
    for card in soup.select(".content-inner .p-wrap"):
        link_el = card.select_one("a.p-flink")
        title_el = card.select_one("a.p-url")
        date_el = card.select_one("abbr.date.published")
        if not link_el:
            continue
        items.append({
            "url": link_el["href"],
            "title": clean_title(title_el.get_text()) if title_el else "",
            "date": parse_date(date_el.get_text(strip=True) if date_el else None),
        })
    return items


def fetch_droix_article(article_url: str, listing_title: str, listing_date: str) -> tuple:
    """Fetch and parse a single droix blog article. Returns (title, body)."""
    soup = BeautifulSoup(get(article_url).text, "html.parser")
    h1 = soup.select_one("h1")
    title = clean_title(h1.get_text()) if h1 else listing_title
    body_el = soup.select_one("article .entry-content") or soup.select_one("article")
    body = html_to_md(str(body_el)) if body_el else ""
    return title, body


def fetch_droix_reviews():
    print("\n[5] droix.net reviews — HTML scrape (listing pages 1-11)")
    out_dir = INGEST / "blog" / "droix-reviews"
    base_url = "https://droix.net/blogs/category/reviews"

    for page in range(1, 12):
        listing_url = f"{base_url}/" if page == 1 else f"{base_url}/page/{page}/"
        print(f"\n  Listing page {page}: {listing_url}")
        try:
            items = scrape_droix_listing_page(listing_url)
        except Exception as e:
            stats["errors"].append(f"droix reviews listing page {page}: {e}")
            continue
        if not items:
            print(f"  No items found on page {page}, stopping.")
            break

        for item in items:
            try:
                title, body = fetch_droix_article(item["url"], item["title"], item["date"])
            except Exception as e:
                stats["errors"].append(f"droix review article {item['url']}: {e}")
                print(f"  ERROR fetching {item['url']}: {e}")
                continue

            slug = f"{item['date']}-{slugify(title)}"
            fm = {
                "title": title,
                "source_url": item["url"],
                "source_site": "droix.net",
                "type": "review-blog",
                "date": item["date"],
            }
            save_md(out_dir / f"{slug}.md", fm, body)
            stats["droix_reviews"] += 1
            print(f"  [{stats['droix_reviews']}] {item['date']} {title[:55]}")

    print(f"\n  → {stats['droix_reviews']} reviews saved")


# ── 6: droix.net shop ────────────────────────────────────────────────────

def fetch_droix_shop(gpdstore_products: list):
    """
    Scrape droix shop pages 1-16. Skip:
    - Any product whose URL slug starts with 'gpd-' (gpdstore covers all GPD)
    - Any product already in gpdstore_products (by URL slug or normalised title)
    """
    print("\n[6] droix.net shop — HTML scrape (pages 1-16, deduplicating GPD)")
    gpd_slugs = {p["url_slug"] for p in gpdstore_products}
    gpd_titles = {slugify(p["title"]) for p in gpdstore_products}

    all_droix = []
    for page in range(1, 17):
        url = "https://droix.net/shop/" if page == 1 else f"https://droix.net/shop/page/{page}/"
        try:
            products = scrape_shop_page(url)
        except Exception as e:
            stats["errors"].append(f"droix shop page {page}: {e}")
            continue
        if not products:
            print(f"  page {page}: no products (stopping)")
            break

        kept, skipped = [], []
        for p in products:
            url_slug = p["url_slug"]
            # Skip GPD products: URL slug starts with 'gpd-' OR matches gpdstore set
            if url_slug.startswith("gpd-") or url_slug in gpd_slugs or slugify(p["title"]) in gpd_titles:
                skipped.append(p["title"])
                stats["droix_shop_skipped"] += 1
            else:
                kept.append(p)
                all_droix.append(p)
                stats["droix_shop"] += 1

        print(f"  page {page}: kept {len(kept)}, skipped {len(skipped)} — cumulative {stats['droix_shop']}")

    # Fetch individual product pages and save as MD
    out_dir = INGEST / "product" / "droix-shop"
    for p in all_droix:
        try:
            fm, body = fetch_product_page(p["href"], "droix.net", p["instock"])
            save_md(out_dir / f"{p['url_slug']}.md", fm, body)
            print(f"  [{stats['droix_shop']}] {fm['title'][:70]}")
        except Exception as e:
            stats["errors"].append(f"droix product page {p['href']}: {e}")
            print(f"  ERROR {p['href']}: {e}")

    print(f"  → {stats['droix_shop']} droix product pages saved, {stats['droix_shop_skipped']} skipped")


# ── 7: MANIFEST ──────────────────────────────────────────────────────────

def write_manifest():
    print("\n[7] Writing MANIFEST.md")
    lines = [
        "# Raw Ingest Manifest",
        "",
        f"**Fetched:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Counts",
        "",
        f"| Source | Type | Count |",
        f"|--------|------|-------|",
        f"| gpdstore.net | Reviews | {stats['gpdstore_reviews']} |",
        f"| gpdstore.net | KB articles | {stats['gpdstore_kb']} |",
        f"| gpdstore.net | Shop products | {stats['gpdstore_shop']} |",
        f"| droix.net | KB articles | {stats['droix_kb']} |",
        f"| droix.net | KB skipped (GPD dupes) | {stats['droix_kb_skipped']} |",
        f"| droix.net | Reviews | {stats['droix_reviews']} |",
        f"| droix.net | Shop products | {stats['droix_shop']} |",
        f"| droix.net | Shop skipped (GPD dupes) | {stats['droix_shop_skipped']} |",
        "",
        "## Deduplication Rules",
        "",
        "- gpdstore.net is fetched first and takes priority for all GPD content.",
        "- droix.net KB: articles skipped if normalised title matches a gpdstore KB article.",
        "- droix.net shop: products skipped if URL slug starts with `gpd-` or matches gpdstore product.",
        "",
    ]
    if stats["errors"]:
        lines += ["## Errors", ""]
        for e in stats["errors"]:
            lines.append(f"- {e}")
        lines.append("")
    else:
        lines += ["## Errors", "", "None.", ""]

    path = INGEST / "MANIFEST.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Saved: raw/ingest/MANIFEST.md")


# ── Main ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    start = datetime.now()
    print(f"Phase 2: Full fetch — {start.strftime('%Y-%m-%d %H:%M')}")

    fetch_gpdstore_reviews()
    fetch_gpdstore_kb()

    # Collect gpdstore KB slugs for droix dedup
    gpdstore_kb_slugs = {
        f.stem for f in (INGEST / "kb" / "gpdstore-kb").glob("*.md")
    }

    gpdstore_products = fetch_gpdstore_shop()

    fetch_droix_kb(gpdstore_kb_slugs)
    fetch_droix_reviews()
    fetch_droix_shop(gpdstore_products)

    write_manifest()

    elapsed = (datetime.now() - start).seconds
    print(f"\nDone in {elapsed//60}m {elapsed%60}s.")
    print(f"Total files: {stats['gpdstore_reviews'] + stats['gpdstore_kb'] + stats['droix_kb'] + stats['droix_reviews']} articles + {stats['gpdstore_shop'] + stats['droix_shop']} product entries")

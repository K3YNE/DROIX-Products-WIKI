#!/usr/bin/env python3
"""
Reprocess KB articles/guides in wiki/sources/ to fetch full content including images.
"""

import os
import sys
import glob
import re
import time
import argparse
import urllib.parse
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}
DELAY = 0.5  # delay in seconds between requests to prevent rate limiting

def fix_droix_casing(text: str) -> str:
    """Replace DroiX/Droix/droix with DROIX unless part of a URL/domain/email."""
    pattern = r"(?<![/.@])\b[Dd]roi[Xx]\b(?!\.(?:net|co\.uk))"
    return re.sub(pattern, "DROIX", text)

def clean_html(soup_el):
    """Strip styles, scripts, review widgets, and unwrap images from parent link tags. Convert iframes to clean links."""
    for tag in soup_el(["style", "script", "noscript"]):
        tag.decompose()
    for tag in soup_el.select(".review-wrapper, [class*='wp-review'], [class*='wpr-']"):
        tag.decompose()
        
    # Process images: unwrap from <a> tags and map lazy loaded attributes to src
    for img in soup_el.find_all("img"):
        # Map lazy load or data sources if src is a placeholder data URI or missing
        src = img.get("src", "")
        if src.startswith("data:") or not src:
            for attr in ["data-lazy-src", "data-src", "data-original"]:
                val = img.get(attr)
                if val and not val.startswith("data:"):
                    img["src"] = val
                    break
        
        # Unwrap img from wrapping <a> tag for cleaner markdownify output
        parent = img.parent
        if parent and parent.name == "a":
            parent.replace_with(img)

    # Convert iframes (YouTube embeds etc.) to plain links so markdownify keeps them
    for tag in soup_el.find_all("iframe"):
        src = tag.get("src", "")
        if src:
            # Normalise embed URLs: youtube.com/embed/ID -> youtu.be/ID
            yt_match = re.search(r"youtube\.com/embed/([^?&\"'>]+)", src)
            if yt_match:
                src = f"https://youtu.be/{yt_match.group(1)}"
            tag.replace_with(BeautifulSoup(f'<p><a href="{src}">{src}</a></p>', "html.parser"))
        else:
            tag.decompose()
            
    return soup_el

def process_file(file_path: str, dry_run: bool = False) -> bool:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Parse frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not fm_match:
        print(f"Skipping {os.path.basename(file_path)}: No frontmatter found.")
        return False
        
    fm_text, existing_body = fm_match.groups()
    
    # Check if this is a kb-article or kb-faq
    if "subtype: kb-article" not in fm_text and "subtype: kb-faq" not in fm_text:
        return False
        
    # Extract source_url
    url_match = re.search(r"source_url:\s*\"?([^\n\"]+)\"?", fm_text)
    if not url_match:
        print(f"Skipping {os.path.basename(file_path)}: No source_url found in frontmatter.")
        return False
        
    source_url = url_match.group(1).strip()
    parsed_url = urllib.parse.urlparse(source_url)
    
    # Determine WP REST API endpoint and post slug
    path = parsed_url.path.rstrip("/")
    slug = path.split("/")[-1] if path else ""
    if not slug:
        print(f"Skipping {os.path.basename(file_path)}: Could not parse slug from URL '{source_url}'.")
        return False
        
    if "droix.net" in parsed_url.netloc:
        api_url = f"https://droix.net/knowledge-base/wp-json/wp/v2/kb?slug={slug}"
    elif "gpdstore.net" in parsed_url.netloc:
        api_url = f"https://gpdstore.net/wp-json/wp/v2/docs?slug={slug}"
    else:
        # Ignore other sites like onexplayerstore.com
        return False
        
    print(f"Fetching {os.path.basename(file_path)} from: {api_url}")
    
    try:
        time.sleep(DELAY)
        response = requests.get(api_url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        posts = response.json()
    except Exception as e:
        print(f"  Error fetching {os.path.basename(file_path)}: {e}")
        return False
        
    if not posts:
        print(f"  Error: No post found for slug '{slug}' in REST API.")
        return False
        
    post = posts[0]
    html_body = post.get("content", {}).get("rendered", "")
    if not html_body:
        print(f"  Error: Post found but has empty content.")
        return False
        
    # Convert HTML to Markdown
    soup = BeautifulSoup(html_body, "html.parser")
    clean_html(soup)
    new_markdown_body = md(str(soup), heading_style="ATX").strip()
    
    # Apply DROIX casing fix to body
    new_markdown_body = fix_droix_casing(new_markdown_body)
    
    # Check if the body actually changed or has images now
    image_count = len(re.findall(r"!\[.*?\]\(.*?\)", new_markdown_body))
    print(f"  Fetched successfully. Length: {len(new_markdown_body)} chars. Images found: {image_count}.")
    
    # Construct updated file content
    updated_content = f"---\n{fm_text}\n---\n\n{new_markdown_body}\n"
    
    if dry_run:
        print(f"  [DRY-RUN] Would update {os.path.basename(file_path)}.")
        return True
        
    # Overwrite the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"  Updated: {os.path.basename(file_path)}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Reprocess KB articles/guides to fetch full content including images.")
    parser.add_argument("--file", help="Path to a single markdown file to reprocess.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without overwriting files.")
    args = parser.parse_args()
    
    wiki_dir = "/Users/eugene/Projects/llm-wiki-yt-droix/wiki/sources"
    
    if args.file:
        file_path = os.path.abspath(args.file)
        if not os.path.exists(file_path):
            print(f"File not found: {args.file}")
            sys.exit(1)
        process_file(file_path, dry_run=args.dry_run)
    else:
        files = glob.glob(os.path.join(wiki_dir, "*.md"))
        success_count = 0
        total_processed = 0
        
        for idx, file_path in enumerate(files, 1):
            # Only process markdown files
            if not os.path.isfile(file_path):
                continue
            res = process_file(file_path, dry_run=args.dry_run)
            if res:
                success_count += 1
            total_processed += 1
            
        print(f"\nDone! Processed {total_processed} files. Successfully updated: {success_count}.")

if __name__ == "__main__":
    main()

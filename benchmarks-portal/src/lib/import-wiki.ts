import fs from "node:fs";
import path from "node:path";
import YAML from "yaml";
import { getDb } from "./db";
import { slugify } from "./normalize";
import { wikiProductsDir } from "./paths";

type Frontmatter = Record<string, unknown>;

function readFrontmatter(file: string): Frontmatter | null {
  const text = fs.readFileSync(file, "utf8");
  const match = text.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;
  return YAML.parse(match[1]) as Frontmatter;
}

function text(value: unknown) {
  if (value === null || value === undefined) return null;
  if (Array.isArray(value)) return value.join(", ");
  return String(value);
}

export function importWikiProducts(dir = wikiProductsDir()) {
  const database = getDb();
  const files = fs.existsSync(dir)
    ? fs.readdirSync(dir).filter((file) => file.endsWith(".md")).sort()
    : [];

  const upsert = database.prepare(`
    INSERT INTO products (
      slug, title, type, brand, parent_slug, form_factor, platform, apu, gpu, wiki_path, source, needs_review, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'wiki', 0, CURRENT_TIMESTAMP)
    ON CONFLICT(slug) DO UPDATE SET
      title = excluded.title,
      type = excluded.type,
      brand = excluded.brand,
      parent_slug = excluded.parent_slug,
      form_factor = excluded.form_factor,
      platform = excluded.platform,
      apu = excluded.apu,
      gpu = excluded.gpu,
      wiki_path = excluded.wiki_path,
      source = CASE WHEN products.source = 'bench_only' THEN 'wiki' ELSE products.source END,
      needs_review = 0,
      updated_at = CURRENT_TIMESTAMP
  `);

  const insertAlias = database.prepare(`
    INSERT INTO product_aliases (raw_label, normalized_label, product_id, confidence, status, notes, updated_at)
    VALUES (?, ?, (SELECT id FROM products WHERE slug = ?), 1, 'approved', 'Imported from wiki product title', CURRENT_TIMESTAMP)
    ON CONFLICT(raw_label) DO UPDATE SET
      product_id = excluded.product_id,
      confidence = 1,
      status = 'approved',
      updated_at = CURRENT_TIMESTAMP
  `);

  let count = 0;
  for (const file of files) {
    const fullPath = path.join(dir, file);
    const frontmatter = readFrontmatter(fullPath);
    if (!frontmatter) continue;
    const title = text(frontmatter.title) ?? path.basename(file, ".md");
    const slug = text(frontmatter.slug) ?? slugify(title);
    upsert.run(
      slug,
      title,
      text(frontmatter.type) ?? "product",
      text(frontmatter.brand),
      text(frontmatter.parent_product),
      text(frontmatter.form_factor),
      text(frontmatter.platform),
      text(frontmatter.apu) ?? text(frontmatter.soc),
      text(frontmatter.gpu),
      path.relative(process.cwd(), fullPath)
    );
    insertAlias.run(title, title, slug);
    count += 1;
  }

  return { files: files.length, imported: count, dir };
}

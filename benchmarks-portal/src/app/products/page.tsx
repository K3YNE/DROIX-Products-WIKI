import Link from "next/link";
import { rows } from "@/lib/db";

export const dynamic = "force-dynamic";

type Product = {
  id: number;
  slug: string;
  title: string;
  brand: string | null;
  type: string;
  platform: string | null;
  source: string;
  needs_review: number;
  run_count: number;
  result_count: number;
};

export default function ProductsPage({ searchParams }: { searchParams: Promise<{ q?: string; status?: string }> }) {
  return <ProductsContent searchParams={searchParams} />;
}

async function ProductsContent({ searchParams }: { searchParams: Promise<{ q?: string; status?: string }> }) {
  const params = await searchParams;
  const q = `%${params.q ?? ""}%`;
  const filters = ["(p.title LIKE ? OR p.slug LIKE ? OR COALESCE(p.brand, '') LIKE ?)"];
  const values: unknown[] = [q, q, q];
  if (params.status === "needs_review") filters.push("p.needs_review = 1");
  const products = rows<Product>(
    `SELECT p.*,
      COUNT(DISTINCT r.id) AS run_count,
      COUNT(br.id) AS result_count
     FROM products p
     LEFT JOIN benchmark_runs r ON r.product_id = p.id
     LEFT JOIN benchmark_results br ON br.run_id = r.id
     WHERE ${filters.join(" AND ")}
     GROUP BY p.id
     ORDER BY p.needs_review DESC, p.brand, p.title`,
    values
  );

  return (
    <>
      <div className="page-header">
        <div>
          <h1>Products</h1>
          <p className="muted">Canonical products, variants, and benchmark-only imported labels.</p>
        </div>
      </div>

      <form className="toolbar">
        <input name="q" placeholder="Search products" defaultValue={params.q ?? ""} />
        <select name="status" defaultValue={params.status ?? ""}>
          <option value="">All statuses</option>
          <option value="needs_review">Needs review</option>
        </select>
        <button type="submit">Filter</button>
        <Link className="button secondary" href="/products">
          Reset
        </Link>
      </form>

      <div className="product-list">
        {products.map((product) => (
          <Link className="product-card" key={product.id} href={`/products/${product.id}`}>
            <h3>{product.title}</h3>
            <div>
              {product.needs_review ? <span className="pill warn">needs review</span> : <span className="pill good">mapped</span>}
              <span className="pill">{product.type}</span>
              {product.brand ? <span className="pill">{product.brand}</span> : null}
              {product.platform ? <span className="pill">{product.platform}</span> : null}
            </div>
            <p className="muted">
              {product.run_count} runs, {product.result_count} results
            </p>
          </Link>
        ))}
      </div>
    </>
  );
}

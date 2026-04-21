import Link from "next/link";
import { rows } from "@/lib/db";

export const dynamic = "force-dynamic";

type Product = { id: number; title: string; brand: string | null; run_count: number };
type Metric = { key: string; display_name: string; result_count: number };
type Comparison = {
  product_id: number;
  product_title: string;
  sheet_name: string;
  source_row: number;
  tested_on: string | null;
  source_hidden: number;
  display_name: string;
  value_numeric: number | null;
  value_text: string | null;
  unit: string | null;
  resolution: string | null;
  tdp_watts: number | null;
};

export default async function ComparePage({
  searchParams
}: {
  searchParams: Promise<{ products?: string; metric?: string; hidden?: string }>;
}) {
  const params = await searchParams;
  const selected = (params.products ?? "")
    .split(",")
    .map((id) => Number(id))
    .filter(Boolean);
  const products = rows<Product>(
    `SELECT p.id, p.title, p.brand, COUNT(r.id) AS run_count
     FROM products p
     JOIN benchmark_runs r ON r.product_id = p.id
     GROUP BY p.id
     ORDER BY p.brand, p.title`
  );
  const metrics = rows<Metric>(
    `SELECT bd.key, bd.display_name, COUNT(br.id) AS result_count
     FROM benchmark_definitions bd
     JOIN benchmark_results br ON br.definition_id = bd.id
     WHERE bd.enabled = 1
     GROUP BY bd.id
     ORDER BY bd.group_name, bd.display_name`
  );

  let comparisons: Comparison[] = [];
  if (selected.length) {
    const placeholders = selected.map(() => "?").join(",");
    const filters = [`p.id IN (${placeholders})`, "bd.enabled = 1"];
    const values: unknown[] = [...selected];
    if (params.hidden !== "1") filters.push("r.source_hidden = 0");
    if (params.metric) {
      filters.push("bd.key = ?");
      values.push(params.metric);
    }
    comparisons = rows<Comparison>(
      `SELECT p.id AS product_id, p.title AS product_title,
        r.sheet_name, r.source_row, r.tested_on, r.source_hidden,
        bd.display_name, br.value_numeric, br.value_text, br.unit, br.resolution, br.tdp_watts
       FROM benchmark_results br
       JOIN benchmark_runs r ON r.id = br.run_id
       JOIN products p ON p.id = r.product_id
       JOIN benchmark_definitions bd ON bd.id = br.definition_id
       WHERE ${filters.join(" AND ")}
       ORDER BY bd.display_name, br.tdp_watts, p.title, r.tested_on DESC`,
      values
    );
  }

  return (
    <>
      <div className="page-header">
        <div>
          <h1>Compare Products</h1>
          <p className="muted">Select products and optionally narrow to one benchmark metric.</p>
        </div>
      </div>

      <div className="compare-grid">
        <form className="panel">
          <h2 style={{ marginTop: 0 }}>Products</h2>
          <div className="checkbox-list">
            {products.map((product) => (
              <label key={product.id}>
                <input
                  type="checkbox"
                  name="product"
                  value={product.id}
                  defaultChecked={selected.includes(product.id)}
                />
                <span>
                  {product.title}
                  <br />
                  <span className="muted">{product.run_count} runs</span>
                </span>
              </label>
            ))}
          </div>
          <h2>Metric</h2>
          <select name="metric" defaultValue={params.metric ?? ""}>
            <option value="">All enabled metrics</option>
            {metrics.map((metric) => (
              <option key={metric.key} value={metric.key}>
                {metric.display_name} ({metric.result_count})
              </option>
            ))}
          </select>
          <label className="toolbar" style={{ marginTop: 12 }}>
            <input type="checkbox" name="hidden" value="1" defaultChecked={params.hidden === "1"} />
            Include hidden Excel rows
          </label>
          <button
            formAction={async (formData) => {
              "use server";
              const chosen = formData.getAll("product").join(",");
              const metric = String(formData.get("metric") ?? "");
              const hidden = formData.get("hidden") ? "&hidden=1" : "";
              const target = `/compare?products=${chosen}${metric ? `&metric=${metric}` : ""}${hidden}`;
              const { redirect } = await import("next/navigation");
              redirect(target);
            }}
            type="submit"
          >
            Update Comparison
          </button>
        </form>

        <div className="panel">
          <table>
            <thead>
              <tr>
                <th>Product</th>
                <th>Benchmark</th>
                <th>Value</th>
                <th>Resolution</th>
                <th>TDP</th>
                <th>Source</th>
              </tr>
            </thead>
            <tbody>
              {comparisons.map((item, index) => (
                <tr key={`${item.product_id}-${item.display_name}-${item.source_row}-${index}`}>
                  <td>
                    <Link href={`/products/${item.product_id}`}>{item.product_title}</Link>
                    {item.source_hidden ? <span className="pill warn">hidden</span> : null}
                  </td>
                  <td>{item.display_name}</td>
                  <td>{item.value_numeric ?? item.value_text}</td>
                  <td>{item.resolution}</td>
                  <td>{item.tdp_watts ? `${item.tdp_watts}W` : ""}</td>
                  <td>
                    {item.sheet_name} row {item.source_row}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

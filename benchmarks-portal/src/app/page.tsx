import Link from "next/link";
import { row, rows } from "@/lib/db";

export const dynamic = "force-dynamic";

export default function HomePage() {
  const stats = row<{
    products: number;
    aliases: number;
    runs: number;
    results: number;
    warnings: number;
  }>(`
    SELECT
      (SELECT COUNT(*) FROM products) AS products,
      (SELECT COUNT(*) FROM product_aliases WHERE status = 'needs_review') AS aliases,
      (SELECT COUNT(*) FROM benchmark_runs) AS runs,
      (SELECT COUNT(*) FROM benchmark_results) AS results,
      (SELECT COUNT(*) FROM import_warnings) AS warnings
  `);
  const batches = rows<{
    source_type: string;
    source_path: string;
    completed_at: string;
    row_count: number;
    result_count: number;
  }>("SELECT * FROM import_batches ORDER BY started_at DESC LIMIT 5");

  return (
    <>
      <div className="page-header">
        <div>
          <h1>Benchmark Portal</h1>
          <p className="muted">Import, maintain, and compare product performance data.</p>
        </div>
        <Link className="button" href="/compare">
          Compare Products
        </Link>
      </div>

      <section className="grid stats">
        <div className="stat">
          <strong>{stats?.products ?? 0}</strong>
          <span>Products</span>
        </div>
        <div className="stat">
          <strong>{stats?.runs ?? 0}</strong>
          <span>Benchmark runs</span>
        </div>
        <div className="stat">
          <strong>{stats?.results ?? 0}</strong>
          <span>Results</span>
        </div>
        <div className="stat">
          <strong>{stats?.aliases ?? 0}</strong>
          <span>Aliases needing review</span>
        </div>
        <div className="stat">
          <strong>{stats?.warnings ?? 0}</strong>
          <span>Import warnings</span>
        </div>
      </section>

      <h2>Recent Imports</h2>
      <div className="panel">
        <table>
          <thead>
            <tr>
              <th>Type</th>
              <th>Source</th>
              <th>Completed</th>
              <th>Rows</th>
              <th>Results</th>
            </tr>
          </thead>
          <tbody>
            {batches.map((batch) => (
              <tr key={`${batch.source_type}-${batch.completed_at}`}>
                <td>{batch.source_type}</td>
                <td>{batch.source_path}</td>
                <td>{batch.completed_at}</td>
                <td>{batch.row_count}</td>
                <td>{batch.result_count}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

import Link from "next/link";
import { notFound } from "next/navigation";
import { row, rows } from "@/lib/db";

export const dynamic = "force-dynamic";

type Product = {
  id: number;
  slug: string;
  title: string;
  type: string;
  brand: string | null;
  platform: string | null;
  apu: string | null;
  gpu: string | null;
  wiki_path: string | null;
  needs_review: number;
};

type Run = {
  id: number;
  sheet_name: string;
  source_row: number;
  source_hidden: number;
  tested_on: string | null;
  notes: string | null;
  row_tdp_watts: string | null;
  connection_type: string | null;
  display_mode: string | null;
  egpu_title: string | null;
};

type Result = {
  id: number;
  run_id: number;
  display_name: string;
  value_numeric: number | null;
  value_text: string | null;
  unit: string | null;
  resolution: string | null;
  tdp_watts: number | null;
  source_cell: string;
};

export default async function ProductDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const product = row<Product>("SELECT * FROM products WHERE id = ? OR slug = ?", [id, id]);
  if (!product) notFound();
  const runs = rows<Run>(
    `SELECT r.*, p.title AS egpu_title
     FROM benchmark_runs r
     LEFT JOIN products p ON p.id = r.egpu_product_id
     WHERE r.product_id = ?
     ORDER BY r.tested_on DESC, r.sheet_name, r.source_row`,
    [product.id]
  );
  const results = rows<Result>(
    `SELECT br.*, bd.display_name
     FROM benchmark_results br
     JOIN benchmark_runs r ON r.id = br.run_id
     JOIN benchmark_definitions bd ON bd.id = br.definition_id
     WHERE r.product_id = ?
     ORDER BY bd.group_name, bd.display_name, br.tdp_watts`,
    [product.id]
  );

  return (
    <>
      <div className="page-header">
        <div>
          <h1>{product.title}</h1>
          <p className="muted">{product.slug}</p>
        </div>
        <Link className="button secondary" href={`/compare?products=${product.id}`}>
          Compare
        </Link>
      </div>

      <div className="panel">
        <span className={product.needs_review ? "pill warn" : "pill good"}>
          {product.needs_review ? "needs review" : "mapped"}
        </span>
        <span className="pill">{product.type}</span>
        {product.brand ? <span className="pill">{product.brand}</span> : null}
        {product.platform ? <span className="pill">{product.platform}</span> : null}
        {product.apu ? <span className="pill">{product.apu}</span> : null}
        {product.gpu ? <span className="pill">{product.gpu}</span> : null}
        {product.wiki_path ? <p className="muted">Wiki source: {product.wiki_path}</p> : null}
      </div>

      <h2>Runs</h2>
      <div className="panel">
        <table>
          <thead>
            <tr>
              <th>Sheet</th>
              <th>Row</th>
              <th>Date</th>
              <th>Context</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            {runs.map((run) => (
              <tr key={run.id}>
                <td>{run.sheet_name}</td>
                <td>{run.source_row}</td>
                <td>{run.tested_on ?? ""}</td>
                <td>
                  {run.source_hidden ? <span className="pill warn">hidden source row</span> : null}
                  {run.row_tdp_watts ? <span className="pill">{run.row_tdp_watts}W context</span> : null}
                  {run.connection_type ? <span className="pill">{run.connection_type}</span> : null}
                  {run.display_mode ? <span className="pill">{run.display_mode}</span> : null}
                  {run.egpu_title ? <span className="pill">{run.egpu_title}</span> : null}
                </td>
                <td>{run.notes}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <h2>Results</h2>
      <div className="panel">
        <table>
          <thead>
            <tr>
              <th>Benchmark</th>
              <th>Value</th>
              <th>Unit</th>
              <th>Resolution</th>
              <th>TDP</th>
              <th>Run</th>
              <th>Cell</th>
            </tr>
          </thead>
          <tbody>
            {results.map((result) => (
              <tr key={result.id}>
                <td>{result.display_name}</td>
                <td>{result.value_numeric ?? result.value_text}</td>
                <td>{result.unit}</td>
                <td>{result.resolution}</td>
                <td>{result.tdp_watts ? `${result.tdp_watts}W` : ""}</td>
                <td>{result.run_id}</td>
                <td>{result.source_cell}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

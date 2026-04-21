import { NextResponse } from "next/server";
import { row, rows } from "@/lib/db";

export const runtime = "nodejs";

export async function GET(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const product = row("SELECT * FROM products WHERE id = ? OR slug = ?", [id, id]);
  if (!product) return NextResponse.json({ error: "Not found" }, { status: 404 });
  const productId = (product as { id: number }).id;
  const runs = rows(
    `SELECT r.*, p.title AS egpu_title
     FROM benchmark_runs r
     LEFT JOIN products p ON p.id = r.egpu_product_id
     WHERE r.product_id = ?
     ORDER BY r.tested_on DESC, r.sheet_name, r.source_row`,
    [productId]
  );
  const results = rows(
    `SELECT br.*, bd.group_name, bd.metric_name, bd.display_name, bd.enabled
     FROM benchmark_results br
     JOIN benchmark_runs r ON r.id = br.run_id
     JOIN benchmark_definitions bd ON bd.id = br.definition_id
     WHERE r.product_id = ?
     ORDER BY r.tested_on DESC, bd.group_name, bd.display_name, br.tdp_watts`,
    [productId]
  );
  return NextResponse.json({ product, runs, results });
}

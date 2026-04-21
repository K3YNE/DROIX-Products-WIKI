import { NextResponse } from "next/server";
import { getDb } from "@/lib/db";
import { searchableLabel } from "@/lib/normalize";

export const runtime = "nodejs";

export async function POST(request: Request) {
  const body = await request.json();
  const result = getDb()
    .prepare(
      `INSERT INTO benchmark_runs (
        product_id, raw_model, normalized_model, sheet_name, source_row, tested_on, notes, row_tdp_watts,
        egpu_product_id, connection_type, display_mode
      ) VALUES (?, ?, ?, 'portal', 0, ?, ?, ?, ?, ?, ?)`
    )
    .run(
      body.product_id,
      body.raw_model,
      searchableLabel(body.raw_model ?? ""),
      body.tested_on ?? null,
      body.notes ?? null,
      body.row_tdp_watts ?? null,
      body.egpu_product_id ?? null,
      body.connection_type ?? null,
      body.display_mode ?? null
    );
  return NextResponse.json({ id: Number(result.lastInsertRowid) });
}

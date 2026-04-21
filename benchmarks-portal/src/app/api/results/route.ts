import { NextResponse } from "next/server";
import { getDb } from "@/lib/db";

export const runtime = "nodejs";

export async function POST(request: Request) {
  const body = await request.json();
  const result = getDb()
    .prepare(
      `INSERT INTO benchmark_results (
        run_id, definition_id, value_numeric, value_text, unit, resolution, tdp_watts, tdp_source, source_cell
      ) VALUES (?, ?, ?, ?, ?, ?, ?, 'portal', 'portal')`
    )
    .run(
      body.run_id,
      body.definition_id,
      body.value_numeric ?? null,
      body.value_text ?? null,
      body.unit ?? null,
      body.resolution ?? null,
      body.tdp_watts ?? null
    );
  return NextResponse.json({ id: Number(result.lastInsertRowid) });
}

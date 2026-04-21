import { NextResponse } from "next/server";
import { getDb } from "@/lib/db";

export const runtime = "nodejs";

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const body = await request.json();
  getDb()
    .prepare(
      `UPDATE benchmark_definitions
       SET display_name = COALESCE(?, display_name),
           unit = COALESCE(?, unit),
           higher_is_better = COALESCE(?, higher_is_better),
           enabled = COALESCE(?, enabled),
           updated_at = CURRENT_TIMESTAMP
       WHERE id = ?`
    )
    .run(
      body.display_name ?? null,
      body.unit ?? null,
      body.higher_is_better === undefined ? null : body.higher_is_better ? 1 : 0,
      body.enabled === undefined ? null : body.enabled ? 1 : 0,
      id
    );
  return NextResponse.json({ ok: true });
}

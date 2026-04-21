import { NextResponse } from "next/server";
import { getDb } from "@/lib/db";

export const runtime = "nodejs";

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const body = await request.json();
  getDb()
    .prepare(
      `UPDATE product_aliases
       SET product_id = COALESCE(?, product_id),
           status = COALESCE(?, status),
           notes = COALESCE(?, notes),
           confidence = COALESCE(?, confidence),
           updated_at = CURRENT_TIMESTAMP
       WHERE id = ?`
    )
    .run(body.product_id ?? null, body.status ?? null, body.notes ?? null, body.confidence ?? null, id);
  return NextResponse.json({ ok: true });
}

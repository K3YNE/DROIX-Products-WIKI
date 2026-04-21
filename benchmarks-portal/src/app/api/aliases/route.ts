import { NextResponse } from "next/server";
import { rows } from "@/lib/db";

export const runtime = "nodejs";

export function GET(request: Request) {
  const url = new URL(request.url);
  const status = url.searchParams.get("status");
  const filters = status ? "WHERE a.status = ?" : "";
  return NextResponse.json(
    rows(
      `SELECT a.*, p.title AS product_title, p.slug AS product_slug
       FROM product_aliases a
       LEFT JOIN products p ON p.id = a.product_id
       ${filters}
       ORDER BY a.status = 'needs_review' DESC, a.confidence ASC, a.raw_label`,
      status ? [status] : []
    )
  );
}

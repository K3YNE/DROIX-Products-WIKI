import { NextResponse } from "next/server";
import { rows } from "@/lib/db";

export const runtime = "nodejs";

export function GET(request: Request) {
  const url = new URL(request.url);
  const q = `%${url.searchParams.get("q") ?? ""}%`;
  const status = url.searchParams.get("status");
  const filters: string[] = ["(p.title LIKE ? OR p.slug LIKE ? OR COALESCE(p.brand, '') LIKE ?)"];
  const params: unknown[] = [q, q, q];
  if (status === "needs_review") filters.push("p.needs_review = 1");
  const data = rows(
    `SELECT p.*,
      COUNT(DISTINCT r.id) AS run_count,
      COUNT(br.id) AS result_count
     FROM products p
     LEFT JOIN benchmark_runs r ON r.product_id = p.id
     LEFT JOIN benchmark_results br ON br.run_id = r.id
     WHERE ${filters.join(" AND ")}
     GROUP BY p.id
     ORDER BY p.needs_review DESC, p.brand, p.title`,
    params
  );
  return NextResponse.json(data);
}

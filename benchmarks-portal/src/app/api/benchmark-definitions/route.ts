import { NextResponse } from "next/server";
import { rows } from "@/lib/db";

export const runtime = "nodejs";

export function GET() {
  return NextResponse.json(
    rows(
      `SELECT bd.*, COUNT(br.id) AS result_count
       FROM benchmark_definitions bd
       LEFT JOIN benchmark_results br ON br.definition_id = bd.id
       GROUP BY bd.id
       ORDER BY bd.enabled DESC, bd.group_name, bd.display_name`
    )
  );
}

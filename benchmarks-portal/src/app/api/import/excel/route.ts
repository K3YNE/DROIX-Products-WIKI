import { NextResponse } from "next/server";
import { importExcel } from "@/lib/import-excel";

export const runtime = "nodejs";

export async function POST() {
  return NextResponse.json(await importExcel());
}

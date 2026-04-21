import { NextResponse } from "next/server";
import { importWikiProducts } from "@/lib/import-wiki";

export const runtime = "nodejs";

export function POST() {
  return NextResponse.json(importWikiProducts());
}

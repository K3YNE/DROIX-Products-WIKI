const brandFixes: Array<[RegExp, string]> = [
  [/\bAYA\s+NEO\b/gi, "AYANEO"],
  [/\bONE\s+XPLAYER\b/gi, "ONEXPLAYER"],
  [/\bONE-NETBOOK\b/gi, "ONENETBOOK"],
  [/\bDROIX\b/gi, "DROIX"]
];

export function normalizeLabel(input: string) {
  let value = input.replace(/\n/g, " ").trim();
  for (const [pattern, replacement] of brandFixes) value = value.replace(pattern, replacement);
  value = value.replace(/\s+/g, " ");
  return value;
}

export function searchableLabel(input: string) {
  return normalizeLabel(input)
    .toUpperCase()
    .replace(/RYZEN AI 9 HX/g, "HX")
    .replace(/AMD RYZEN AI MAX\+/g, "AMD MAX+")
    .replace(/AMD RYZEN AI MAX/g, "AMD MAX")
    .replace(/RYZEN AI MAX\+/g, "AMD MAX+")
    .replace(/RYZEN AI MAX/g, "AMD MAX")
    .replace(/RYZEN 7/g, "")
    .replace(/INTEL PROCESSOR/g, "INTEL")
    .replace(/\s*\/\s*\(([^)]*)\)/g, " $1 ")
    .replace(/[()]/g, " ")
    .replace(/\b\d+W\b/g, " ")
    .replace(/[^A-Z0-9+]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

export function slugify(input: string) {
  return normalizeLabel(input)
    .toLowerCase()
    .replace(/\+/g, " plus ")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 120);
}

export function parseTdpTokens(input: string) {
  const matches = input.matchAll(/(?<!\d)(\d{1,3})\s*W\b/gi);
  return [...new Set([...matches].map((match) => Number(match[1])))].sort((a, b) => a - b);
}

export function parseResolution(input: string) {
  const text = input.toUpperCase();
  const direct = text.match(/\b(4K|1440P|1400P|1200P|1080P|800P|720P)\b/);
  if (direct) return direct[1];
  if (text.includes("MAX RES")) return "MAX";
  return null;
}

export function parseDisplayMode(input: string) {
  const text = input.toUpperCase();
  if (text.includes("INTERNAL")) return "internal";
  if (text.includes("EXTERNAL")) return "external";
  return null;
}

export function parseConnectionType(input: string) {
  const text = input.toUpperCase();
  if (text.includes("OCULINK") || text.includes("OCULINK")) return "Oculink";
  if (text.includes("USB4")) return "USB4";
  if (text.includes("USB")) return "USB";
  return null;
}

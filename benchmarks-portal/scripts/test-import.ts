import assert from "node:assert/strict";
import fs from "node:fs";
import { rows, row } from "../src/lib/db";
import { importWikiProducts } from "../src/lib/import-wiki";
import { importExcel } from "../src/lib/import-excel";
import { parseTdpTokens, searchableLabel } from "../src/lib/normalize";

assert.deepEqual(parseTdpTokens("1080P 75W and 28W TDP"), [28, 75]);
try {
  fs.unlinkSync("data/benchmarks.sqlite");
} catch {}

assert.equal(searchableLabel("AYA NEO 2S\n(7840U)"), "AYANEO 2S 7840U");

importWikiProducts();
const result = await importExcel();

assert.equal(result.sheets, 19);
assert.equal(result.rows, 424);

const hidden = row<{ count: number }>(
  "SELECT COUNT(*) AS count FROM benchmark_runs WHERE sheet_name = 'eGPU benchmarks' AND source_hidden = 1"
);
assert.equal(hidden?.count, 5);

const gpd = row<{ count: number }>(
  `SELECT COUNT(*) AS count
   FROM benchmark_runs r
   JOIN products p ON p.id = r.product_id
   WHERE p.slug = 'gpd-win-5-max-395'`
);
assert.ok((gpd?.count ?? 0) > 0);

const tdpResults = rows<{ tdp_watts: number }>(
  `SELECT DISTINCT br.tdp_watts
   FROM benchmark_results br
   JOIN benchmark_runs r ON r.id = br.run_id
   WHERE r.sheet_name = '2026 Windows Gaming Handhelds' AND br.tdp_watts IS NOT NULL
   ORDER BY br.tdp_watts`
).map((item) => item.tdp_watts);
assert.deepEqual(tdpResults, [4, 15, 28, 55, 75]);

console.log("Import tests passed.");

import { importExcel } from "../src/lib/import-excel";

const result = await importExcel();
console.log(JSON.stringify(result, null, 2));

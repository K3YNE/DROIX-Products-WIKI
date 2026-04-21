import { importWikiProducts } from "../src/lib/import-wiki";

const result = importWikiProducts();
console.log(JSON.stringify(result, null, 2));

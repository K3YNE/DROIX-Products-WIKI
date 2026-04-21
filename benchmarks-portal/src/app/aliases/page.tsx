import { revalidatePath } from "next/cache";
import { getDb, rows } from "@/lib/db";

export const dynamic = "force-dynamic";

type Alias = {
  id: number;
  raw_label: string;
  normalized_label: string;
  confidence: number;
  status: string;
  notes: string | null;
  product_id: number | null;
  product_title: string | null;
};

type Product = { id: number; title: string };

async function updateAlias(formData: FormData) {
  "use server";
  const productId = Number(formData.get("product_id"));
  const status = String(formData.get("status") ?? "needs_review");
  getDb()
    .prepare(
      `UPDATE product_aliases
       SET product_id = ?, status = ?, confidence = ?, notes = ?, updated_at = CURRENT_TIMESTAMP
       WHERE id = ?`
    )
    .run(
      Number.isFinite(productId) && productId > 0 ? productId : null,
      status,
      status === "approved" ? 1 : Number(formData.get("confidence") ?? 0),
      String(formData.get("notes") ?? ""),
      Number(formData.get("id"))
    );
  revalidatePath("/aliases");
}

export default function AliasesPage() {
  const aliases = rows<Alias>(
    `SELECT a.*, p.title AS product_title
     FROM product_aliases a
     LEFT JOIN products p ON p.id = a.product_id
     ORDER BY a.status = 'needs_review' DESC, a.confidence ASC, a.raw_label`
  );
  const products = rows<Product>("SELECT id, title FROM products ORDER BY title");

  return (
    <>
      <div className="page-header">
        <div>
          <h1>Alias Review</h1>
          <p className="muted">Approve or correct raw Excel product labels.</p>
        </div>
      </div>

      <div className="panel">
        <table>
          <thead>
            <tr>
              <th>Raw label</th>
              <th>Mapped product</th>
              <th>Status</th>
              <th>Confidence</th>
              <th>Notes</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {aliases.map((alias) => (
              <tr key={alias.id}>
                <td>
                  <strong>{alias.raw_label}</strong>
                  <br />
                  <span className="muted">{alias.normalized_label}</span>
                </td>
                <td>
                  <form id={`alias-${alias.id}`} action={updateAlias}>
                    <input type="hidden" name="id" value={alias.id} />
                    <select name="product_id" defaultValue={alias.product_id ?? ""}>
                      <option value="">No mapping</option>
                      {products.map((product) => (
                        <option key={product.id} value={product.id}>
                          {product.title}
                        </option>
                      ))}
                    </select>
                  </form>
                </td>
                <td>
                  <select form={`alias-${alias.id}`} name="status" defaultValue={alias.status}>
                    <option value="needs_review">needs_review</option>
                    <option value="approved">approved</option>
                    <option value="ignored">ignored</option>
                  </select>
                </td>
                <td>
                  <input
                    form={`alias-${alias.id}`}
                    name="confidence"
                    type="number"
                    step="0.01"
                    min="0"
                    max="1"
                    defaultValue={alias.confidence}
                  />
                </td>
                <td>
                  <input form={`alias-${alias.id}`} name="notes" defaultValue={alias.notes ?? ""} />
                </td>
                <td>
                  <button form={`alias-${alias.id}`} type="submit">
                    Save
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

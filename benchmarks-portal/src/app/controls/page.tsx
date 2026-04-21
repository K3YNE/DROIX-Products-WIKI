import { revalidatePath } from "next/cache";
import { getDb, rows } from "@/lib/db";

export const dynamic = "force-dynamic";

type Definition = {
  id: number;
  group_name: string;
  display_name: string;
  unit: string | null;
  higher_is_better: number;
  enabled: number;
  result_count: number;
};

async function updateDefinition(formData: FormData) {
  "use server";
  getDb()
    .prepare(
      `UPDATE benchmark_definitions
       SET display_name = ?, unit = ?, higher_is_better = ?, enabled = ?, updated_at = CURRENT_TIMESTAMP
       WHERE id = ?`
    )
    .run(
      String(formData.get("display_name") ?? ""),
      String(formData.get("unit") ?? ""),
      formData.get("higher_is_better") ? 1 : 0,
      formData.get("enabled") ? 1 : 0,
      Number(formData.get("id"))
    );
  revalidatePath("/controls");
}

export default function ControlsPage() {
  const definitions = rows<Definition>(
    `SELECT bd.*, COUNT(br.id) AS result_count
     FROM benchmark_definitions bd
     LEFT JOIN benchmark_results br ON br.definition_id = bd.id
     GROUP BY bd.id
     ORDER BY bd.enabled DESC, bd.group_name, bd.display_name`
  );

  return (
    <>
      <div className="page-header">
        <div>
          <h1>Benchmark Controls</h1>
          <p className="muted">Control which imported metrics appear in comparisons.</p>
        </div>
      </div>

      <div className="panel">
        <table>
          <thead>
            <tr>
              <th>Group</th>
              <th>Display label</th>
              <th>Unit</th>
              <th>Higher better</th>
              <th>Enabled</th>
              <th>Results</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {definitions.map((definition) => (
              <tr key={definition.id}>
                <td>{definition.group_name}</td>
                <td>
                  <form id={`metric-${definition.id}`} action={updateDefinition}>
                    <input type="hidden" name="id" value={definition.id} />
                    <input name="display_name" defaultValue={definition.display_name} />
                  </form>
                </td>
                <td>
                  <input form={`metric-${definition.id}`} name="unit" defaultValue={definition.unit ?? ""} />
                </td>
                <td>
                  <input
                    form={`metric-${definition.id}`}
                    type="checkbox"
                    name="higher_is_better"
                    defaultChecked={Boolean(definition.higher_is_better)}
                  />
                </td>
                <td>
                  <input
                    form={`metric-${definition.id}`}
                    type="checkbox"
                    name="enabled"
                    defaultChecked={Boolean(definition.enabled)}
                  />
                </td>
                <td>{definition.result_count}</td>
                <td>
                  <button form={`metric-${definition.id}`} type="submit">
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

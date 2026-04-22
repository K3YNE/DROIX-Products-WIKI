import { QuartzTransformerPlugin } from "../types"

/**
 * Maps wiki frontmatter field `updated` to `modified` so that
 * Quartz's CreatedModifiedDate plugin can read it correctly.
 * The DROIX wiki uses `updated` instead of Quartz's expected `modified`.
 */
export const DroixDates: QuartzTransformerPlugin = () => {
  return {
    name: "DroixDates",
    markdownPlugins() {
      return [
        () => (_tree, file) => {
          if (file.data.frontmatter && file.data.frontmatter.updated) {
            file.data.frontmatter.modified ??= file.data.frontmatter.updated
          }
        },
      ]
    },
  }
}

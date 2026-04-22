import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      DROIX: "https://droix.co.uk",
      YouTube: "https://youtube.com/@droix",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      title: "Wiki",
      folderDefaultState: "collapsed",
      mapFn: (node) => {
        // Rename folder display names for clarity
        const folderNames: Record<string, string> = {
          products: "Products",
          entities: "Brands & Technology",
          concepts: "Concepts",
          sources: "Sources & Reviews",
          analysis: "Analysis",
        }
        if (node.isFolder && folderNames[node.displayName]) {
          node.displayName = folderNames[node.displayName]
        }
      },
      sortFn: (a, b) => {
        // Sort top-level folders in a meaningful order
        const folderOrder: Record<string, number> = {
          Products: 0,
          "Brands & Technology": 1,
          Concepts: 2,
          Analysis: 3,
          "Sources & Reviews": 4,
        }
        const aOrder = folderOrder[a.displayName] ?? 99
        const bOrder = folderOrder[b.displayName] ?? 99
        if (a.isFolder && b.isFolder && (aOrder !== 99 || bOrder !== 99)) {
          return aOrder - bOrder
        }
        // Default: folders before files, then alphabetical
        if (a.isFolder && !b.isFolder) return -1
        if (!a.isFolder && b.isFolder) return 1
        return a.displayName.localeCompare(b.displayName)
      },
    }),
  ],
  right: [
    Component.Graph({
      localGraph: {
        depth: 2,
        showTags: false,
      },
    }),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      title: "Wiki",
      folderDefaultState: "collapsed",
    }),
  ],
  right: [],
}

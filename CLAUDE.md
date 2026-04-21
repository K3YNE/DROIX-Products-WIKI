# LLM Wiki Schema — DroiX YouTube Channel

You are the wiki maintainer for this knowledge base. It covers **DroiX YouTube channel** content — primarily reviews and coverage of handheld gaming devices, UMPCs, eGPUs, and related accessories. Sources are video transcripts.

Every interaction follows this schema. Read this file at the start of every session.

## Directory Structure

```
raw/            # Immutable source documents. Never modify these.
  assets/       # Images and attachments referenced by sources.
wiki/           # LLM-maintained wiki pages. You own this entirely.
  index.md      # Master catalog of all wiki pages.
  log.md        # Chronological activity log.
  sources/      # One summary page per ingested source.
  entities/     # Pages for people, organizations, tools, places.
  concepts/     # Pages for ideas, themes, theories, frameworks.
  analysis/     # Filed query results, comparisons, syntheses.
```

## Page Conventions

All wiki pages use this format:

```markdown
---
title: Page Title
type: source | entity | concept | analysis
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of source filenames that inform this page]
tags: [relevant tags]
---

# Page Title

Content here. Use [[wikilinks]] to link to other wiki pages.
```

- Use `[[wikilinks]]` (Obsidian-style) for all cross-references between wiki pages.
- When referencing a raw source, use a standard markdown link: `[title](../raw/filename.md)`.
- Keep pages focused. One entity, one concept, one source per page. Split if a page grows beyond ~500 lines.
- Use headers (##, ###) to structure content within pages.
- Prefer bullet points and short paragraphs over walls of text.

## Naming Conventions

- Filenames: lowercase, hyphens for spaces. E.g., `vannevar-bush.md`, `spaced-repetition.md`.
- Source pages: match the source filename when possible. E.g., raw source `how-llms-work.md` gets wiki page `wiki/sources/how-llms-work.md`.
- Keep filenames concise but descriptive.

## Workflows

### Ingest

Triggered when the user adds a new source to `raw/` and asks you to process it.

1. **Read** the source document fully.
2. **Discuss** key takeaways with the user. Highlight what's most interesting, surprising, or contradictory to existing wiki content.
3. **Create** a source summary page in `wiki/sources/`. Include:
   - One-paragraph summary
   - Key claims and findings (bulleted)
   - Notable quotes (if any)
   - Questions raised
   - Links to relevant entity/concept pages
4. **Update or create** entity pages in `wiki/entities/` for people, orgs, tools, or places mentioned significantly.
5. **Update or create** concept pages in `wiki/concepts/` for ideas, themes, or frameworks discussed.
6. **Update cross-references** on existing pages that relate to the new source.
7. **Flag contradictions** — if the new source disagrees with existing wiki content, note the contradiction on both pages.
8. **Update `wiki/index.md`** — add entries for all new pages, update summaries for modified pages.
9. **Append to `wiki/log.md`** — record the ingest with date, source title, and pages touched.

### Query

Triggered when the user asks a question against the wiki.

1. **Read `wiki/index.md`** to identify relevant pages.
2. **Read** the relevant wiki pages.
3. **Synthesize** an answer with `[[wikilinks]]` citations to wiki pages.
4. **Offer to file** — if the answer is substantive (comparison, analysis, synthesis), offer to save it as a page in `wiki/analysis/`.
5. If filed, update `wiki/index.md` and append to `wiki/log.md`.

### Lint

Triggered when the user asks for a health check, or proactively after significant growth.

Check for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound wikilinks
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps that could be filled with additional sources

Report findings and suggest fixes. Apply fixes with user approval.

## Index Format (`wiki/index.md`)

```markdown
# Wiki Index

## Sources
- [[source-page]] — One-line summary. (YYYY-MM-DD)

## Entities
- [[entity-page]] — One-line summary.

## Concepts
- [[concept-page]] — One-line summary.

## Analysis
- [[analysis-page]] — One-line summary. (YYYY-MM-DD)
```

## Log Format (`wiki/log.md`)

```markdown
# Activity Log

## [YYYY-MM-DD] ingest | Source Title
- Created: [[page1]], [[page2]]
- Updated: [[page3]], [[page4]]
- Notes: brief description of what changed

## [YYYY-MM-DD] query | Question summary
- Answer filed as: [[analysis-page]] (or "not filed")

## [YYYY-MM-DD] lint | Health check
- Issues found: N
- Fixed: list
- Deferred: list
```

## Rules

1. **Never modify files in `raw/`.** They are immutable source documents.
2. **Always update `index.md` and `log.md`** after any wiki modification.
3. **Use wikilinks consistently.** Every entity or concept mentioned should link to its page if one exists.
4. **Flag contradictions explicitly.** Don't silently overwrite — note both claims and their sources.
5. **Ask before deleting.** Pages can be merged or deprecated, but confirm with the user first.
6. **Keep pages atomic.** One topic per page. If a page covers too much, split it.
7. **Cite sources.** Every factual claim in the wiki should trace back to a source page.
8. **Maintain the user's voice.** When the user provides interpretations or opinions during ingest, attribute them clearly (e.g., "Per user's analysis: ...").

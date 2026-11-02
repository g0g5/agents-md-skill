# AGENTS.md Legacy Migration

Use this guide when an existing `AGENTS.md` still stores workflow or note content inline instead of indexing files under `.agents/`. The shared index format, directory rules, and file conventions live in `SKILL.md`; this guide only covers the migration itself.

## When To Use

Migrate when any of these are true:

- `Workflows`, `Working Guide`, or `Notes` contains prose, steps, or bullet lists instead of one-line file links.
- The file uses older section names such as `Project Overview`, `Development Guide`, `Working Guide`, or `Tech Stack` nested under `Development Guide`.
- Workflow or note content exists in `AGENTS.md` while `.agents/workflows/` or `.agents/notes/` is missing or incomplete.

Do not migrate when `AGENTS.md` already uses the indexed layout and the indexes match the files on disk. That case is a normal update.

## Section Mapping

| Legacy content | New location |
| --- | --- |
| `Project Overview` | `Overview` |
| Stack details inside `Development Guide` or `Tech Stack` | top-level `Tech Stack` |
| `Development Guide > Commands` | top-level `Commands` |
| `Development Guide > Workflows` | files under `.agents/workflows/` |
| `Working Guide` | files under `.agents/workflows/` |
| `Notes` prose | files under `.agents/notes/` |

## Migration Steps

1. Inventory the legacy sections returned by the delegated inspection. List every workflow, operation set, and note block before writing anything.
2. Split by topic: one workflow or one group of related caveats per file. Use a kebab-case filename that names the topic, and add a subdirectory when that keeps the index readable.
3. Write each file in the standard shape: `# Title`, one summary sentence, then concise steps or bullets. Tighten wording, but keep every fact, command, constraint, and reference.
4. Move content that belongs elsewhere first: pure command lists go to `Commands`, structure or stack facts go to their own sections, and references go into the file that needs them. Do not create a file just to hold a command list.
5. Drop content that is outdated or contradicts the current project. Record each drop and the reason for the final summary.
6. Resolve collisions: if the target file already exists, merge into it or choose a different filename. Never overwrite an existing file blindly.
7. Do not add workflow or note files beyond what the legacy content requires. Migration is not an invitation to document new processes.
8. Rewrite `Workflows` and `Notes` as indexes of the files that now exist, using `[No content yet.]` when a section has no files.
9. Re-check that no legacy prose remains in either section and that every index entry links to a real file.

## Reporting

In the final summary, add to the usual create/update report:

- The files created under `.agents/workflows/` and `.agents/notes/`.
- Where each legacy block moved, in old section to new file form.
- Any content dropped, with the reason.
- Any merge or rename performed because of a filename collision.

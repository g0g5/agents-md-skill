# Generic Project Guide

Use this guide for documentation, configuration, content, prompt, asset, and other non-code projects. The final `AGENTS.md` should orient agents to the project purpose, organization, and documented tooling.

Shared workflow, section layout, and `.agents/` index rules live in `SKILL.md`. Read that first and use `templates/AGENTS.md` for the section order.

## Delegated Inspection

Add these non-code requirements to the shared `@explore` request in `SKILL.md`:

- WHAT: project type, major content or configuration areas, any relevant tooling, and a structure tree with one-line purpose per item.
- WHY: project purpose and the role of each major section.
- HOW `commands`: only documented validation, preview, or publishing scripts. Leave `Tech Stack` and `Commands` sparse or write `[No content yet.]` when the project has none.

For the structure tree, instruct the `@explore` agent to:

- Include meaningful hierarchy, drilling into sections that define the project's organization.
- Include files only when they are entrypoints or serve a unique, project-significant role.
- Omit repetitive leaves and fold interchangeable siblings with `- ...`.
- Exclude generated, cache, vendor, and dot-prefixed internals unless they are part of the core project layout.

If the delegated inspection shows this is primarily a software/code project with build, test, or typecheck workflows, switch to `guides/CODING.md` before writing.

## Writing AGENTS.md

Fill the sections from the delegated inspection, focusing on information agents need for ordinary non-code project work: purpose, structure, documented scripts, and project-specific caveats.

Leave `Workflows` and `Notes` as indexes into `.agents/` files. Do not inline workflow steps or caveats when a matching file already covers them.

## Quality Bar

Before finishing, check that the `AGENTS.md`:

- Is concise and avoids long prose.
- Explains what the project is and why it exists in one sentence.
- Maps meaningful sections and omits repetitive leaves.
- Uses selective file inclusion for entrypoints or uniquely important files only.
- Lists validation or publishing scripts only when the project documents them.
- Keeps `Workflows` and `Notes` as one-line indexes that match the actual files under `.agents/`.
- Avoids generated, cache, vendor, and dot-prefixed internals unless core to the project layout.
- Does not include secrets, local machine assumptions, or rarely used trivia.

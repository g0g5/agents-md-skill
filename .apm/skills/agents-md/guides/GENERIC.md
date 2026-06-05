# Generic Project Guide

Use this guide for documentation, configuration, content, prompt, asset, and other non-code projects. The final `AGENTS.md` should orient agents to the project purpose, organization, common workflows, and validation steps.

## Delegated Inspection

Ask one `@explore` agent to inspect the workspace and return a concise report covering:

- WHAT: project type, major content or configuration areas, any relevant tooling, and a structure tree with one-line purpose per item.
- WHY: project purpose and the role of each major section.
- HOW: only the most common workflows agents need, such as editing, reviewing, validating, previewing, publishing, or deployment when they are central to the project.

For the structure tree, instruct the `@explore` agent to:

- Include meaningful hierarchy, drilling into sections that define the project's organization.
- Include files only when they are entrypoints or serve a unique, project-significant role.
- Omit repetitive leaves and fold interchangeable siblings with `- ...`.
- Exclude generated, cache, vendor, and dot-prefixed internals unless they are part of the core project layout.

If an `AGENTS.md` already exists, also ask the `@explore` agent to compare it against the current workspace and call out structure, purpose, tooling, or workflow differences that may make it stale.

If the delegated inspection shows this is primarily a software/code project with build, test, or typecheck workflows, switch to `guides/CODING.md` and `templates/CODING.md` before writing.

## Writing AGENTS.md

Use `templates/GENERIC.md` as the canonical `AGENTS.md` template. Read it before writing or updating the file, then fill the sections with project-specific content from the delegated inspection.

Focus on information agents need for ordinary non-code project work: purpose, structure, common workflows, validation commands, and project-specific caveats.

## Quality Bar

Before finishing, check that the `AGENTS.md`:

- Is concise and avoids long prose.
- Explains what the project is and why it exists in one sentence.
- Maps meaningful sections and omits repetitive leaves.
- Uses selective file inclusion for entrypoints or uniquely important files only.
- Gives agents enough workflow and validation guidance to perform normal changes.
- Avoids generated, cache, vendor, and dot-prefixed internals unless core to the project layout.
- Does not include secrets, local machine assumptions, or rarely used trivia.

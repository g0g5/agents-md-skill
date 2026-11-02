# Coding Project Guide

Use this guide for software/code projects. The final `AGENTS.md` should help coding agents understand the project purpose, stack, structure, and normal verification loop.

Shared workflow, section layout, and `.agents/` index rules live in `SKILL.md`. Read that first and use `templates/AGENTS.md` for the section order.

## Delegated Inspection

Add these code-specific requirements to the shared `@explore` request in `SKILL.md`:

- WHAT: tech stack, package manager, monorepo app and package boundaries, and a structure tree with one-line purpose per item.
- WHY: project purpose and the role of each major component.
- HOW `commands`: only the most universally needed commands: build, test, typecheck, and verify changes.

For the structure tree, instruct the `@explore` agent to:

- Include meaningful directory hierarchy, including deeper nested directories when they clarify module boundaries.
- Include each app and shared package as a top-level module in monorepos.
- Include files only when architecturally important, such as entrypoints, shared foundations, registries, orchestration files, or files other project code depends on.
- Omit leaf implementation files and repetitive sibling files that are mostly interchangeable or isolated variants, unless one is the canonical entrypoint or shared base.
- Exclude dot-prefixed internals and generated, build, cache, and vendor directories unless they are part of the core source layout.

If the delegated inspection shows this is not primarily a software/code project, switch to `guides/GENERIC.md` before writing.

## Writing AGENTS.md

Fill the sections from the delegated inspection, focusing on information agents need for ordinary coding tasks: purpose, stack, structure, and verification commands.

Leave `Workflows` and `Notes` as indexes into `.agents/` files. Do not inline workflow steps or caveats when a matching file already covers them.

## Quality Bar

Before finishing, check that the `AGENTS.md`:

- Is concise and avoids long prose.
- Explains what the project is and the stack in one sentence.
- Maps meaningful modules and omits repetitive leaves.
- Uses selective file inclusion for architectural files only.
- Avoids generated, cache, vendor, and dot-prefixed internals unless core to the source layout.
- Gives agents enough build/test/typecheck guidance to verify normal changes.
- Keeps `Workflows` and `Notes` as one-line indexes that match the actual files under `.agents/`.
- Does not include secrets, local machine assumptions, or rarely used trivia.

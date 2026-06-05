# Coding Project Guide

Use this guide for software/code projects. The final `AGENTS.md` should help coding agents understand the project purpose, stack, structure, and normal verification loop.

## Delegated Inspection

Ask one `@explore` agent to inspect the workspace and return a concise report covering:

- WHAT: tech stack and a structure tree with one-line purpose per item.
- WHY: project purpose and the role of each major component.
- HOW: only the most universally needed commands: build, test, typecheck, and verify changes.

For the structure tree, instruct the `@explore` agent to:

- Include meaningful directory hierarchy, including deeper nested directories when they clarify module boundaries.
- Include each app and shared package as a top-level module in monorepos.
- Include files only when architecturally important, such as entrypoints, shared foundations, registries, orchestration files, or files other project code depends on.
- Omit leaf implementation files and repetitive sibling files that are mostly interchangeable or isolated variants, unless one is the canonical entrypoint or shared base.
- Exclude dot-prefixed internals and generated, build, cache, and vendor directories unless they are part of the core source layout.

If an `AGENTS.md` already exists, also ask the `@explore` agent to compare it against the current workspace and call out structure, tech stack, or tooling differences that may make it stale.

If the delegated inspection shows this is not primarily a software/code project, switch to `guides/GENERIC.md` and `templates/GENERIC.md` before writing.

## Writing AGENTS.md

Use `templates/CODING.md` as the canonical `AGENTS.md` template. Read it before writing or updating the file, then fill the sections with project-specific content from the delegated inspection.

Focus on information agents need for ordinary coding tasks: purpose, structure, stack, and verification commands.

## Quality Bar

Before finishing, check that the `AGENTS.md`:

- Is concise and avoids long prose.
- Explains what the project is and the stack in one sentence.
- Maps meaningful modules and omits repetitive leaves.
- Uses selective file inclusion for architectural files only.
- Avoids generated, cache, vendor, and dot-prefixed internals unless core to the source layout.
- Gives agents enough build/test/typecheck guidance to verify normal changes.
- Does not include secrets, local machine assumptions, or rarely used trivia.

---
name: agents-md
description: Create or update a concise AGENTS.md for the project. Use this whenever the user asks to create, refresh, audit, fix, or maintain AGENTS.md.
compatibility: Requires an explore subagent or equivalent delegated workspace-inspection agent.
---

# AGENTS.md Workflow

Use this skill to create or update `AGENTS.md` in a project. The goal is a short, useful file that helps coding agents become productive quickly without burying them in obvious or rarely used details.

## Core Principles

- Create a TODO list before starting and keep it current.
- Delegate workspace inspection to exactly one `@explore` agent. Do not inspect the workspace yourself before delegation.
- Keep the final `AGENTS.md` concise and practical.
- Focus on information agents need for ordinary coding tasks: purpose, structure, stack, and verification commands.
- Prefer the smallest correct update when an `AGENTS.md` already exists.

## Starting State

Identify which case applies from the user's request and the delegated inspection result:

- No existing `AGENTS.md`: create a new one.
- Existing `AGENTS.md`: update it only where it is stale, incomplete, or conflicts with current structure, tech stack, or tooling.

When updating an existing file, preserve accurate useful content. Do not rewrite for style alone.

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

## Writing AGENTS.md

Use the templates in this skill directory as the canonical `AGENTS.md` templates. Read the appropriate one before writing or updating the file, then fill the sections with project-specific content from the delegated inspection:

- `TEMPLATE-CODING.md` — for software/code projects (includes tech stack, build/test/typecheck commands)
- `TEMPLATE-GENERIC.md` — for documentation, configuration, and other non-code projects

See each template for detailed formatting rules and examples.

## Quality Bar

Before finishing, check that the `AGENTS.md`:

- Is concise and avoids long prose.
- Explains what the project is and the stack in one sentence.
- Maps meaningful modules and omits repetitive leaves.
- Uses selective file inclusion for architectural files only.
- Avoids generated, cache, vendor, and dot-prefixed internals unless core to the source layout.
- Gives agents enough build/test/typecheck guidance to verify normal changes.
- Does not include secrets, local machine assumptions, or rarely used trivia.

## Response Summary

After creating or updating the file, summarize:

- The path changed.
- Whether this was a new file or an update.
- Any commands or verification steps run, or why they were not run.

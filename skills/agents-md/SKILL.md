---
name: agents-md
description: Use when the user asks to create, refresh, audit, fix, or maintain AGENTS.md for a project. Create or update a concise, practical agent onboarding file.
compatibility: Requires an explore subagent or equivalent delegated workspace-inspection agent.
---

# AGENTS.md Workflow

Use this skill to create or update `AGENTS.md` in a project. The goal is a short, useful file that helps agents become productive quickly without burying them in obvious or rarely used details.

## Core Workflow

- Create a TODO list before starting and keep it current.
- Delegate workspace inspection to exactly one `@explore` agent. Do not inspect the workspace yourself before delegation.
- Treat the user's instructions and any existing `AGENTS.md` content rules as higher priority than this skill's instructions. When they conflict, follow the user's instructions and existing rules.
- Keep the final `AGENTS.md` concise and practical.
- Prefer the smallest correct update when an `AGENTS.md` already exists.
- Keep template section headings even when there is no suitable content to add. Write `[No content yet.]` as the section content in that case.

## Guide Selection

Read the appropriate guide before inspecting or writing:

- `guides/CODING.md` - for software/code projects. Use `templates/CODING.md`.
- `guides/GENERIC.md` - for documentation, configuration, and other non-code projects. Use `templates/GENERIC.md`.

If the project type is unclear from the request, read both guides and ask the delegated inspection to classify the workspace before choosing the final guide and template.

## Starting State

Identify which case applies from the user's request and the delegated inspection result:

- No existing `AGENTS.md`: create a new one.
- Existing `AGENTS.md`: update it only where it is stale, incomplete, or conflicts with the current project structure, purpose, stack, tooling, or workflows.

When updating an existing file, preserve accurate useful content. Do not rewrite for style alone.

## Response Summary

After creating or updating the file, summarize:

- The path changed.
- Whether this was a new file or an update.
- Any commands or verification steps run, or why they were not run.

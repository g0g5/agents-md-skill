# Skill Alignment

Keep `SKILL.md`, `MIGRATION.md`, guides, template, and README behavior aligned when changing the skill workflow.

- A change to the section layout or `.agents/` index rules belongs in `SKILL.md` and `skills/agents-md/templates/AGENTS.md` together.
- A change to legacy detection, splitting, or reporting steps belongs in `MIGRATION.md`; `SKILL.md` keeps only the pointer.
- Update the matching guide when inspection focus or a quality bar changes.
- Update `README.md` expected behavior whenever the default runtime behavior changes, including when files under `.agents/` may or may not be created.
- Avoid duplicating `.agents/` index rules in the guides; reference `SKILL.md` instead.

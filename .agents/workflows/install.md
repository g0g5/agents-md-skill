# Install Local Skill Copy

How to install this skill into a local agent client after cloning the repository.

## Claude Code

```bash
mkdir -p ~/.claude/skills/agents-md
cp -R skills/agents-md/. ~/.claude/skills/agents-md/
```

## OpenCode And Other Clients

```bash
mkdir -p ~/.agents/skills/agents-md
cp -R skills/agents-md/. ~/.agents/skills/agents-md/
```

Keep `README.md` install instructions in sync with these commands.

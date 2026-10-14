# Assignment 3 support (IIMK AIBP Course 3)

This repository is run by the `a3-support-agent`. In Claude Code, follow the agent's rules for every task here: stages, approval gates, the shared ledger, and keeping every judgement with the author.

@.claude/agents/a3-support-agent.md

## Layout
- Skills: `.claude/skills/<name>/SKILL.md` (shared with VS Code Copilot and the Copilot app).
- Agent: `.claude/agents/a3-support-agent.md` (Claude Code) and `.github/agents/a3-support-agent.agent.md` (Copilot). Keep the two identical apart from the file name.
- Working files: `ledger/`, `drafts/`, `sources_text/`, `tests/`. See `README.md` for details.

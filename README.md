# token-saver

A Claude Code skill that keeps token use and cost low: an audit script for context bloat plus lean working rules.

Page: https://mr1charles.github.io/token-saver/

## Install
```
git clone https://github.com/mr1charles/token-saver
cp -r token-saver/skills/token-saver ~/.claude/skills/
```
Then ask Claude: "audit my token use", or run `python3 ~/.claude/skills/token-saver/scripts/audit.py`.

## What it does
- `audit.py` (read-only): lists enabled plugins, MCP deny rules, instruction-file sizes, rough token estimate (~4 chars/token).
- `SKILL.md`: one task per session, small reads, small images, no needless subagents, `/clear` and `/compact` habits, how to disable plugins and connectors.

Estimates are rough. Use `/context` for real numbers. MIT license.

---
name: token-saver
description: Keep Claude Code token use and cost low. Use at the start of a session, when the user mentions tokens, cost, usage, "context is big", slow or expensive sessions, or before long tool-heavy work. Audits settings for context bloat and enforces lean working habits.
---

# Token saver

Cost per turn = fixed context (system prompt, tool names, MCP instructions, skill list, memory files) + the whole conversation re-sent. The second part grows every turn and is usually the bigger bill.

## Do now
1. Run `python3 ~/.claude/skills/token-saver/scripts/audit.py`. It lists enabled plugins, connector count, deny rules and instruction-file sizes, with an estimated fixed-context cost.
2. Tell the user the top 2-3 findings. Never edit `settings.json` without a backup copy and the user's OK.

## Rules while working
1. One task per session. Done, or ~150k tokens in? Save state to notes, tell the user to `/clear`.
2. After a long tool-heavy stretch, suggest `/compact`.
3. Read small: `grep`, `head`, `tail`, line ranges. Never cat big files, logs or JSON. Never re-read a file already in context.
4. Images are expensive: <= 900 px wide, few frames, one look per check.
5. Batch independent tool calls in one turn.
6. No subagents or workflows unless clearly worth it; each starts cold and re-reads context.
7. Long jobs: run in background, read only the last lines of the log.
8. Answer first, no recap, no offers. Summarize long output and point to a file.
9. Keep instruction files (CLAUDE.md, memory index) under ~40 lines; link, don't copy.

## Cutting fixed context
- Disable plugins you do not use: set `"enabledPlugins": {"name@market": false}` in `~/.claude/settings.json`.
- Remove unused connectors: add `"mcp__claude_ai_<Server>"` to `permissions.deny`. Even unused servers cost tokens for names and instructions.
- Restore anything later by flipping the flag or removing the deny rule.
- Check real numbers with `/context`; the audit script only estimates.

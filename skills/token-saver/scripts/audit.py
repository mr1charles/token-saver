#!/usr/bin/env python3
"""Estimate Claude Code fixed-context bloat. Read-only. ~4 chars/token."""
import json, pathlib, sys
h = pathlib.Path.home() / ".claude"
tok = lambda p: p.stat().st_size // 4 if p.exists() else 0
try:
    s = json.loads((h / "settings.json").read_text())
except Exception as e:
    sys.exit(f"cannot read settings.json: {e}")
plugins = s.get("enabledPlugins", {})
on = sorted(k for k, v in plugins.items() if v)
deny = s.get("permissions", {}).get("deny", [])
conn = [d for d in deny if d.startswith("mcp__")]
print(f"plugins on ({len(on)}): {', '.join(on) or 'none'}")
print(f"deny rules: {len(deny)} ({len(conn)} MCP)")
files = [h / "CLAUDE.md", *h.glob("projects/*/memory/MEMORY.md")]
tot = 0
for f in files:
    t = tok(f); tot += t
    flag = "  <- big, trim" if t > 1500 else ""
    print(f"{f.relative_to(h)}: ~{t} tokens{flag}")
skills = [d for d in (h / "skills").glob("*") if d.is_dir()]
print(f"user skills: {len(skills)} (each adds a description line to context)")
print(f"instruction files total: ~{tot} tokens")
if len(on) > 4:
    print("TIP: many plugins on; each adds skills/hooks. Disable unused ones.")
if len(conn) < 5:
    print("TIP: few connectors denied; check /context for MCP tool names you never use.")

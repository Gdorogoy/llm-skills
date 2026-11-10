#!/usr/bin/env python3
"""UserPromptSubmit: when a plan is pending, a user reply like 'yes'/'proceed' approves it."""
import json, os, re, sys
d = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
c = os.path.join(d, ".claude")
try:
    ev = json.load(sys.stdin)
except Exception:
    sys.exit(0)
p = (ev.get("prompt") or "").strip().lower()
if os.path.exists(os.path.join(c, "plan-pending")) and re.match(r"^(yes|y|ok|okay|proceed|approve[d]?|go|go ahead|do it|lgtm)\b", p):
    open(os.path.join(c, "plan-approved"), "w").close()

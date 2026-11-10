#!/usr/bin/env python3
"""PreToolUse: block Edit/Write while a plan is pending and not yet approved by the user."""
import json, os, sys
d = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
pending = os.path.exists(os.path.join(d, ".claude", "plan-pending"))
approved = os.path.exists(os.path.join(d, ".claude", "plan-approved"))
try:
    ev = json.load(sys.stdin)
except Exception:
    sys.exit(0)
tool = ev.get("tool_name", "")
cmd = (ev.get("tool_input") or {}).get("command", "")
deny = None
if pending and not approved and tool in ("Edit", "Write", "NotebookEdit"):
    deny = "Plan not approved yet. Present the plan and wait for the user to say yes."
elif tool == "Bash" and "plan-approved" in cmd:
    deny = "Only the user can approve a plan. Do not create .claude/plan-approved."
if deny:
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
        "permissionDecision": "deny", "permissionDecisionReason": deny}}))

---
name: small-steps
description: "Limit work to one small change at a time, verifying between each. Use for any multi-file task. Trigger: /small-steps"
---
# /small-steps
Rules:
- One logical change per step; at most one or two files.
- Read the file before editing it. Edit only what the step needs. No drive-by refactors.
- After each step: run the test/build/linter and show the result.
- If a step fails twice, STOP and report what you tried. Do not pile on more changes.
- After each step print: `Step N done: <what> | verified by: <command> | next: <step>`.
- Never touch files outside the plan without asking.

## Pauses (ask the user before continuing)
Default mode: after each step print the `Step N done` line, then
- **PAUSE and wait for "ok"** if the step touched more than one file, changed behavior (logic, order, data, API), or deleted anything.
- **Continue** if it was a small safe edit (comment, rename, test-only, formatting) and verification passed.

The user can change the mode at any time:
- "pause every step" → wait for ok after every step
- "no pauses" → run all steps, report at the end (still stop on failure)
When pausing, show what changed (`git diff` or the edited lines) and the verification result, then ask: "Continue to step N+1?"

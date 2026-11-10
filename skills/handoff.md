---
name: handoff
description: "Save session state to a file so a fresh context can continue. Trigger: /handoff"
---
# /handoff
Write `HANDOFF.md` in the project root (overwrite):

```
# Handoff — <date>
## Goal
## Done (with file paths)
## In progress / current state (what exact command fails, if any)
## Next steps (ordered, concrete)
## Decisions made & why
## Gotchas / things that did NOT work
## Key files
## How to verify (commands)
```
Only include facts you verified. Mark guesses as "unverified". At the start of a new session, read HANDOFF.md first.

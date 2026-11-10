---
name: cornell-summary
description: "Summarize changes (git diff, session work, PR, or a folder) as Cornell notes: cues/questions, notes, and a short summary. Trigger: /cornell-summary [target]"
---

# /cornell-summary — Cornell-note summary of changes

## Gather (facts only, via tools)
- In a git repo: `git status`, `git diff --stat`, `git diff` (or `git diff <base>...HEAD`, or the PR if given).
- Not a git repo: use what you changed this session + file mtimes (`find . -mtime -1`).
- Read changed hunks; don't summarize from filenames alone. If unsure what something does, read it. Run `/verify` on any claim you can't point to a line for.

## Output format (exactly this layout)

```
# Cornell Notes — <topic: what the change is about>
Date: <today> · Scope: <repo/branch/files> · Size: <N files, +A/−D>

| Cues / Questions                  | Notes                                           |
|-----------------------------------|-------------------------------------------------|
| Why was this change made?         | <motivation, 1–3 bullets>                       |
| What changed? (per area)          | <bullets grouped by module, with `path:line`>   |
| How does it work now?             | <new flow/behavior, before → after>             |
| What could break?                 | <risks, edge cases, migrations, untested parts> |
| How do I check it?                | <commands/tests to run; what's been run>        |
| What's left / open questions?     | <TODOs, decisions needed>                       |

## Summary
<2–4 sentences, plain language: what, why, impact, confidence level.>
```

## Rules
- Cues column = questions a reviewer would ask; Notes = answers. Keep notes terse, concrete, referenced.
- Separate facts (seen in diff) from inference (mark with "likely").
- No filler, no restating the diff line by line. Group by meaning, not by file order.
- Offer to save as `notes/<date>-<topic>.md` if the user wants it kept.

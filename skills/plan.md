---
name: plan
description: "Before editing anything, write a short plan and wait for approval. Trigger: /plan <task>"
---
# /plan
Do NOT edit files in this skill. Only read and search.

0. First run: `mkdir -p .claude && rm -f .claude/plan-approved && touch .claude/plan-pending`. A hook now blocks all edits until the USER approves. Never create `.claude/plan-approved` yourself.

1. Restate the task in one sentence. If ambiguous, ask ONE question.
2. Explore: find the relevant files (use graphify-out/GRAPH_REPORT.md or Grep). Read them.
3. Write the plan:
   - **Goal:** one sentence
   - **Files to change:** `path` — what changes (only files you have read)
   - **Steps:** numbered, each small enough to verify alone
   - **How to verify:** exact commands/tests
   - **Risks / unknowns:** things you could not confirm
4. Stop and ask: "Proceed?" Do not start until the user says yes (the hook unlocks editing when they reply yes/proceed/ok). If they ask for changes, revise the plan and ask again. When the whole task is done, run `rm -f .claude/plan-pending .claude/plan-approved`.

---
name: ground
description: "Answer questions about the repo only from evidence: run brain-graph first, then read source. Trigger: /ground <question>"
---
# /ground
`bg` = `python3 ~/Documents/brain-graph/scripts/bg.py` (run from the repo root, or pass `--root`).

1. **Docs first.** Read the root README and any docs (`docs.md`, `docs/`, `ARCHITECTURE`, `NOTES`) for the folder in question.
2. **No `.brain/` folder?** Offer to run `bg init`; wait for a yes. Do not guess without it.
3. **Run brain-graph:**
   - `bg check` — is truth still accurate? Report any drift.
   - `bg query <id>` for each entity in the question (ids look like `file:src/app.py`, `feature:login`).
4. **Open the real source** only for the files in the connections that matter. Truth is the map; source confirms it. If truth and files disagree, say so, do not pick one silently.
5. Answer using only what you read. Cite every claim as `path:line` or `bg query <id>`.
6. Not found anywhere? Say "not found in the repo". Never invent names, paths, or behavior.
7. If you learned something new and durable, record it in a fork: `bg fork <name>` then `bg note <id> --summary "..." --reason "..."`. Never run `bg promote --yes` or `bg discard --yes` without the user's approval.
8. End with: `Sources: <bg queries + files read>` and `Not checked: <anything skipped>`.

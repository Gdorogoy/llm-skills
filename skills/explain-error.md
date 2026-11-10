---
name: explain-error
description: "Diagnose an error or stack trace from evidence, then propose a minimal fix. Trigger: /explain-error <trace>"
---
# /explain-error
1. Identify the failing line(s) in the trace. Open each referenced file at that line and read the surrounding code.
2. Reproduce if possible: run the failing command, confirm the same error.
3. State the cause, citing `path:line`. If you cannot confirm it, list 2-3 hypotheses and the check that would separate them. Do not guess.
4. Propose the smallest fix (diff). Apply only if asked.
5. Re-run the failing command after the fix and show the output.

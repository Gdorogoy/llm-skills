---
name: verify
description: "Anti-hallucination check. Use after writing or before reporting code, answers, or claims about a codebase: verifies every file path, function, import, package, API, flag, and factual claim actually exists, and labels each claim VERIFIED / UNVERIFIED / WRONG. Trigger: /verify"
---

# /verify — anti-hallucination check

Goal: nothing leaves your mouth that you have not seen with a tool. Run this on your own last answer/diff (or on a target the user names).

## Procedure

1. **Extract claims.** List every checkable claim in the output as a numbered list:
   - file paths, directories
   - functions, classes, methods, variables, config keys, CLI flags, env vars
   - imports / packages / versions / external APIs and their signatures
   - behavior claims ("X calls Y", "this fixes Z", "tests pass")
   - numbers, dates, quotes, URLs
2. **Check each against ground truth** — never against memory:
   - code symbols: Grep/Read the actual file (or `graphify-out/graph.json` / `GRAPH_REPORT.md` if present, then confirm in source)
   - packages/APIs: check lockfile + installed source (`node_modules`, `site-packages`), or run `--help` / import it
   - behavior: run the code/test/command and read the real output
   - external facts: fetch the source; if none is reachable, mark UNVERIFIED
3. **Label** each claim:
   - `VERIFIED` — saw it; cite `path:line` or command output
   - `WRONG` — contradicted by evidence; give the correction
   - `UNVERIFIED` — could not check; say why
4. **Fix.** Correct every WRONG item in the actual output. Remove or hedge every UNVERIFIED item. Do not leave invented names "because they look plausible".
5. **Report** a compact table: `# | claim | status | evidence`, then one line: `N verified, N wrong (fixed), N unverified (hedged)`.

## Rules
- "Tests pass" / "it works" is only VERIFIED if you ran it this session and saw the output.
- Plausible-sounding ≠ true. If a name isn't found by search, it doesn't exist until proven otherwise.
- If you catch yourself guessing a signature, stop and read the source.
- Don't verify everything twice: batch greps, skip claims already evidenced in this conversation.
- Say "I don't know" rather than fill a gap.

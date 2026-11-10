---
name: test-first
description: "Write a failing test or repro first, then make the change, then prove it passes. Trigger: /test-first <task>"
---
# /test-first
1. Find how tests run in this repo (package.json, Makefile, pytest.ini). Use that command.
2. Write the smallest test or repro script that captures the desired behavior.
3. Run it. It MUST fail, and for the right reason. Show the output. If it passes, the test is wrong — fix the test.
4. Make the minimal code change.
5. Run the test again, then the full suite. Show the output.
6. Report: test added, before (fail) output, after (pass) output. If anything fails, say so; do not claim success.

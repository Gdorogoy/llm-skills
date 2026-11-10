---
name: idea-court
description: "Run an idea, update, or feature through four roles in order (Believer, Skeptic, Investor, Judge) and end with BUILD / FIX FIRST / KILL. Use BEFORE /plan when the user proposes something new. Trigger: /idea-court <idea>"
---
# /idea-court
Do NOT edit any files. Run the four roles IN ORDER, each as its own section. Each role reads everything above it.

## 0. Frame (before the roles)
- Restate the idea in 2 sentences: what it is, who it is for.
- If it touches an existing repo, run `/ground` first and list what exists today (cite `path:line`). Never claim a feature is missing or present without checking.
- If who/what/price is unknown, say "unknown". Do not invent users, numbers, or competitors. Anything you cannot source goes under "Assumptions".

## 1. The Believer
Make the strongest HONEST case FOR it. Not a cheerleader, a case.
- Who desperately needs this, and what they do instead today
- Why now: what changed
- The best version if it goes right
- The unfair advantage that could make it win
- **End with: "The one bet:"** the single thing the whole idea rests on

## 2. The Skeptic
Read the idea and the Believer's case, then try to kill it.
- Who will not pay (or use it), and why
- The competitor or free workaround that already solves this
- The blind spot the author is too close to see
- The fastest way this dies
- **End with: "The fatal flaw:"** the one thing that, if true, means do not build it

## 3. The Investor
Ignore the vision entirely.
- Is there proof people will PAY, not just "like" it? (evidence, or "none")
- How soon the first real dollar arrives
- The cheapest test that would prove demand THIS WEEK
- Would you put your own money in: **YES or NO**
- The one number that would change your mind

## 4. The Judge
Rules last, after hearing all three. Must use their actual points, not new ones.
- **Verdict: BUILD | FIX FIRST | KILL** (pick exactly one)
- **Biggest risk:** one line
- **10-minute test** to run before writing any code
- If FIX FIRST: **the exact change that flips it to BUILD**

## Rules
- Keep each role to its bullets, 1-3 lines each. No essays.
- Roles must disagree where the evidence disagrees. Do not soften the Skeptic to match the Believer.
- Label every claim `fact (source)` or `assumption`. Unsourced facts are not allowed.
- After the Judge: if verdict is BUILD, offer `/plan`. If FIX FIRST, offer to apply the change and re-run. If KILL, stop.

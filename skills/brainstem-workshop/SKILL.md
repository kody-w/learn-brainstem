---
name: brainstem-workshop
description: Run one Academy workshop from the AIBAST Agents Library end to end, building the solution, passing its locked cases, capturing evidence, and creating a reviewed Draft in Copilot Studio without publishing. Use when the learner is ready to prove a solution or asks about workshops, evidence, or Copilot Studio. Teaches evals, evidence, and Draft versus publish.
license: MIT
metadata:
  author: kody-w
  path: brainstem-workshop
---

# Prove one

## What the learner will understand at the end

"It works" is a claim. Evidence is the locked cases passing, the evidence report captured, and
a Draft a reviewer can open. Draft is not published; nothing reaches a user until a person
decides it should.

## Steps

1. Open the Academy: https://microsoft.github.io/aibast-agents-library/academy.html. If the learner already picked a solution in
   `brainstem-library`, use that one. Otherwise list the courses and ask.
2. Every workshop has two lanes, and each lane is its own skill file the learner attaches to
   their AI:
   - With the Brainstem: `https://microsoft.github.io/aibast-agents-library/skills/aibast-easy-mode-brainstem/SKILL.md`
   - Copilot only, no local server: `https://microsoft.github.io/aibast-agents-library/skills/aibast-easy-mode-copilot/SKILL.md`
   Fetch the lane skill that matches the learner's setup and follow it. Do not reinvent its
   steps; it owns discovery, build, test, and Draft.
3. The lane skill stops at a reviewed Draft in Copilot Studio with `published: false`. Confirm
   that with the learner in the Copilot Studio preview: run one locked case there.
4. Open the workshop's evidence report on the site (`solutions/<slug>/evidence-report.html`).
   Show the learner what was captured and what a reviewer would look at.
5. Optional: open the Manual lane on the workshop page. It replays every action the AI took, one
   browser frame per step, so they can see how the agent was built. Do not make them do it by
   hand unless they want to.

## Done when

- Every locked case passes in the local run.
- A Draft exists in Copilot Studio and answers one preview case.
- Nothing was published.

## Teach-back

1. What is the difference between a passing chat and evidence?
2. Why does the lane stop at Draft?
3. What did the Manual lane show that Easy mode hid?

Next: `brainstem-graduate`.

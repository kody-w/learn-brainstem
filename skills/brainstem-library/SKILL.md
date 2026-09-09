---
name: brainstem-library
description: Browse the AIBAST Agents Library from its registry, let the learner pick an industry solution, install its portable agent into the Brainstem, and run its locked test cases. Use when someone wants a real example agent, asks what is in the library, or wants to see an industry use case. Teaches portable single-file agents, registries, synthetic data, and evals.
license: MIT
metadata:
  author: kody-w
  path: brainstem-library
---

# Pick a real one from the library

## What the learner will understand at the end

An agent worth sharing is one file with a manifest, synthetic data inside it, and a set of
test cases that prove it. A registry is a list of those files with their checksums. Evals are
how you know an agent still works after you change it.

## Steps

1. Fetch `https://microsoft.github.io/aibast-agents-library/registry.json`. List entries whose `_catalog_kind` is
   `solution`, grouped by `category` written as a plain industry name, one line each:
   `display_name` and `description`. Do not paste JSON.
2. Ask one question: which one. Accept a number, a name, or a description. Resolve to exactly one
   entry and confirm the `display_name`.
3. Download the agent from `https://raw.githubusercontent.com/microsoft/aibast-agents-library/main/<_file>`. Verify the SHA-256 against `_sha256`. Refuse to
   continue on a mismatch; say what differed.
4. Install it either by copying the file into `~/.brainstem/src/rapp_brainstem/agents/` or by
   posting it: `curl -s -F file=@<the .py> localhost:7071/agents/import`.
5. Open the file with the learner. Find three things together: the manifest at the top, the
   synthetic data it carries, and the `perform` method. Say why the data is synthetic.
6. Fetch the locked cases: `https://raw.githubusercontent.com/microsoft/aibast-agents-library/main/tests/demo_cases/<slug>.json`, where `<slug>` comes from the
   registry entry's `_solution.package.slug`. Run every case through `/chat`. For each, check the
   `must_include` and `must_not_include` markers against the `response`. Report a table:
   case, pass or fail, the marker that decided it.
7. If any case fails, do not retry until it passes. Show the response and the marker, and ask the
   learner what they think happened.

## Done when

- One library agent is installed and listed by `/health`.
- Every locked case ran, with a pass or fail per case and the reason.
- The learner can point to the manifest, the synthetic data, and the tool in the file.

## Teach-back

1. What makes this agent portable, and what would break if the data were real?
2. What is the registry for, and why does the checksum matter?
3. What is a locked test case protecting against?

Next: `brainstem-memory`.

# Changelog

## 1.3.2 (2026-09-10)

- Proved live, end to end on one machine: `brainstem-first-agent` (tool written, loaded without
  restart, called from chat), `brainstem-share` (to-skill, prove PASS, check, run with no server),
  `brainstem-anywhere` (the same skill answered inside GitHub Copilot CLI), and ship rung 1. All
  four gave the identical answer. Ship rung 2 now names the device-code sign-in as the learner's step.

## 1.3.1 (2026-09-10)

- `brainstem-ship` accepts three inputs: the learner's own build, a ready-made harness
  workspace from an industry solution library (deploys unchanged with `--workspace-dir`), or
  both. Verified by packing a library solution with `pac copilot pack`: the guard's
  `cliagent-1.0.0` template came out as required.

## 1.3.0 (2026-09-09)

- New `brainstem-ship`: the skill runs in the GitHub Copilot harness on the learner's machine
  (proved live), becomes the skill of a Copilot Studio harness agent, is reached from code, and
  is opened to Teams and Microsoft 365 Copilot, all through copilot-harness-sdk. Rungs 2 to 4
  are written from the SDK's source and README and not yet run end to end here.
- Validator no longer treats Copilot Studio as foreign; it is a target, not a library.
- Live check covers the SDK's exports, deploy script, and the harness YAML shapes.

## 1.2.0 (2026-09-09)

- Registry: skip agents the Brainstem already bundles, pass `sha256` to the import so the
  Brainstem verifies integrity itself, and handle the 409 name conflict. Found by running the
  lesson against a live Brainstem.
- Memory: rewritten to what the Brainstem does. It saves a stated preference on its own, and
  "forget" records a retraction rather than erasing. The counterfactual is proved by moving
  the memory file aside. Found the same way.

Skills carry `metadata.version`. Bump it when a lesson's steps change so a learner who reinstalls
can tell.

## 1.1.0 (2026-09-09)

- Entry skill lists the raw URL of every other skill, so the one-URL path can reach them.
- Host precheck (terminal, file, URL access) and an "undo everything" section.
- Setup: what the piped installer does, how to start, stop, update, and uninstall; Windows notes.
- Registry: read the code before installing it; prefer official or verified tiers.
- Memory: real on-disk paths.
- Every teach-back question has a "good answer" for the AI to grade against.
- Live contract check and weekly CI that files an issue when a dependency drifts.

## 1.0.0 (2026-09-09)

- Seven skills on the RAPP foundation only.

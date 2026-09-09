---
name: brainstem-registry
description: Browse RAR, the open registry of single-file agents, let the learner pick one, verify its checksum, install it into the Brainstem, and use it from chat. Use when someone wants a real example agent, asks what other people have built, or asks how sharing works. Teaches portable single-file agents, registries, checksums, and provenance.
license: MIT
metadata:
  author: kody-w
  version: "1.1.0"
  path: brainstem-registry
---

# Pick one from the registry

## What the learner will understand at the end

An agent worth sharing is one file with a manifest at the top. A registry is a list of those
files with their checksums and a record of who published them. You install by downloading one
file and checking one hash. Nothing else.

## Steps

1. Fetch `https://kody-w.github.io/RAR/registry.json`. It lists about 1,700 agents. Do not paste it. Ask the learner
   what they are curious about, filter by `tags`, `category`, and `description`, and show at most
   ten: `display_name`, `description`, `quality_tier`, `author`. For this lesson, prefer
   `official` or `verified` tiers; `community` entries are fine to read, and say why you are
   choosing carefully: installing an agent means the Brainstem will run its `perform` code.
2. Ask one question: which one. Resolve to exactly one entry and confirm the `display_name`.
3. Download `https://raw.githubusercontent.com/kody-w/RAR/main/<_file>`. Compute its SHA-256 and compare with `_sha256`. Refuse to
   continue on a mismatch; say what differed. Show the `_lifecycle` and `_receipt` fields and say
   what they are: a record that this exact file was published, and by whom.
4. Read it before you run it. Open the downloaded file with the learner and look for anything
   that reaches outside the machine or the task: network calls, file writes outside the
   Brainstem folder, environment variables. Say what you see. If anything looks wrong, stop
   here and pick another agent. That habit is the lesson.
5. Install it: copy the file into `~/.brainstem/src/rapp_brainstem/agents/` using the entry's
   `_install_filename`, or post it: `curl -s -F file=@<the .py> localhost:7071/agents/import`.
6. Back in the file, find the `__manifest__` block, the `metadata` the model
   reads, and the `perform` method that runs. If the manifest has an `example_call`, send that
   through `/chat`; otherwise ask the model in plain words for what the description promises.
   Show the tool call in `agent_logs`.
7. Delete it again: `curl -s -X DELETE localhost:7071/agents/<_install_filename>`. Confirm
   `/health` no longer lists it. Installing and removing is two commands; that is the point.

## Done when

- One registry agent was verified, installed, used from chat, and removed.
- The learner can point to the manifest, the metadata, and the tool in the file.
- They can say what the checksum and the receipt each protect against.

## Teach-back

1. What makes this agent portable?
   A good answer: it is one file with its manifest and data inside; nothing else to install.
2. What does the checksum prove, and what does it not prove?
   A good answer: that the file is exactly what the registry recorded; not that the code is safe.
3. What would you look at before installing an agent from someone you do not know?
   A good answer: the tier and receipt, then the code itself, especially network and file access.

Next: `brainstem-memory`.

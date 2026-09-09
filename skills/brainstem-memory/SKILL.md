---
name: brainstem-memory
description: Show the learner how the Brainstem remembers across sessions with the bundled ContextMemory and ManageMemory agents, that memory is a file it writes on its own, and that forgetting is a design choice. Use when someone asks why the AI forgets, how memory works, or how state is kept. Teaches context windows, injected context, and stored state.
license: MIT
metadata:
  author: kody-w
  version: "1.2.0"
  path: brainstem-memory
---

# Remembering

## What the learner will understand at the end

A model has no memory. It has a context window, and everything it "remembers" was put into
that window on this request by something outside the model. Memory is state you store and
inject. The Brainstem bundles two agents for exactly that: `ManageMemory`, which the model
calls to save, and `ContextMemory`, which injects what was saved into every later turn. The
model decides when to save; watch it do so unasked.

## Steps

1. Open the store first, so the learner sees where memory lives before anything is in it:
   `~/.brainstem/src/rapp_brainstem/.brainstem_data/shared_memories/memory.json`. Per-user
   memory sits beside it under `.brainstem_data/memory/<guid>/user_memory.json`.
2. Send "My favourite colour is teal." with a `session_id` of your choosing. Read `agent_logs`:
   the Brainstem called `ManageMemory` and saved a preference without being asked. Open the
   file again; the entry is there. That is memory being written, by the model's decision.
3. New session (a different `session_id`): "What is my favourite colour?" It knows. Nothing
   from the first session was sent; `ContextMemory` injected the stored entry.
4. Prove the counterfactual. Move the file aside:
   `mv .../shared_memories/memory.json .../shared_memories/memory.json.aside`. Ask again in a
   new session. Now it does not know. Move the file back; it knows again. Memory is that file.
5. Ask it to forget. Read `agent_logs` and the file: `ManageMemory` recorded a retraction, and
   the original entry is still there. The Brainstem appends; it does not erase. Ask the learner
   whether a memory system should erase, and who should decide. There is no single right answer.
6. If they want it gone, delete the entry from the file by hand, or remove the file. Show the
   next answer no longer mentions teal.

## Done when

- The learner watched the save happen in `agent_logs` without asking for it.
- They saw the answer change when the file was moved away and back.
- They saw the retraction and can say why the entry was still there.

## Teach-back

1. Why did the model know the colour in a new session when nothing from the first was sent?
   A good answer: `ContextMemory` read the file and injected it into this request's context.
2. What is the difference between conversation history and memory here?
   A good answer: history is the turns of one session; memory is a file, written by a tool call
   and injected on later requests.
3. Where would this memory need to live if the agent ran for a team instead of one person?
   A good answer: somewhere shared and durable, with a decision about who can read and erase it.

Next: `brainstem-share`.

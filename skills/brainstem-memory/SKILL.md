---
name: brainstem-memory
description: Give the learner's Brainstem memory that survives across sessions using the bundled ContextMemory and ManageMemory agents, then show the difference between context and memory. Use when someone asks why the AI forgets, how memory works, or how state is kept. Teaches context windows, injected context, and stored state.
license: MIT
metadata:
  author: kody-w
  path: brainstem-memory
---

# Remembering

## What the learner will understand at the end

A model has no memory. It has a context window, and everything it "remembers" was put into
that window on this request by something outside the model. Memory is state you store and
inject. The Brainstem bundles two agents for exactly that: `ContextMemory`, which injects
stored context into every turn, and `ManageMemory`, which the model calls to save or change it.

## Steps

1. Prove forgetting. Send "My favourite colour is teal." Then, in a new session (omit or change
   `session_id`), ask "What is my favourite colour?" Show that it does not know.
2. Look at `agents/context_memory_agent.py` and `agents/manage_memory_agent.py` with the learner.
   Point at where `ManageMemory` writes, and where `ContextMemory` reads and returns context.
3. Ask the Brainstem to remember: "Remember that my favourite colour is teal." Show the tool call
   to `ManageMemory` in `agent_logs`.
4. New session again. Ask the question. Now it knows. Show the `<memory>` block that the
   Brainstem injected into the system context for that request.
5. Ask it to forget, and confirm it forgot.
6. Show where the memory file lives on disk and open it. Memory is a file; there is no magic.

## Done when

- The learner has seen the same question fail before memory and pass after.
- They have seen the stored file and the injected block.

## Teach-back

1. Why did the model not know the colour in a new session, even though you had just said it?
2. What is the difference between conversation history and memory here?
3. Where would this memory need to live if the agent ran for a team instead of one person?

Next: `brainstem-share`.

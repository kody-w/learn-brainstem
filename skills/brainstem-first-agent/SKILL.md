---
name: brainstem-first-agent
description: Write the learner's first tool as a single Python file, drop it into the Brainstem, and watch the model call it from chat. Use after setup, or when someone asks how tools, function calling, or agents work. Teaches system prompts, tool schemas, the agent loop, and hot reload.
license: MIT
metadata:
  author: kody-w
  version: "1.1.0"
  path: brainstem-first-agent
---

# Your first tool

## What the learner will understand at the end

The model does not run code. It reads a menu of tools, each described by a JSON schema, and
asks for one by name with arguments. The Brainstem runs the Python, hands the result back, and
the model writes the answer. That menu is the `metadata`; the Python is `perform`.

## Steps

1. Ask what small, real thing they want the AI to be able to do for them. Something with an
   obvious answer they can check: a unit conversion, a lookup in a list they give you, a date
   calculation. Avoid anything that needs a password or their data.
2. Write one file in `~/.brainstem/src/rapp_brainstem/agents/` (same path under the user's home
   folder on Windows), named `<thing>_agent.py`.
   The shape is fixed:

   ```python
   from agents.basic_agent import BasicAgent

   class TipCalculatorAgent(BasicAgent):
       def __init__(self):
           self.name = "TipCalculator"
           self.metadata = {
               "name": self.name,
               "description": "Splits a restaurant bill and adds a tip. Use when the user asks what to tip or how to split a bill.",
               "parameters": {
                   "type": "object",
                   "properties": {
                       "total": {"type": "number", "description": "Bill total"},
                       "people": {"type": "integer", "description": "How many people are paying"},
                       "tip_percent": {"type": "number", "description": "Tip percentage, default 18"}
                   },
                   "required": ["total", "people"]
               }
           }
           super().__init__(name=self.name, metadata=self.metadata)

       def perform(self, total, people, tip_percent=18):
           tip = round(total * tip_percent / 100, 2)
           return f"Tip {tip}, total {round(total + tip, 2)}, each pays {round((total + tip) / people, 2)}"
   ```

3. Do not restart anything. Agents are discovered from disk on every request.
4. Ask the model in plain words: "What should we each pay on a 84 dollar bill between three
   people?" Show the JSON answer and point at `agent_logs`: that is the tool call.
5. Now break it on purpose: make `perform` raise an exception. Send the message again. Show
   the learner what the model says when a tool fails, then fix it.
6. Change only the `description` so it no longer mentions bills. Ask the same question.
   Notice the model may stop choosing the tool. The description is how the model decides.

## Done when

- The learner's tool appears in `curl -s localhost:7071/health` under loaded agents.
- One chat message produced a tool call and a correct answer.
- They have seen a failing tool and a description that stopped being chosen.

## Teach-back

1. What does the model actually send when it wants a tool to run?
   A good answer: the tool's name and a JSON object of arguments; not code.
2. Which part of the file does the model read, and which part does it never see?
   A good answer: it reads `metadata` (the name, description, and parameter schema); it never
   sees `perform`, only its return value.
3. Why did changing one sentence change whether the tool was used?
   A good answer: the description is the only thing the model has to decide with.

Next: `brainstem-library`.

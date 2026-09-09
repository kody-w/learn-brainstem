---
name: brainstem-graduate
description: Take what the learner built in the Brainstem to where real users are, using the workshop's Copilot Studio solution export and the production guide. Use when someone asks "how do I ship this", "what's next", or where an agent runs in production. Teaches that the Brainstem is a learning and prototyping tool and the same skill graduates into GitHub Copilot, Copilot Studio, and Microsoft 365 Copilot.
license: MIT
metadata:
  author: kody-w
  path: brainstem-graduate
---

# Graduate

## What the learner will understand at the end

The Brainstem is a local frontier learning and rapid prototyping tool. It is not where an agent
lives for users. The same skill, unchanged in what it does, moves into first-party tools:
GitHub Copilot for the builder's daily work, Copilot Studio for the reviewed agent, Microsoft
365 Copilot and Teams for the people who use it. Read https://microsoft.github.io/aibast-agents-library/why.html with the learner first.

## Steps

1. Take the solution from `brainstem-workshop`. Its Copilot Studio export is at
   `https://microsoft.github.io/aibast-agents-library/solutions/<slug>/exports/<slug>-copilot-studio-solution.zip`, with
   `deployment.json` beside it describing the agent, its knowledge, and its capabilities.
2. Walk the production guide, https://microsoft.github.io/aibast-agents-library/docs/rapp-guide.html, and map the workshop onto its 14
   steps. Ask the learner which steps the workshop already covered and which are left. Write that
   list down for them.
3. Show the three surfaces and what each is for. Do not install anything else:
   - GitHub Copilot: where they will build and adapt the next agent.
   - Copilot Studio: where the reviewed Draft lives, and where publish is a human decision.
   - Microsoft 365 Copilot and Teams: where a published agent meets its users.
4. Ask the learner to describe, in their own words, one real use case from their work and how it
   would move through Learn, Prove, Ship. That description is the deliverable.
5. Point at the next thing to build. Send them back to `brainstem-first-agent` with their own
   use case, or to `brainstem-library` for a neighbouring solution.

## Done when

- The learner can say what the Brainstem is for and what it is not for, unprompted.
- They have a written use case mapped to Learn, Prove, Ship.
- They know which first-party surface each stage lands in.

## Teach-back

1. Why would you not run the Brainstem for real users?
2. What stays the same when a skill moves from the Brainstem to Copilot Studio?
3. Who decides to publish, and where?

That is the whole path. Start it again with their own use case.

---
name: brainstem-share
description: Turn the learner's agent into one skill file with rapp-skills, prove nothing is lost on the way there and back, and hand it to another person or tool. Use when someone asks how to share an agent, back up their agents, or what a skill is. Teaches the one-file idea and lossless portability.
license: MIT
metadata:
  author: kody-w
  path: brainstem-share
---

# One file that travels

## What the learner will understand at the end

The agent they wrote is already the whole thing. rapp-skills turns that Python file into a
`SKILL.md` that any AI tool can read, with the code carried inside it, and turns it back into
the same file, byte for byte. Sharing an agent is sending one file. Nothing to install.

## Steps

1. Get the converter. It is one file: https://github.com/kody-w/rapp-skills. Clone it or fetch `rapp_skills.py`.
   Python 3.11 or newer, nothing else.
2. Convert the agent from `brainstem-first-agent`:

   ```bash
   python3 rapp_skills.py to-skill ~/.brainstem/src/rapp_brainstem/agents/<their>_agent.py --out ~/my-skills
   python3 rapp_skills.py check ~/my-skills/*
   python3 rapp_skills.py prove ~/.brainstem/src/rapp_brainstem/agents/<their>_agent.py
   ```

   Open the `SKILL.md`. Show the learner that their code is inside it, and that `prove` said PASS:
   the file goes to a skill and back with nothing lost.
3. Run it without the Brainstem: `python3 rapp_skills.py run ~/my-skills/<name> --json '{...}'`
   with the same arguments the model used earlier. Same answer, no server.
4. Send it somewhere. Copy the folder to the place the learner's own AI tool reads skills, then ask
   that tool to use it in plain words. Or send the `SKILL.md` to a colleague; it carries its own
   launcher.
5. Back up everything:

   ```bash
   python3 rapp_skills.py to-skill ~/.brainstem/src/rapp_brainstem/agents --out ~/my-skills
   ```

   Every agent becomes a skill. Point at the folder. That folder is their portfolio.

## Done when

- `prove` printed PASS for their agent.
- The skill ran once without the Brainstem and once inside another AI tool.
- The learner has a folder of skills that is theirs.

## Teach-back

1. What is inside the `SKILL.md`, and why does that matter for sharing?
2. What did `prove` check?
3. If the Brainstem disappeared tomorrow, what would you still have?

Next: `brainstem-anywhere`.

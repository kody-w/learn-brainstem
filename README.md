# learn-brainstem

Learn how AI agents work by running one on your own machine. Give your AI these skills and it
teaches you, one concept at a time, using the RAPP Brainstem as the lab bench.

The Brainstem is a local frontier learning and rapid prototyping tool from the
[AIBAST Agents Library](https://microsoft.github.io/aibast-agents-library/). It runs the real agent loop, system prompt, tools, model,
answer, from plain Python files, powered by GitHub Copilot. Nothing to ship, no keys to manage.
What you learn graduates into GitHub Copilot, Copilot Studio, and Microsoft 365 Copilot.
[Why it exists.](https://microsoft.github.io/aibast-agents-library/why.html)

## Install

All skills, into the AI you use:

```bash
npx skills add kody-w/learn-brainstem
```

One skill:

```bash
npx skills add kody-w/learn-brainstem --skill brainstem-setup
```

Add `-g` to install for every project on your machine. This works for Claude Code, GitHub Copilot
CLI, Cursor, and anything that reads [Agent Skills](https://agentskills.io).

No installer at all: paste this into GitHub Copilot, Claude Code, Cowork, or Microsoft Scout.

```
Read https://raw.githubusercontent.com/kody-w/learn-brainstem/main/skills/learn-brainstem/SKILL.md and teach me AI with the Brainstem.
```

## The path

| Skill | You learn | Done when |
|---|---|---|
| `learn-brainstem` | Where to start | Your AI knows what you want and what you have |
| `brainstem-setup` | What an agent loop is; why no API key | Health check green, first chat answered |
| `brainstem-first-agent` | System prompts, tools, function calling, hot reload | Your own tool is called from chat |
| `brainstem-library` | Portable agents, registries, synthetic data, tests | A library agent passes its locked cases |
| `brainstem-memory` | Context versus memory, state across turns | The agent remembers across sessions |
| `brainstem-workshop` | Evidence, evals, Draft versus publish | A reviewed Draft in Copilot Studio |
| `brainstem-graduate` | Where agents live for real users | Your use case mapped to Learn, Prove, Ship |

Each skill ends with a teach-back: you explain the concept, your AI asks three questions, and
you only move on when you can answer them.

## What your AI does, and what you do

Your AI runs the terminal, writes the files, and checks the results. You read, answer, and
decide. You are asked to act only for GitHub sign-in, operating-system prompts, and choices
that are yours. Everything uses synthetic data. Nothing is ever published from Copilot Studio.

## Where the material is

- Library and front page: https://microsoft.github.io/aibast-agents-library/
- Installer: https://microsoft.github.io/aibast-agents-library/docs/installer.html
- Academy workshops: https://microsoft.github.io/aibast-agents-library/academy.html
- Production guide: https://microsoft.github.io/aibast-agents-library/docs/rapp-guide.html

## Check the skills

```bash
python3 tests/check_skills.py
```

MIT licensed. The library, its workshops, and the Brainstem are published by the AIBAST team at
Microsoft under their own license; this repository only teaches with them.

# learn-brainstem

Learn how AI agents work by running one on your own machine. Give your AI these skills and it
teaches you, one concept at a time, using the RAPP Brainstem as the lab bench.

The [Brainstem](https://kody-w.github.io/rapp-installer/) is a small local server, powered by GitHub Copilot, that runs the
real agent loop, system prompt, tools, model, answer, from plain Python files. No keys to
manage, nothing to ship. It is where you learn and prototype. What you build leaves as one
file that any AI tool can read, and can be pushed into Copilot Studio, Teams, and Microsoft 365 Copilot. [Why it is built this way.](https://github.com/kody-w/rapp-mission)

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

No installer at all: paste this into your AI.

```
Read https://raw.githubusercontent.com/kody-w/learn-brainstem/main/skills/learn-brainstem/SKILL.md and teach me AI with the Brainstem.
```

## The path

| Skill | You learn | Done when |
|---|---|---|
| `learn-brainstem` | Where to start | Your AI knows what you want and what you have |
| `brainstem-setup` | What an agent loop is; why no API key | Health check green, first chat answered |
| `brainstem-first-agent` | System prompts, tools, function calling, hot reload | Your own tool is called from chat |
| `brainstem-registry` | Portable agents, registries, checksums, provenance | A community agent installed and used |
| `brainstem-memory` | Context versus memory, state across turns | The agent remembers across sessions |
| `brainstem-share` | One file that travels; nothing lost on the way | Your agent runs as a skill somewhere else |
| `brainstem-anywhere` | Where agents live; the Brainstem as last resort | Your skill runs in a native AI tool |
| `brainstem-ship` | Harnesses; Copilot Studio, Teams, Microsoft 365 Copilot | Your skill runs in the GitHub Copilot harness, then further |

Each skill ends with a teach-back: you explain the concept, your AI asks three questions, and
you only move on when you can answer them.

## What your AI needs

A terminal, a file system, and the web: Claude Code, GitHub Copilot CLI, Cursor, or Microsoft
Scout. A chat window with no terminal cannot run the lessons. Removing everything afterwards is
one command; the entry skill has it.

## What your AI does, and what you do

Your AI runs the terminal, writes the files, and checks the results. You read, answer, and
decide. You are asked to act only for GitHub sign-in, operating-system prompts, and choices
that are yours. Learn on synthetic or throwaway data, never on someone's work data.

## Where the material is

- The Brainstem and its installer: https://kody-w.github.io/rapp-installer/
- RAR, the open registry of single-file agents: https://kody-w.github.io/RAR/
- rapp-skills, the converter and the one-file idea: https://github.com/kody-w/rapp-skills
- The charter and the fallback ladder: https://github.com/kody-w/rapp-mission
- copilot-harness-sdk, one client and one deploy for every GitHub Copilot harness: https://github.com/kody-w/copilot-harness-sdk

## Check the skills

```bash
python3 tests/check_skills.py   # structure and separation
python3 tests/check_live.py     # the installer, endpoints, registry and converter the lessons quote
```

CI runs both on every push and weekly, and files an issue if something the lessons depend on
moves. Skill versions are in each file's frontmatter; see `CHANGELOG.md`.

MIT licensed.

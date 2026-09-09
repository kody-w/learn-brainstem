---
name: brainstem-setup
description: Install the RAPP Brainstem on the learner's machine, sign in with GitHub Copilot, verify the health check, and send the first chat. Use when someone needs the Brainstem installed, started, repaired, or verified. Teaches what an agent loop is and why no API key is needed.
license: MIT
metadata:
  author: kody-w
  version: "1.1.0"
  path: brainstem-setup
---

# Set up the bench

## What the learner will understand at the end

An AI agent is a loop: a system prompt sets the rules, the model reads the conversation,
decides whether to call a tool, the tool runs, and the model answers. The Brainstem runs that
loop locally and borrows GitHub Copilot as the model, so there is no key to manage.

## Steps (you do these; the learner watches)

1. Detect the operating system and check for Python 3.11 or newer and Git. Report what is
   missing. The installer fixes most of it; say so.
2. Install:
   - macOS or Linux: `curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash`
   - Windows PowerShell: `irm https://kody-w.github.io/rapp-installer/install.ps1 | iex`
   The installer clones the source to `~/.brainstem/src`, creates a virtual environment, and
   starts the server on port 7071. When it runs through a pipe like this, the server keeps
   running in the background after the installer returns; your terminal is free.
3. If the server asks for GitHub sign-in, hand the device code to the learner. That is the one
   step they do themselves.
4. Verify: `curl -s localhost:7071/health`. Read out three things from the JSON: the model, the
   number of loaded agents, and the token state.
5. Open `http://localhost:7071` in their browser. That is the chat UI.
6. Send the first message from the terminal so they see the wire:

   ```bash
   curl -s localhost:7071/chat -H "Content-Type: application/json" \
     -d '{"user_input": "What can you do?"}'
   ```

   The answer comes back in the `response` field. `agent_logs` shows which tools ran; it is
   empty for a plain answer. Show both. On Windows PowerShell use `curl.exe`, not `curl`, which
   is an alias for something else there.

## Point at the files

- `~/.brainstem/src/rapp_brainstem/soul.md` is the system prompt. Open it. Ask the learner to
  change one line of the personality, send the same message again, and notice the difference.
  Nothing restarts; the file is read on every request.
- `~/.brainstem/src/rapp_brainstem/agents/` holds the tools. Each `*_agent.py` is one tool.

## Start, stop, and start again

- Start later: run `brainstem`. The installer put a launcher at `~/.local/bin/brainstem` on macOS
  and Linux and `brainstem.cmd` on Windows. It runs in the foreground; Ctrl-C stops it.
- Check whether one is already running: `curl -s localhost:7071/health`.
- Stop a background one: find the process listening on 7071 and end it
  (`lsof -i :7071` on macOS or Linux, `Get-NetTCPConnection -LocalPort 7071` on Windows).
- Update: rerun the install one-liner; it skips work already done.

## Done when

- `/health` returns 200 with a model name.
- One chat message answered from the terminal and one from the browser.
- The learner changed the soul file and saw the answer change.

## Teach-back

1. Where does the model run, and what credential does it use?
   A good answer: the model runs behind GitHub Copilot, not on the machine; the only credential
   is the learner's GitHub sign-in; there is no API key anywhere.
2. What file changes the agent's personality, and when is it read?
   A good answer: `soul.md`; on every request; nothing restarts.
3. What is the one endpoint everything goes through?
   A good answer: `POST /chat`, with `user_input` in and `response` out.

Next: `brainstem-first-agent`.

## If it breaks

- Port 7071 busy: another Brainstem is running; use it.
- Sign-in loops: run `curl -s localhost:7071/login/status`, then follow `/login` again.
- Anything else: `curl -s localhost:7071/diagnostics` and read the last error aloud.

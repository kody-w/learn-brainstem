---
name: brainstem-ship
description: Push the learner's skill into the Microsoft AI ecosystem with copilot-harness-sdk, one rung at a time. Run it inside the GitHub Copilot harness on their machine, deploy it as a Copilot Studio agent on the GitHub Copilot harness where the skill file is the agent's skill, reach that agent from code, and open it to Teams and Microsoft 365 Copilot. Use when someone asks how to get their agent to Copilot Studio, Teams, or Microsoft 365 Copilot, or what a harness is.
license: MIT
metadata:
  author: kody-w
  version: "1.1.1"
  path: brainstem-ship
---

# Ship it into the Microsoft AI ecosystem

## What the learner will understand at the end

The `SKILL.md` they made in `brainstem-share` is the unit that moves. The same file runs in the
GitHub Copilot harness on their machine, becomes the skill of a Copilot Studio agent that runs
on that same harness, and from there is reachable in Teams and Microsoft 365 Copilot. A harness
is the runtime that reads skills and calls tools; the file does not change, the harness does.
`copilot-harness-sdk` is one client and one deploy script for all of it: https://github.com/kody-w/copilot-harness-sdk

## What you can ship

Three inputs, one path. Decide which the learner has before choosing a rung.

- **Their own build.** The skill folder from `brainstem-share`, or any single-file agent they
  wrote or took from the registry, turned into a skill with `rapp_skills.py to-skill`. Rung 1
  runs it as is. Rung 2 wraps it in a two-file workspace, described below.
- **A ready-made solution workspace.** Industry solution libraries ship a Copilot Studio folder
  per solution, often named `copilot-studio/`, holding `settings.mcs.yml` plus `behaviors/` and
  sometimes `capabilities/`. If its settings say `template: cliagent-1.0.0` and
  `recognizer.kind: CLICopilotRecognizer`, it is a harness workspace and deploys unchanged:
  `--workspace-dir <that folder>` with `--publisher-prefix` set to the prefix already at the front
  of its `schemaName` (the part before the underscore). Display name, schema name, instructions,
  and skills come from the folder. The guard line still has to print `cliagent-1.0.0`.
- **Both.** Deploy a library solution, then add the learner's own skill as one more
  `behaviors/<name>.mcs.yml` in a copy of that folder. Their file rides inside a proven agent.

## Before you start

Each rung needs more than the last. Say which rungs the learner can do today and stop cleanly
at the first one they cannot; the earlier rungs still count.

| Rung | Needs |
|---|---|
| 0. The SDK | `git clone https://github.com/kody-w/copilot-harness-sdk`; if that returns 404 the repository is private and the learner needs access from its maintainer before any rung |
| 1. Local harness | Node 20.19 or newer, GitHub Copilot CLI installed and signed in |
| 2. Copilot Studio agent | A Power Platform environment they own, `az login`, `pac` CLI, a publisher prefix |
| 3. Reach it from code | An Entra app with the delegated permission `CopilotStudio.Copilots.Invoke` |
| 4. Teams and Microsoft 365 Copilot | Rung 3, plus the right to publish channels in that environment |

Use synthetic data throughout. Never point any of this at a customer tenant while learning.

## Rung 1. The same skill, inside the GitHub Copilot harness

1. `git clone https://github.com/kody-w/copilot-harness-sdk` then `npm install` and `npm test` in that folder. Tests need no
   network or credentials; they should pass before anything else.
2. Point the harness at the learner's skills folder from `brainstem-share` and ask for the skill:

   ```js
   import { HarnessClient } from './copilot-harness-sdk/index.js';
   const client = await HarnessClient.create({ mode: 'copilot-sdk',
     copilotSdk: { model: 'auto', permissions: 'approve-all', skillDirectories: ['<their skills folder>'] } });
   const session = await client.createSession({ sessionId: 'learn-' + Date.now() });
   for await (const ev of session.stream('Use the <skill name> skill: <the same request as before>')) {
     if (ev.type === 'tool.start') console.log('tool', ev.name);
     if (ev.type === 'text.final') console.log(ev.text);
   }
   await client.close();
   ```

3. Show the event stream: `tool.start skill` is the harness loading their file, then whatever the
   skill's launcher ran, then the answer. Same answer as the Brainstem gave; different runtime.
4. Change `permissions` to `'emit'` and run again. Every shell or file action now arrives as a
   `permission.request` the learner must approve. That is what a harness owes its user.

## Rung 2. A Copilot Studio agent whose skill is that file

Copilot Studio agents come in two kinds. Only the **GitHub Copilot harness** kind reads skills;
the SDK's deploy script refuses to create the other kind. Its skill component is a YAML file
whose `content` is a `SKILL.md`, byte for byte.

1. Make a workspace folder with two files.
   `settings.mcs.yml`: copy `usecases/vendor-contract-renewal/agent/settings.mcs.yml` from the
   SDK and change `displayName` (42 characters or fewer, longer never finishes provisioning),
   `schemaName` (`<prefix>_<Name>`), the `instructions` text, the greeting, and the starters.
   Keep `template: cliagent-1.0.0` and `recognizer.kind: CLICopilotRecognizer`; those make it a
   harness agent. Write one instruction line: "When asked for <what the skill does>, follow the
   <skill name> skill exactly."
   `behaviors/<skill name>.mcs.yml`:

   ```yaml
   mcs.metadata:
     componentName: "<skill name>"
     description: "<the skill's description line>"
   kind: InlineAgentSkill
   content: |
     <the learner's SKILL.md, indented two spaces, unchanged>
   ```

2. Sign in and deploy:

   ```bash
   az login
   pac auth create --deviceCode --environment https://<org>.crm.dynamics.com/
   npm run deploy:harness -- --workspace-dir ./workspace --name "<display name>" \
     --publisher-prefix <prefix> --environment https://<org>.crm.dynamics.com/
   ```

   `pac auth create` prints a device code; the learner signs in with it, the one step that is theirs.
   The script packs the solution, refuses the zip unless it is the harness template, imports,
   writes the instructions onto the live record, publishes, and reads the record back. Show the
   final verification line: template, recognizer, model, instruction length.
3. Open the agent in Copilot Studio. Under Skills the learner's file is there. Ask it in the
   test pane for the same thing as rung 1.

## Rung 3. Reach it from code, one normalized stream

1. In Copilot Studio set the agent to **Authenticate with Microsoft**, publish, and share it
   with the learner's own user.
2. From the SDK:

   ```js
   import { HarnessClient, createDeviceCodeTokenProvider, assertHarnessAgent } from './copilot-harness-sdk/index.js';
   const client = await HarnessClient.create({ mode: 'copilot-studio-3p', copilotStudio: {
     environmentId: process.env.COPILOT_ENVIRONMENT_ID, schemaName: '<prefix>_<Name>',
     getAccessToken: createDeviceCodeTokenProvider({ clientId: process.env.ENTRA_CLIENT_ID, tenantId: process.env.ENTRA_TENANT_ID }) } });
   await client.preflight();
   ```

   Same `session.stream` loop as rung 1. Point out that no `tool.start` arrives now: the
   Studio agent runs its skill server-side. The text events are identical in shape.
3. Run `assertHarnessAgent` against the live record with `requirePublished: true`. It throws
   `ClassicAgentError` for anything that is not the harness. That is the check to keep.

## Rung 4. Teams and Microsoft 365 Copilot

```js
import { setChannels, shareAgent } from './copilot-harness-sdk/index.js';
await setChannels({ environmentUrl, schemaName, getDataverseToken,
  channels: ['Teams', 'Microsoft365Copilot'] });
await shareAgent({ environmentUrl, schemaName, getDataverseToken, userId });
```

Then `pac copilot publish`. The learner opens Microsoft 365 Copilot or Teams and asks their
agent the same question a fourth time. Four runtimes, one file.

## Done when

- Rung 1: `tool.start skill` appeared and the answer matched the Brainstem's.
- Rung 2, if reachable: the deploy's verification line shows `cliagent-1.0.0` and the skill is
  listed under Skills in Copilot Studio.
- Rung 3 and 4, if reachable: the same question answered from code and from Teams or
  Microsoft 365 Copilot.

## Teach-back

1. What is a harness, and what did the file have to change to move between them?
   A good answer: the runtime that reads skills and runs tools; the file did not change at all.
2. Why did `tool.start` disappear in rung 3?
   A good answer: the Copilot Studio agent runs its tools and skills server-side; the client
   only sees text.
3. Why does the deploy script refuse one kind of Copilot Studio agent?
   A good answer: the classic kind does not read skills and cannot be converted in place.

That is the end of the path. Everything the learner built is one file, and it is now in four places.

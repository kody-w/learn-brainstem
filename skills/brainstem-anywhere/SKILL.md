---
name: brainstem-anywhere
description: Show the learner where an agent actually lives once it works, using the fallback ladder from rapp-mission, and run their skill in a native AI tool. Use when someone asks "how do I ship this", "what's next", or where agents run for real. Teaches that native platforms come first, the file second, and the Brainstem is the last resort.
license: MIT
metadata:
  author: kody-w
  version: "1.1.0"
  path: brainstem-anywhere
---

# Where it lives

## What the learner will understand at the end

The ladder, from https://github.com/kody-w/rapp-mission: use the native platform first, wherever the learner and their
users already are; carry the file when the platform cannot do it yet; run the Brainstem only
as the last resort, when nothing native exists. The Brainstem taught them the pattern. The
skill is what they keep.

## Steps

1. Read the charter with the learner: https://github.com/kody-w/rapp-mission. Ask them to say the ladder back in one
   sentence.
2. Take the skill from `brainstem-share` and run it in the AI tool they use every day. rapp-skills
   documents the folders for Claude Code and GitHub Copilot CLI; anything that reads Agent Skills
   works the same way. Ask the tool for the skill in plain words and show it answering.
3. Compare: the same skill answered from the Brainstem, from `rapp_skills.py run`, and from the
   native tool. Point out what changed (nothing) and what did (where it ran).
4. If they need it running for other people, the Brainstem installer's own README covers the
   cloud path: https://kody-w.github.io/rapp-installer/. Do not install it now. Explain when you would.
5. Ask the learner for one real thing from their life or work that they want an agent for.
   Write, with them, which rung it belongs on and why. That paragraph is the deliverable.
6. Send them back to `brainstem-first-agent` with that use case. The loop starts again, faster.

## Done when

- The learner's skill answered from a native AI tool.
- They can say the ladder unprompted and place their own use case on it.
- They know the Brainstem is where they learn and prototype, not where things live.

## Teach-back

1. Why is the Brainstem the last rung and not the first?
   A good answer: native tools already run the loop; the Brainstem is for when nothing native exists.
2. What stays the same when a skill moves from the Brainstem to a native tool?
   A good answer: the file and what it does; only where it runs changes.
3. What would make you climb back down a rung?
   A good answer: no platform, no network, or no account for what you need.

That is the whole path. Start it again with their own use case.

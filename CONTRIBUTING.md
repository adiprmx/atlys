# Contributing to atlys

Thanks for wanting to add to the collection. atlys is curated, not comprehensive —
every skill has to earn its place. This guide tells you exactly what that takes.

## The bar

Before writing anything, read **"The bar"** in the main README. In short:

- **Real substance.** A skill must be genuinely useful on its own. Thin stubs
  get closed. The collection averages ~12k characters per `SKILL.md` — that's
  the neighborhood you're aiming for, not a requirement, but a 500-character
  file won't make it.
- **Non-generic.** If an LLM could have written it from the prompt "write a
  skill about X" with no added insight, it doesn't belong here. What's your
  angle? What do you know that the model doesn't?
- **Human-voiced.** No AI-slop: no emoji soup, no hype adjectives, no filler
  transitions. Write like a person who respects the reader's time.

## How to submit a skill

1. **Open an issue first** (or use the skill-request template) if you're unsure
   the skill fits — saves us both time.
2. **Fork, add, PR.** Your PR adds one folder under the right category:
   `design/`, `writing/`, or `engineering/`.

### Folder layout

```
<category>/<skill-name>/
  SKILL.md      # the skill itself — frontmatter + substance
  skill.yaml    # metadata, in sync with SKILL.md frontmatter
  README.md     # scope quote, "When to use", annotated contents, install command
```

### SKILL.md

- Starts with frontmatter — `name` and `description` are **mandatory**.
  The validator rejects the PR without them.
- `name` uses dashes, lowercase: `taste-skill`, not `TasteSkill`.
- `description` is one or two sentences, plain language.

### skill.yaml

Keep it in sync with the `SKILL.md` frontmatter (name, description, version).
See any existing skill for the exact shape.

### README.md

Follow the collection's format:

- A scope quote — what this skill covers, in one line.
- **When to use** — concrete situations, hand-written, not templated.
- **Contents** — annotated, so readers know what's inside before installing.
- Install command: `npx skills add adiprmx/atlys -s <skill-name> -y`
- If adapted from external work: credit the source with a link, and note the
  original license. (See Attribution in the main README.)

## Authoring a skill that passes

1. **Start from a real problem** you've actually hit, not a topic you find
   interesting. The best skills read like field notes.
2. **Write the "When to use" first.** If you can't name three concrete
   situations, the skill isn't ready.
3. **Show, don't list.** Rules with examples beat bullet points of abstractions.
   Before/after pairs are gold.
4. **Cut ruthlessly.** Every paragraph should survive the question "would a
   busy practitioner miss this if it were gone?"
5. **Read it out loud.** If it sounds like a model wrote it, rewrite it.

## Validation

Run this before opening the PR — CI runs the same check and it must pass:

```sh
python3 tools/validate.py
```

It verifies frontmatter on every skill, per-category counts, badge accuracy,
and that all relative links resolve. Fix everything it flags.

Also confirm the skill installs:

```sh
npx skills add adiprmx/atlys -s <skill-name> -y
```

## What happens after you submit

- The PR template checklist is your friend — fill it in, it speeds up review.
- Expect review on substance and voice, not just format.
- Small fix requests are normal. Large rewrites mean the skill wasn't ready;
  take it back, rework, resubmit.

## Code of Conduct

Be kind. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

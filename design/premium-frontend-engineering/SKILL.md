---
description: 'Hand-coded frontend: brief-driven design dials, bias-corrected typography
  and color, intentional GSAP/Motion choreography, strict pre-flight check.'
name: premium-frontend-engineering
---

# Premium frontend engineering

## Read the brief and set the dials

- State a one-line design read before touching code: page kind, audience, vibe language, and the design system or aesthetic family you are leaning toward. Ask exactly one clarifying question only when the read genuinely diverges.

- Set design variance, motion intensity, and visual density from the read and gate every layout, motion, and density decision on them. Roll the variance engine silently and commit to one vibe archetype and one layout archetype per project, never the same output twice in a row.

- Reach for a real design system when the brief matches one and use its official package. Otherwise build with native CSS plus Tailwind, one icon family per project, and verified dependencies from package.json.

## Correct the default biases

- Replace the LLM defaults: distinctive fonts instead of Inter, one accent under 80 percent saturation, shadows tinted to the background hue, generous macro whitespace, and a single corner-radius scale. Never ship AI-purple gradients, centered dark heroes, or three equal feature cards by default.

- Diversify layout with asymmetric bento grids, editorial splits, or stacked storytelling, and vary composition so no layout family repeats on the page. Keep one theme across all sections.

- Ship full interaction cycles: loading skeletons, composed empty states, inline errors, tactile active feedback, and WCAG AA contrast on every button and form. Keep every CTA label on one line and one label per intent.

## Choreograph motion with intent

- Use real GSAP ScrollTrigger for pinning, stacking, and horizontal scrubbing, or Motion whileInView for simple reveals. Never drive animation from window scroll listeners or React state, and never animate top, left, width, or height.

- Apply spring physics and custom cubic-bezier curves, stagger list entries, and keep every animation communicating hierarchy, story, or feedback. If an animation has no one-sentence reason, drop it.

- Honor prefers-reduced-motion for anything above static and collapse heavy effects to static when motion cannot be built well. Keep blur and grain on fixed pointer-events-none layers only.

## Verify before shipping

- Run the pre-flight: hero fits the first viewport with a headline of at most two lines, navigation renders on one line, bento cell counts match content, eyebrows are capped at one per three sections, and no zigzag image-text split runs three sections in a row.

- Confirm mobile collapse below 768px with no horizontal scroll, min-h-100dvh instead of h-screen, grid instead of flex percentage math, and 44px minimum touch targets.

- Re-read every visible string and rewrite anything grammatically broken, vague, or AI-cute. Prefer real generated images over div-faked screenshots, and real SVG brand logos over text wordmarks in logo walls.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- When the user needs design reference images before code, generate them first with `local_frontend_image_direction` and implement from the references.

- When upgrading an existing site rather than building new, audit it first with the redesign skill and fix in place.
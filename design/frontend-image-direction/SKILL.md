---
description: Section references, mobile screen concepts, and brand-consistent image
  sets with locked cross-image consistency, then implements from the references without
  design drift.
name: frontend-image-direction
---

# Frontend image direction

## Lock the design direction first

- Read the brief and set the dials: design variance, visual density, art direction, implementation clarity, and spacing generosity. Adapt them from the user's words and keep them as global variables for every later decision.

- Pick one coherent combination and commit to it: theme paradigm, background character, typography character, hero architecture, section system, exactly four signature components, and two motion-implied cues. Never mash options together.

- Vary composition across the page and never reach for the left-text right-image hero by default. Consider centered, bottom-left over image, stacked center, image-as-canvas, off-grid editorial, or inverted classic first.

## Generate one image per unit

- Generate one separate horizontal image per website section and one image per mobile screen. Never collapse multiple sections into one frame, one tall slice, or one collage.

- Announce each unit as you go and keep generating sequentially until the count matches the request. Default high when the count is ambiguous: landing page means 6 images, full website means 8.

- Prefer fresh standalone generation over cropping. When a section needs a detail view, generate a new clean image in the same design language instead of zooming or cutting into an old one.

## Enforce cross-image consistency

- Lock an internal design bible before generating more than one image: palette logic, typography mood and scale, spacing system, corner radius logic, icon style, image treatment, CTA styling, and texture intensity.

- Keep every later image in the same product world. Vary composition and visual tempo across the set, never identity, palette, or spacing logic.

- Run the clarity check before finalizing: obvious hierarchy, distinctive design, no AI tells, breathable spacing, and the image count exactly matching the request.

## Direct each channel's craft

- For websites: keep the hero cinematic and clean with a short headline of one to three lines, use confident backgrounds matched to the palette, keep a single disciplined palette across all frames, and make every reference readable enough for a developer to build from.

- For mobile: present screens inside a clean phone mockup with even margins and content as the hero, respect safe areas and real navigation patterns, keep text comfortably readable at phone size, and make multi-screen sets a logical believable flow.

- For image-to-code work: generate the reference images first, then deeply analyze and extract text, typography, spacing, buttons, colors, and layout logic from each image. Implement the frontend to match the references closely and never drift into generic coded layouts during implementation.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- When the user wants real interactive UI rather than reference images, implement directly in code with `local_premium_frontend_engineering`.

- When the task is a brand identity board rather than screens or sections, use the brandkit skill instead.
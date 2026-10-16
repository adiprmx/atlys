

# Intent Pattern QA

## Purpose
Verify regex intent patterns actually match real queries — `re.compile` passing is necessary but never sufficient, because several silent-death classes compile cleanly yet never match.

## Workflow
1. After authoring or modifying any intent batch, run the silent-death checklist on every pattern before the batch may be called verified:
   - **H1 — Uppercase literals dead.** Input is lowercased by `_normalize` before `_score`, so any literal uppercase outside a character class never matches. Write all literals lowercase; keep uppercase only inside `[...]`.
   - **H2 — `\A` guard without `.*`.** A pattern beginning `\A(?!...)` or `\A(?<!...)` with no `.*` in the first 40 chars pins the keyword to position 0 and dies on any query that does not start with it. Require `.*` immediately after the guard: `\A(?!.*\bGUARD\b).*`.
   - **H3 — Backslash corruption via `re.subn`.** A string replacement turns `\b` into byte `0x08`, killing the pattern silently. Build replacements with a function (`lambda m: ...`), never a string, and assert `chr(8) not in` the output.
   - **H4 — Newline injection from guard constants.** Guard constants defined as multi-line raw strings inject literal `0x0A` into every concatenated pattern. Keep guard constants single-line; assert `"\n" not in` every pattern.
2. Run **dynamic positive-match probes**: feed 2–3 realistic positive queries per pattern through the production `_score` path (not a standalone regex test) and require at least one hit. Zero hits on its own positive probes means silent-dead — fix or drop the pattern.
3. Run byte-level asserts over the final batch files: no `chr(8)`, no newline inside patterns, no uppercase literals outside character classes.

## Output Contract
- Per-batch QA report: pattern count, positive-probe hit rate, silent-dead patterns found and how each was fixed, byte-assert results.
- A batch is never reported "verified" on compile-only evidence.

## Operating Rules
1. `re.compile` PASS is a pre-check, never the verification.
2. Probe through the production scoring path — normalization, guards, and tie-breaks only exist there.
3. When verification discovers a new silent-death class, log it in the batch report with probe evidence so the improvement loop can fold it into the H-checklist above.
4. Quote probe queries and hit counts in the report — numbers with method, never bare claims.
## Available connectors

Use `muse.connector_search` to find the current connector docs before following
recovered instructions.

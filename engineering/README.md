# ⚙️ Engineering & QA

4 skills for reliable, complete, well-resourced agent work.

| Skill | What it does |
|---|---|
| `local-output-skill` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. |
| `local-intent-pattern-qa` | Catches silent regex-pattern death — patterns that compile but never match — via positive-match probes and byte-level asserts. |
| `local-batch-run-integrity` | Keeps long multi-chunk batch jobs honest and resumable: incremental on-disk checkpoints, completion claims reconciled against artifacts on disk. |
| `local-worker-resource-budgeting` | Budgets RAM before fanning out parallel workers, so verification workers never starve the live system. |

← Back to [atlys](../)

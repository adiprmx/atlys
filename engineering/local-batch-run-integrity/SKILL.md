

# Batch Run Integrity

## Purpose
Keep long multi-chunk batch jobs (serapan runs, tumpah-ilmu runs, mining waves) resumable after runtime kills and keep every progress claim honest, by checkpointing to disk and reconciling claims against artifacts instead of counters.

## Workflow
1. **Checkpoint per chunk.** Before starting chunk N+1, append chunk N's durable output to a progress file on disk (chunk id, artifact paths, counts). A run killed mid-way resumes from the last checkpointed chunk — completed chunks are never redone or lost.
2. **Reconcile claims against artifacts.** Any completion claim ("X intents in Y batches") is verified by listing artifacts on disk with `muse.read` — batch files present, intent counts parsed from the files themselves — never by trusting in-memory counters or coordinator summaries. Missing files mean the claim is false: report the shortfall honestly and salvage what exists.
3. **Re-verify race-sensitive allocations at deploy time.** ID ranges, label pools, and dedupe horizons are re-checked against live production state immediately before deploy, not trusted from draft-time notes — a concurrent run may have claimed the same range in between. On collision, re-allocate before writing.
4. **Verify against pristine production.** Run dedupe/verification probes with the new batch files moved out of the production tree, then copy them in. Probing after the copy produces self-dedupe false FAILs.

## Output Contract
- Progress file on disk, updated per chunk; the run is resumable after kills.
- Completion report cites artifact counts read from disk, with any shortfall stated plainly.
- Deploy report cites the deploy-time re-verification (max ID, dedupe) with timestamps.

## Operating Rules
1. No progress file, no claim of progress — a run with only in-memory state has produced nothing durable.
2. Counters are claims; files are evidence. Reconcile the two before every handoff.
3. Draft-time allocations expire at deploy time — re-verify, then write.
4. Report shortfalls honestly — an honest ugly number beats a pretty fake one.
## Available connectors

Use `muse.connector_search` to find the current connector docs before following
recovered instructions.

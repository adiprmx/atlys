

# Worker Resource Budgeting

## Purpose
Stop parallel verification workers from starving the live bot of RAM — each worker that loads the full intent brain costs 400–700 MB, and a handful of them can kill the bot at startup.

## Workflow
1. Before fanning out N parallel workers that load the full brain (verification, dedupe, probes, `check_otak`), check free memory with `muse.exec` (`free -g`). Reserve 2 GB headroom for the bot and OS; the rest is the worker budget.
2. Cap concurrency at `budget / 700 MB` (worst-case per-worker RSS). When headroom is tight, run workers sequentially instead of in parallel.
3. For dedupe-only or name-list tasks, spawn slim workers that load only a hash set of names/labels — never the full pattern brain.
4. Before any deploy or restart, finish or throttle heavy workers first; never restart the bot while verification workers are still holding gigabytes.
5. After a platform reboot, verify the bot is up and healthy before spawning any heavy workers — post-reboot is the highest-risk window.

## Output Contract
- Fan-out plan states: free RAM observed, per-worker estimate, worker count chosen, headroom reserved.
- No silent worker spawns during deploy/restart windows.

## Operating Rules
1. The live bot's RAM is non-negotiable — workers are expendable, the bot is not.
2. `check_otak`-class jobs are CPU-heavy: never run two concurrently, and never alongside an active brain-building run.
3. If free RAM drops below 1 GB mid-run, stop spawning and throttle existing workers before the OOM killer decides for you.
## Available connectors

Use `muse.connector_search` to find the current connector docs before following
recovered instructions.

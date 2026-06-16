# Job Applications Workflow — Handoff to Claude Code

**Context:** This was set up via Claude (web chat) on 2026-06-15. Handing over to Claude Code for ongoing maintenance, debugging, and feature additions.

---

## What This Is

A workflow for tracking job applications, with Obsidian as the source of truth and a sync script that exports to this directory (`E:\job_applications\jobsearch\`).

**Note:** Career-ops (the previous job search tool/repo) has been retired. This is a fresh, lightweight, custom setup — not connected to career-ops in any way.

---

## Architecture

```
X:\Vault\Hatch\                          (Obsidian vault — SOURCE OF TRUTH)
├── _templates/
│   └── Job Application Template.md      ← template for new job notes
├── job-hunt/
│   ├── Job Applications Board.md        ← Dataview kanban (4 statuses)
│   ├── [Company] - [Role].md            ← individual job application notes
│   └── ...

E:\job_applications\jobsearch\           (THIS DIRECTORY — sync target)
├── sync_jobs.py                         ← Python sync script
├── applications.md                      ← generated summary (markdown)
└── applications.json                    ← generated summary (JSON)
```

---

## How It Works

1. User adds/edits job application notes in Obsidian (`job-hunt/` folder), each with YAML frontmatter (see schema below)
2. User views progress via a Dataview kanban board in Obsidian, grouped by `status`
3. When ready, user runs `python sync_jobs.py` from this directory
4. Script reads all `.md` files in `X:\Vault\Hatch\job-hunt\` (except the board file itself), parses frontmatter, and generates:
   - `applications.md` — human-readable summary grouped by status, sorted by deadline
   - `applications.json` — structured export with status counts + full application list

---

## YAML Frontmatter Schema (per job note)

```yaml
---
status: Interesting        # Interesting | To Apply | Applied | Response
company: 
role: 
url:                        # CRITICAL — must be a real, verifiable, current job posting
posting_date:               # YYYY-MM-DD — used to filter stale postings
deadline:                   # YYYY-MM-DD — kanban sorts by this
key_requirements:           # free text — skills/tools for fit assessment
sector:                     # optional, e.g. VFX, games
team_size:                  # optional — user prefers small teams
salary:                     # optional, if listed
type: posted                # posted | cold-call
date_found: 2026-06-15      # YYYY-MM-DD
---
```

**Kanban pipeline (in order):** Interesting → To Apply → Applied → Response

---

## Known Issue Already Fixed

YAML auto-parses unquoted dates (e.g. `date_found: 2026-06-15`) into Python `date` objects, which `json.dump()` can't serialize by default. This caused a `TypeError: Object of type date is not JSON serializable` on first run.

**Fix applied (already in `sync_jobs.py`):**
- Added `json_serial()` helper that converts `date`/`datetime` objects to ISO strings via `default=json_serial` in `json.dump()`
- Also normalized all date-like frontmatter values to ISO strings immediately after YAML parsing (in `extract_frontmatter()`), so sorting by deadline doesn't mix `date` objects and strings

If you see similar `TypeError` issues with other fields, the same normalization pattern (convert in `extract_frontmatter()`) is the right place to fix it.

---

## Dependencies

- `pyyaml` (only external dependency)
- User was advised to optionally use a venv in this folder — may or may not have set one up. Check for `venv/` before assuming global install.

---

## User's Priorities / Preferences (for context)

- **Critical:** Real, verifiable, current job URLs — avoid stale postings wasting time
- Prefers small teams
- Currently focused on Dublin-area creative technologist / motion design / full-stack roles (see profile: 15+ years motion design/animation, Disney+/Cartoon Saloon/Science Gallery credits, full-stack React/Node/PostgreSQL, CNC/manufacturing automation background)
- Wants minimal overhead — no cron jobs, no over-engineering. Manual sync is fine for now
- Eventually wants: URL verification step (check postings are live/recent), fit assessment, tailored CV/cover letter drafting — but these are NOT built yet, just noted as future workflow steps

---

## Possible Next Steps (not yet built)

- [ ] URL liveness/freshness check (could be a separate script — would need web fetch capability)
- [ ] Fit-scoring against user's CV/profile
- [ ] CV/cover letter generation per application
- [ ] Individual `.md` file exports per job (currently single summary file only, by user's choice)
- [ ] `.bat` wrapper for one-click sync (mentioned, not confirmed built)
- [ ] venv setup (mentioned, not confirmed built)

---

## Files in This Handoff

- `sync_jobs.py` — the sync script (tested, working after date fix)
- This handoff doc

Template file (`Job Application Template.md`) and setup guide were delivered separately and should already be in the vault — verify they exist at:
- `X:\Vault\Hatch\_templates\Job Application Template.md`
- `X:\Vault\Hatch\job-hunt\Job Applications Board.md`

If either is missing, recreate from this handoff's schema above.

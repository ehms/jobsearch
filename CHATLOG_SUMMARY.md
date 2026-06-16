# Chat Session Summary - Job Search Automation Build

**Session:** 2026-06-15 to 2026-06-16  
**User:** Shem Shortall  
**Goal:** Build comprehensive, automated job search system

## Key Decisions Made

1. **Search Strategy**
   - Expanded from 5 to 16 job categories to surface adjacent roles
   - Added "dark horse" fields (Game Designer, Concept Artist, etc.) for variety
   - Strict mid-level filter (3-6 years), Dublin/Remote EU only
   - Exclude Senior/Lead/Principal roles (user preference)

2. **Automation Approach**
   - Cloud-based scheduled routine (9am daily) — independent of local terminal
   - Local sync script for Obsidian vault integration
   - Manual triggers (`/parse`, `/cold-call`) for evaluation and outreach
   - Balance: automated discovery + manual decision-making

3. **Storage & Sync**
   - GitHub repo (github.com/ehms/jobs) for cloud agent output
   - Local Obsidian vault for job tracking and cold-calls
   - PowerShell sync script bridges the two without git-backing vault

4. **Cold-Call System**
   - Identified 4 target companies (Windmill Lane, Brown Bag Films, Void Interactive, Lifesize Plans)
   - Lifesize Plans Ireland contacted (LIDAR scanning angle, pending response)
   - `/cold-call [Company]` command drafts personalized emails

## Why Each Choice Was Made

| Decision | Why |
|----------|-----|
| Cloud agent vs local cron | Reliable, scales, no terminal needed, built-in cloud infrastructure |
| 16 categories | Broader funnel to surface adjacent roles user qualifies for |
| Dark horse fields | Prevents repetitive search, keeps discovery interesting |
| Local sync script (not git vault) | Simpler setup, avoids Obsidian git complexity, works great |
| Manual `/parse` trigger | Lets user batch-review jobs on their schedule, not push notifications |
| `/cold-call` command | Quick outreach drafting without needing full application setup |

## What Was Discovered

- Mid-level job market for Technical Artist/Motion Designer in Dublin is thin right now
- Most Dublin studios hiring Senior/Lead roles (backfill opportunities likely coming)
- Web scraping can hit rate limits (rotated schedule handles this)
- Obsidian + git sync is optional; local sync script is simpler for this workflow

## Files Created

- `CLAUDE.md` — Full project context (already existed)
- `search-queries.md` — 16 job categories (updated)
- `job-urls.md` (in Obsidian) — Single source of truth for jobs + cold calls
- `job-queue.md` — Lightweight discovery format (not used in final approach)
- `cold-call-targets.md` — Cold-call tracking (superseded by tagging in job-urls.md)
- `sync-job-urls.ps1` — Local sync script (PowerShell)
- `sync-urls.bat` — Sync wrapper (double-click runner)
- `parse.bat` — Job parser wrapper
- `parse_urls.py` — Job posting parser (updated for #coldcall filtering)
- `.claude/settings.json` — WebFetch permission enabled

## Open Questions / Future Work

- **Windows Task Scheduler**: Could auto-run sync script on schedule (optional)
- **Obsidian git-backing**: Could add for vault backup (optional, not critical)
- **Interview prep**: Could integrate with interview preparation system
- **Application tracking**: Could add status field in job-urls.md (Interesting → Applied → Rejected/Interview)

---

**Session Status: COMPLETE**  
**Next Session:** Cloud job search will have accumulated URLs. Run `/parse` to see results.

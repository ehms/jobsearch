# Session Context - Job Search Automation

**Last Updated:** 2026-06-16
**Status:** All systems operational

## Active Workflows

### ✅ Daily Cloud Job Search (Running)
- **Schedule:** 9am Dublin time (8am UTC) every day
- **Routine ID:** trig_01NM6JCSgeTfpQ4AEyaCsDM2
- **Repo:** https://github.com/ehms/jobs
- **Output:** `jobs/urls.md` with new job URLs
- **Status:** No action needed - runs automatically in cloud
- **View at:** https://claude.ai/code/routines/trig_01NM6JCSgeTfpQ4AEyaCsDM2

### ✅ Local URL Sync Script (Manual)
- **Script:** `sync-urls.bat` (double-click to run)
- **Function:** Pulls jobs repo → merges new URLs into Obsidian `job-urls.md`
- **Frequency:** Run manually anytime, or after cloud agent runs
- **Clone location:** `C:\repos\jobs`

### ✅ Job Parsing & Evaluation
- **Command:** `/parse`
- **Function:** Extracts job details from URLs in Obsidian `job-urls.md`
- **Output:** `parsed-jobs.md`

### ✅ Cold-Call Outreach
- **Command:** `/cold-call [Company Name]`
- **Function:** Drafts personalized outreach emails
- **Target Companies:** Windmill Lane, Brown Bag Films, Void Interactive, Lifesize Plans Ireland
- **Status:** Lifesize Plans already contacted

## Available Commands

| Command | Purpose |
|---------|---------|
| `/parse` | Extract job details from job-urls.md |
| `/cold-call [Company]` | Draft outreach email for company |
| `/sync` | Run local URL sync (via sync-urls.bat) |

## Job URLs Format (Obsidian)

```markdown
## Job Postings (to parse with /parse)
- [URLs added by sync script]

## Cold-Call Targets
- Company Name #coldcall | reason
```

## Key Files

- `CLAUDE.md` — Full project context & candidate profile
- `JOB_URLS_FORMAT.md` — Format guide for job-urls.md
- `job-alerts-setup.md` — How to set up LinkedIn/Indeed alerts
- `sync-job-urls.ps1` — Local sync script (PowerShell)
- `sync-urls.bat` — Sync wrapper (double-click to run)

## Notes for Next Session

- Everything is automated and running
- No immediate action needed
- Check Obsidian `job-urls.md` to see synced URLs
- Run `/parse` to evaluate jobs
- Add cold-call targets with `#coldcall` tag to trigger email drafting

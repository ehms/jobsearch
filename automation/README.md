# Job Capture Automation

Automatically convert job emails into markdown files ready for the `/apply` workflow.

## Quick Start

### Choose your method:

| Method | Effort | Cost | Features |
|--------|--------|------|----------|
| **Google Apps Script** | 5 min | Free | Built-in, runs hourly, syncs to Google Drive |
| **Python Script** | 10 min | Free | Local control, runs on-demand or scheduled |
| **Zapier** | 10 min | Free tier / $29+/mo | Easiest setup, cloud-based |

---

## 1. Google Apps Script (Recommended for beginners)

**Best for:** Non-technical users, minimal setup, free tier

1. Go to **[SETUP_EMAIL_CAPTURE.md](SETUP_EMAIL_CAPTURE.md)** → "Option 1"
2. Follow the 5-minute setup
3. Star + label emails as `job-leads` in Gmail
4. Script runs hourly, files appear in Google Drive
5. Sync to laptop with Google Drive for Desktop

**File:** `google-apps-script-job-capture.gs`

---

## 2. Python Script (Best for control)

**Best for:** Developers, running locally, Windows Task Scheduler integration

1. Go to **[SETUP_EMAIL_CAPTURE.md](SETUP_EMAIL_CAPTURE.md)** → "Option 2"
2. Install dependencies and set up Gmail API
3. Run: `python job-email-capture.py`
4. Files appear directly in `jobs/prospective/`

**File:** `job-email-capture.py`

---

## 3. Zapier (Easiest integration)

**Best for:** Cloud automation, connecting to other apps (Slack, Notion, etc.)

1. Go to **[SETUP_EMAIL_CAPTURE.md](SETUP_EMAIL_CAPTURE.md)** → "Option 3"
2. Set up Zapier workflow (5 min)
3. Create new Zap: Gmail → Google Drive

---

## Testing

After setup, send yourself a test email:

**Subject:** `Test: Senior Backend Engineer at ACME Corp`

Then:
1. Star it
2. Add label `job-leads`
3. Wait for script to run (or run manually)
4. Check output folder for the markdown file

---

## File Format

Captured emails are converted to this template:

```markdown
---
company: "ACME Corp"
role: "Senior Backend Engineer"
url: ""
posted: "2026-06-12"
salary: "Not listed"
location: "See email"
source: "Email from jobs@acme.com"
---

# ACME Corp - Senior Backend Engineer

[Email content here]

## My Notes

- [ ] Read full description
- [ ] Self-assess fit
- [ ] Ready to apply
```

Edit the metadata (company, role, url, salary, location) if needed, then run:

```bash
/apply jobs/prospective/[filename].md
```

---

## Workflow

```
You receive job email
    ↓
Star + label it "job-leads"
    ↓
Script runs (hourly or on-demand)
    ↓
Markdown file created in jobs/prospective/
    ↓
Synced to your laptop
    ↓
When ready: /apply jobs/prospective/company_role.md
    ↓
Full application workflow (fit eval, CV, cover letter)
```

---

## Troubleshooting

**Script not running?**
- Check that the `job-leads` label exists in Gmail
- Verify the trigger is set up (Apps Script → clock icon)
- Check the script's execution log for errors

**Files not appearing?**
- Make sure you labeled the email with `job-leads` (case-sensitive)
- Check that the Google Drive folder ID is correct
- Try running the script manually (click "Run")

**Duplicates?**
- The script adds a `job-leads/processed` label to prevent re-processing
- If duplicates appear, check that the label was applied

**Python script not working?**
- Ensure `credentials.json` is in this directory
- Run `python job-email-capture.py` from the command line to see error messages
- First run opens a browser for OAuth - follow the prompts

---

## Advanced: Schedule Python script on Windows

To run the Python script automatically every hour on Windows:

1. Open **Task Scheduler**
2. Click "Create Basic Task"
3. Name: "Capture Job Emails"
4. Trigger: "Daily" at your preferred time
5. Action: Start a program
   - Program: `C:\Users\[YOUR_USER]\AppData\Local\Programs\Python\Python310\python.exe`
   - Arguments: `C:\path\to\job-email-capture.py`
6. Click OK

Or use a batch file:

```batch
@echo off
cd E:\job_applications\jobsearch\automation
python job-email-capture.py
```

Save as `capture-jobs.bat` and schedule it.

---

## More info

- `google-apps-script-job-capture.gs` — Google Apps Script source code
- `job-email-capture.py` — Python script source code
- `SETUP_EMAIL_CAPTURE.md` — Detailed setup instructions for all methods

# Email-Based Job Capture Setup

Automatically convert job emails into markdown files in `jobs/prospective/`.

## Option 1: Google Apps Script (Recommended - Free & Built-in)

### Setup (5 minutes)

1. **Create a Gmail label:**
   - In Gmail, click the label icon on the left sidebar
   - Click "Create new label"
   - Name it `job-leads` (case-sensitive)

2. **Open Google Apps Script:**
   - Go to [script.google.com](https://script.google.com)
   - Click "New project"
   - Copy the code from `google-apps-script-job-capture.gs` below
   - Paste it into the editor
   - Click "Save" (name it "Job Email Capture")

3. **Set up Google Drive folder:**
   - Create a folder in Google Drive called `job-prospective` (or whatever you prefer)
   - Open the folder and copy its ID from the URL: `folders/[FOLDER_ID]`
   - In the script, replace `FOLDER_ID = "your-folder-id-here"` with your actual ID

4. **Authorize the script:**
   - Click "Run" → select the function `captureJobEmails`
   - Click "Review permissions" and authorize the script to access Gmail and Drive
   - (It will fail the first run with no emails, that's expected)

5. **Set up a trigger:**
   - In the Apps Script editor, click the clock icon (Triggers) on the left
   - Click "Create new trigger"
   - Configure:
     - Function: `captureJobEmails`
     - Deployment: `Head`
     - Event type: `Time-driven`
     - Frequency: `Every hour` (or every 30 minutes)
   - Click "Save"

### How to use:

1. When you receive a job email, **star it** and **add the `job-leads` label**
2. The script will run every hour and:
   - Pull emails with the `job-leads` label
   - Convert them to markdown files
   - Save them to your Google Drive folder
   - Add the email label so it doesn't duplicate

3. **Sync Google Drive to your laptop:**
   - Install [Google Drive for Desktop](https://www.google.com/drive/download/)
   - Choose "Stream" or "Mirror" sync
   - It will sync your Drive folder to a local path
   - Configure a Git ignore rule to sync just the markdown files, or manually download them

---

## Option 2: Python Script (More control, requires setup)

If you prefer to run this locally:

1. **Install Google API libraries:**
   ```bash
   pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

2. **Set up Gmail API:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Gmail API and Google Drive API
   - Create an OAuth 2.0 credential (Desktop App)
   - Download the JSON credentials file → save as `credentials.json` in this folder

3. **Run the script:**
   - Use `python job-email-capture.py` to convert emails to markdown files in `jobs/prospective/`
   - On first run, it will open a browser to authorize Gmail access
   - Add it to your Windows Task Scheduler to run every hour

---

## Option 3: Zapier/IFTTT (Easiest but requires subscription)

**Zapier** (paid, free tier limited):
- Trigger: New email with label `job-leads`
- Action: Create file in Google Drive/Dropbox
- Action: Append to Google Sheet as a log

**IFTTT** (free):
- Trigger: Email to specific address
- Action: Create document in Google Drive
- (More limited formatting)

Setup instructions: See `SETUP_ZAPIER.md`

---

## Syncing to your laptop

Once you have files in Google Drive:

1. **Google Drive for Desktop (Recommended):**
   - Download from [Google Drive for Desktop](https://www.google.com/drive/download/)
   - Install and sign in
   - Choose "Stream" (on-demand, saves space) or "Mirror" (full sync)
   - Navigate to your job-prospective folder
   - Link it to your repo with a Git symlink:
     ```powershell
     cd E:\job_applications\jobsearch\jobs\prospective
     New-Item -ItemType SymbolicLink -Path "from-email" -Target "C:\Users\[YOUR_USER]\Google Drive\job-prospective"
     ```

2. **Manual download:**
   - Download markdown files from Google Drive when ready
   - Paste into `jobs/prospective/`

3. **Rclone (Advanced):**
   - Use [Rclone](https://rclone.org/) to sync Google Drive ↔ local folder in background
   - Set up a scheduled task to run `rclone sync` every hour

---

## Testing

After setup:

1. Send yourself a test email with subject: `Test: Senior Backend Engineer at ACME Corp`
2. Star it and label it `job-leads`
3. Wait for the script to run (or click "Run" manually)
4. Check your Google Drive folder for the generated markdown file

The file should be named something like `2026-06-12_test-senior-backend-engineer-acme-corp.md` and contain the email body formatted as markdown.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Script runs but no files appear | Check Gmail label name is exactly `job-leads`, check folder ID is correct |
| "Authorization failed" | Clear browser cache and re-authorize the script |
| Duplicates appearing | Script adds a label to mark processed emails; if missing, emails get reprocessed |
| Too slow | Increase trigger frequency or use Python script instead |


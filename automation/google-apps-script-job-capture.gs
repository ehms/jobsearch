// Google Apps Script: Convert job emails to markdown files
// Copy this entire file into Google Apps Script editor at script.google.com
// Then follow setup instructions in SETUP_EMAIL_CAPTURE.md

const GMAIL_LABEL = 'job-leads';
const PROCESSED_LABEL = 'job-leads/processed';
const DRIVE_FOLDER_ID = 'your-folder-id-here'; // Replace with your Google Drive folder ID

function captureJobEmails() {
  try {
    // Get all unprocessed emails with the job-leads label
    const label = GmailApp.getUserLabelByName(GMAIL_LABEL);
    if (!label) {
      Logger.log(`Label "${GMAIL_LABEL}" not found. Create it in Gmail first.`);
      return;
    }

    const threads = label.getThreads(0, 50); // Process up to 50 emails per run
    let processed = 0;

    for (const thread of threads) {
      const messages = thread.getMessages();
      for (const message of messages) {
        // Skip already processed emails
        if (message.getLabels().some(l => l.getName() === PROCESSED_LABEL)) {
          continue;
        }

        const fileName = generateFileName(message);
        const markdown = convertEmailToMarkdown(message);

        // Save to Google Drive
        const folder = DriveApp.getFolderById(DRIVE_FOLDER_ID);
        const file = folder.createFile(fileName + '.md', markdown);

        Logger.log(`Created: ${fileName}.md`);

        // Mark as processed
        try {
          const processedLabel = GmailApp.getUserLabelByName(PROCESSED_LABEL);
          if (!processedLabel) {
            // Create the label if it doesn't exist
            GmailApp.createLabel(PROCESSED_LABEL);
            const newLabel = GmailApp.getUserLabelByName(PROCESSED_LABEL);
            message.addLabel(newLabel);
          } else {
            message.addLabel(processedLabel);
          }
        } catch (e) {
          Logger.log(`Could not mark as processed: ${e}`);
        }

        processed++;
      }
    }

    Logger.log(`Processed ${processed} emails`);
  } catch (error) {
    Logger.log(`Error: ${error.message}`);
    throw error;
  }
}

function generateFileName(message) {
  const date = Utilities.formatDate(message.getDate(), Session.getScriptTimeZone(), 'yyyy-MM-dd');
  const subject = message.getSubject()
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '') // Remove special characters
    .replace(/\s+/g, '-') // Replace spaces with hyphens
    .replace(/-+/g, '-') // Replace multiple hyphens with single
    .substring(0, 60); // Limit length

  return `${date}_${subject}`;
}

function convertEmailToMarkdown(message) {
  const subject = message.getSubject();
  const from = message.getFrom();
  const date = Utilities.formatDate(message.getDate(), Session.getScriptTimeZone(), 'yyyy-MM-dd HH:mm:ss');
  const body = message.getPlainBody();

  // Parse subject for company and role (adjust regex as needed)
  // Expected format: "Company - Role" or "Role at Company"
  let company = 'Unknown';
  let role = 'Unknown';

  const match1 = subject.match(/^([^-]+)\s*-\s*(.+)$/);
  if (match1) {
    company = match1[1].trim();
    role = match1[2].trim();
  }

  const markdown = `---
company: "${company}"
role: "${role}"
url: ""
posted: "${date}"
salary: "Not listed"
location: "See email"
source: "Email from ${from}"
---

# ${company} - ${role}

## Email Details

- **From:** ${from}
- **Date:** ${date}
- **Subject:** ${subject}

## Job Description

${body}

## My Notes

- [ ] Read full description
- [ ] Self-assess fit
- [ ] Ready to apply

---

*Captured from email on ${date}. Edit company, role, and location above before applying.*
`;

  return markdown;
}

function testEmailCapture() {
  // Test function - remove after confirming it works
  Logger.log('Testing email capture...');
  captureJobEmails();
}

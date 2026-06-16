#!/usr/bin/env python3
"""
Job Email Capture - Convert Gmail emails to markdown files
Run with: python job-email-capture.py
"""

import os
import pickle
import re
from datetime import datetime
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.api_core.exceptions import HttpError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Configuration
GMAIL_LABEL = 'job-leads'
OUTPUT_DIR = Path(__file__).parent.parent / 'jobs' / 'prospective'
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'


def authenticate_gmail():
    """Authenticate with Gmail API."""
    creds = None

    # Load existing token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # Refresh or create new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(
                    f'{CREDENTIALS_FILE} not found. '
                    'Download OAuth credentials from Google Cloud Console first.'
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save token for future runs
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_gmail_service(creds):
    """Create Gmail service."""
    return build('gmail', 'v1', credentials=creds)


def get_label_id(service, label_name):
    """Get Gmail label ID by name."""
    try:
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        for label in labels:
            if label['name'] == label_name:
                return label['id']
        return None
    except HttpError as error:
        print(f'Error getting labels: {error}')
        return None


def get_unread_emails(service, label_id, max_results=10):
    """Get unread emails from specified label."""
    try:
        # Query for unread emails with label
        query = f'label:{GMAIL_LABEL} is:unread'
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=max_results
        ).execute()
        return results.get('messages', [])
    except HttpError as error:
        print(f'Error getting messages: {error}')
        return []


def get_email_details(service, message_id):
    """Get full email details."""
    try:
        message = service.users().messages().get(
            userId='me',
            id=message_id,
            format='full'
        ).execute()
        return message
    except HttpError as error:
        print(f'Error getting message: {error}')
        return None


def extract_email_content(message):
    """Extract subject, from, date, and body from email."""
    headers = message['payload'].get('headers', [])
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
    from_addr = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
    date_str = next((h['value'] for h in headers if h['name'] == 'Date'), '')

    # Extract body
    body = ''
    if 'parts' in message['payload']:
        for part in message['payload']['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body'].get('data', '')
                if data:
                    body = data.replace('-', '')  # Decode base64 if needed
                    break
    else:
        body = message['payload']['body'].get('data', '')

    return subject, from_addr, date_str, body


def generate_filename(subject, date_str):
    """Generate markdown filename from subject and date."""
    # Parse date
    try:
        date_obj = datetime.strptime(date_str[:10], '%Y-%m-%d')
        date_prefix = date_obj.strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        date_prefix = datetime.now().strftime('%Y-%m-%d')

    # Clean subject for filename
    clean_subject = re.sub(r'[^a-z0-9\s-]', '', subject.lower())
    clean_subject = re.sub(r'\s+', '-', clean_subject)
    clean_subject = re.sub(r'-+', '-', clean_subject)
    clean_subject = clean_subject[:60]

    return f'{date_prefix}_{clean_subject}'


def parse_company_and_role(subject):
    """Try to extract company and role from subject."""
    # Pattern: "Company - Role" or "Role at Company"
    match = re.match(r'^([^-]+)\s*-\s*(.+)$', subject)
    if match:
        return match.group(1).strip(), match.group(2).strip()

    match = re.search(r'(.+?)\s+at\s+(.+)', subject, re.IGNORECASE)
    if match:
        return match.group(2).strip(), match.group(1).strip()

    return 'Unknown', subject


def convert_to_markdown(subject, from_addr, date_str, body):
    """Convert email to markdown format."""
    company, role = parse_company_and_role(subject)

    markdown = f"""---
company: "{company}"
role: "{role}"
url: ""
posted: "{date_str}"
salary: "Not listed"
location: "See email"
source: "Email from {from_addr}"
---

# {company} - {role}

## Email Details

- **From:** {from_addr}
- **Date:** {date_str}
- **Subject:** {subject}

## Job Description

{body}

## My Notes

- [ ] Read full description
- [ ] Self-assess fit
- [ ] Ready to apply

---

*Captured from email on {date_str}. Edit company, role, and location above before applying.*
"""
    return markdown


def mark_as_read(service, message_id):
    """Mark email as read."""
    try:
        service.users().messages().modify(
            userId='me',
            id=message_id,
            body={'removeLabelIds': ['UNREAD']}
        ).execute()
    except HttpError as error:
        print(f'Error marking as read: {error}')


def main():
    """Main function."""
    print('Starting job email capture...')

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Authenticate
    creds = authenticate_gmail()
    service = get_gmail_service(creds)

    # Get label ID
    label_id = get_label_id(service, GMAIL_LABEL)
    if not label_id:
        print(f'Label "{GMAIL_LABEL}" not found. Create it in Gmail first.')
        return

    # Get unread emails
    emails = get_unread_emails(service, label_id, max_results=10)
    if not emails:
        print(f'No unread emails found with label "{GMAIL_LABEL}"')
        return

    print(f'Found {len(emails)} unread emails')

    # Process each email
    for message in emails:
        message_id = message['id']
        full_message = get_email_details(service, message_id)
        if not full_message:
            continue

        # Extract content
        subject, from_addr, date_str, body = extract_email_content(full_message)

        # Generate filename and markdown
        filename = generate_filename(subject, date_str)
        markdown = convert_to_markdown(subject, from_addr, date_str, body)

        # Save to file
        output_path = OUTPUT_DIR / f'{filename}.md'
        output_path.write_text(markdown, encoding='utf-8')
        print(f'✓ Created: {filename}.md')

        # Mark as read
        mark_as_read(service, message_id)

    print(f'Done! Files saved to {OUTPUT_DIR}')


if __name__ == '__main__':
    main()

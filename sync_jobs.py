#!/usr/bin/env python3
"""
Sync job applications from Obsidian vault to external jobsearch directory.
Reads YAML frontmatter from markdown files and generates summary files.

Usage: python sync_jobs.py
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime, date
import yaml


def json_serial(obj):
    """JSON serializer for objects not serializable by default (e.g. date)."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

# Configuration
VAULT_PATH = Path("X:/Vault/Hatch")
JOBSEARCH_PATH = Path("E:/job_applications/jobsearch")
JOBS_FOLDER = "job-hunt"  # Folder in vault where job application notes live

# Status order for kanban
STATUS_ORDER = ["Interesting", "To Apply", "Applied", "Response"]


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        try:
            frontmatter = yaml.safe_load(match.group(1))
            if not isinstance(frontmatter, dict):
                return {}
            # Normalize date/datetime objects to ISO strings
            # (YAML auto-parses unquoted dates like 2026-06-15 into date objects)
            for key, value in frontmatter.items():
                if isinstance(value, (datetime, date)):
                    frontmatter[key] = value.isoformat()
            return frontmatter
        except yaml.YAMLError as e:
            print(f"  ⚠️  YAML parse error: {e}")
            return {}
    return {}


def read_job_applications():
    """Scan vault for job application notes and extract metadata."""
    jobs_folder = VAULT_PATH / JOBS_FOLDER
    
    if not jobs_folder.exists():
        print(f"❌ Jobs folder not found: {jobs_folder}")
        return []
    
    applications = []
    
    for md_file in jobs_folder.glob("*.md"):
        # Skip the kanban board file itself
        if md_file.name == "Job Applications Board.md":
            continue
        
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            frontmatter = extract_frontmatter(content)
            
            # Ensure required fields
            if not frontmatter.get("company") or not frontmatter.get("role"):
                print(f"  ⚠️  Skipping {md_file.name} (missing company or role)")
                continue
            
            # Build application object
            app = {
                "file": md_file.name,
                "company": frontmatter.get("company", ""),
                "role": frontmatter.get("role", ""),
                "status": frontmatter.get("status", "Interesting"),
                "url": frontmatter.get("url", ""),
                "posting_date": frontmatter.get("posting_date", ""),
                "deadline": frontmatter.get("deadline", ""),
                "key_requirements": frontmatter.get("key_requirements", ""),
                "sector": frontmatter.get("sector", ""),
                "team_size": frontmatter.get("team_size", ""),
                "salary": frontmatter.get("salary", ""),
                "type": frontmatter.get("type", "posted"),
                "date_found": frontmatter.get("date_found", ""),
            }
            
            applications.append(app)
            print(f"  ✓ {app['company']} — {app['role']} ({app['status']})")
        
        except Exception as e:
            print(f"  ❌ Error reading {md_file.name}: {e}")
    
    return applications


def generate_markdown(applications):
    """Generate markdown summary of all applications."""
    markdown = "# Job Applications Summary\n\n"
    markdown += f"**Last synced:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    markdown += f"**Total applications:** {len(applications)}\n"
    
    # Group by status
    by_status = {status: [] for status in STATUS_ORDER}
    for app in applications:
        status = app.get("status", "Interesting")
        if status not in by_status:
            by_status[status] = []
        by_status[status].append(app)
    
    # Sort by deadline within each status
    for status in by_status:
        by_status[status].sort(
            key=lambda x: x.get("deadline", "9999-12-31") or "9999-12-31"
        )
    
    # Generate sections for each status
    for status in STATUS_ORDER:
        apps = by_status.get(status, [])
        if not apps:
            continue
        
        markdown += f"\n## {status} ({len(apps)})\n\n"
        
        for app in apps:
            markdown += f"### {app['company']} — {app['role']}\n"
            
            if app["url"]:
                markdown += f"- **URL:** [{app['url']}]({app['url']})\n"
            
            if app["posting_date"]:
                markdown += f"- **Posted:** {app['posting_date']}\n"
            
            if app["deadline"]:
                markdown += f"- **Deadline:** {app['deadline']}\n"
            
            if app["sector"]:
                markdown += f"- **Sector:** {app['sector']}\n"
            
            if app["team_size"]:
                markdown += f"- **Team size:** {app['team_size']}\n"
            
            if app["salary"]:
                markdown += f"- **Salary:** {app['salary']}\n"
            
            if app["key_requirements"]:
                markdown += f"- **Requirements:** {app['key_requirements']}\n"
            
            markdown += f"- **Found:** {app['date_found']}\n"
            markdown += f"- **Source:** `{app['file']}`\n\n"
    
    return markdown


def generate_json(applications):
    """Generate JSON export of all applications."""
    json_output = {
        "generated": datetime.now().isoformat(),
        "total_applications": len(applications),
        "by_status": {},
        "applications": applications
    }
    
    # Count by status
    for app in applications:
        status = app.get("status", "Interesting")
        if status not in json_output["by_status"]:
            json_output["by_status"][status] = 0
        json_output["by_status"][status] += 1
    
    return json_output


def main():
    """Main sync function."""
    print(f"\n🔄 Syncing job applications...\n")
    print(f"📂 Vault: {VAULT_PATH}")
    print(f"📂 Jobsearch: {JOBSEARCH_PATH}\n")
    
    # Ensure jobsearch directory exists
    JOBSEARCH_PATH.mkdir(parents=True, exist_ok=True)
    
    # Read applications from vault
    print("Reading applications from vault:")
    applications = read_job_applications()
    
    if not applications:
        print("\n⚠️  No applications found.")
        return
    
    print(f"\n✅ Found {len(applications)} applications\n")
    
    # Generate outputs
    print("Generating summary files...")
    markdown = generate_markdown(applications)
    json_data = generate_json(applications)
    
    # Write markdown summary
    md_path = JOBSEARCH_PATH / "applications.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"  ✓ {md_path}")
    
    # Write JSON export
    json_path = JOBSEARCH_PATH / "applications.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, default=json_serial)
    print(f"  ✓ {json_path}")
    
    print(f"\n✅ Sync complete!\n")
    
    # Summary stats
    print("📊 Summary:")
    for status in STATUS_ORDER:
        count = json_data["by_status"].get(status, 0)
        if count > 0:
            print(f"  {status}: {count}")


if __name__ == "__main__":
    main()

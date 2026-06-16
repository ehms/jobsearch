#!/usr/bin/env python3
"""
Job URL Parser
Reads job URLs from Obsidian vault, fetches postings, extracts details, outputs summary.
"""

import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Missing dependencies (requests, beautifulsoup4)")
    print("Install with: pip install requests beautifulsoup4")
    sys.exit(1)

# Configuration
VAULT_PATH = Path(r"X:\Vault\Hatch\job-hunt\job-urls.md")  # Obsidian double extension
OUTPUT_PATH = Path(__file__).parent / "parsed-jobs.md"
TIMEOUT = 10
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

class JobParser:
    def __init__(self):
        self.jobs = []
        self.errors = []

    def read_urls(self):
        """Extract URLs from Obsidian job-urls.md, skip #coldcall lines"""
        if not VAULT_PATH.exists():
            raise FileNotFoundError(f"Job URLs file not found: {VAULT_PATH}")

        content = VAULT_PATH.read_text(encoding='utf-8')
        lines = content.split('\n')

        # Extract URLs, but skip lines with #coldcall tag
        urls = []
        for line in lines:
            if '#coldcall' in line:
                continue  # Skip cold-call targets
            matches = re.findall(r'https?://[^\s\)]+', line)
            urls.extend(matches)

        if not urls:
            print("No job posting URLs found (cold-call targets with #coldcall are skipped)")
            return []

        print(f"Found {len(urls)} job posting URL(s) to parse")
        return urls

    def fetch_and_parse(self, url):
        """Fetch job posting and extract key details"""
        try:
            response = requests.get(url, timeout=TIMEOUT, headers=HEADERS)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract title (try common selectors)
            title = self._extract_title(soup, url)
            company = self._extract_company(soup, url)
            location = self._extract_location(soup)
            posting_date = self._extract_posting_date(soup)
            requirements = self._extract_requirements(soup)

            return {
                "url": url,
                "title": title,
                "company": company,
                "location": location,
                "posting_date": posting_date,
                "requirements": requirements,
                "status": "success"
            }

        except requests.exceptions.Timeout:
            self.errors.append(f"⏱️  Timeout: {url}")
            return None
        except requests.exceptions.ConnectionError:
            self.errors.append(f"🔗 Connection error: {url}")
            return None
        except Exception as e:
            self.errors.append(f"❌ Error parsing {url}: {str(e)}")
            return None

    def _extract_title(self, soup, url):
        """Extract job title from page"""
        # LinkedIn
        if "linkedin.com" in url:
            title = soup.find("h1", class_=re.compile("top-card-layout__title"))
            if title:
                return title.get_text(strip=True)

        # Indeed
        if "indeed.com" in url:
            title = soup.find("h1", class_=re.compile("jobsearch-JobInfoHeader"))
            if title:
                return title.get_text(strip=True)

        # Generic: try <h1> or <title>
        h1 = soup.find("h1")
        if h1:
            return h1.get_text(strip=True)

        page_title = soup.find("title")
        if page_title:
            text = page_title.get_text(strip=True)
            # Clean up typical job title formats
            text = re.sub(r'\s*\|\s*(LinkedIn|Indeed|.*Jobs).*', '', text)
            return text[:80]  # Truncate to 80 chars

        return "Unknown Title"

    def _extract_company(self, soup, url):
        """Extract company name"""
        # LinkedIn
        if "linkedin.com" in url:
            comp = soup.find("a", class_=re.compile("topcard__org-name-link"))
            if comp:
                return comp.get_text(strip=True)

        # Indeed
        if "indeed.com" in url:
            comp = soup.find("span", {"data-testid": "jobsearch-JobInfoHeader-companyName"})
            if comp:
                return comp.get_text(strip=True)

        # Parse from URL domain
        domain = urlparse(url).netloc
        company = domain.replace("www.", "").replace(".com", "").replace(".ie", "").title()
        return company

    def _extract_location(self, soup):
        """Extract job location"""
        # Try common location indicators
        selectors = [
            ("span", re.compile("location"), "class"),
            ("span", {"data-testid": "jobsearch-JobInfoHeader-jobLocationMobile"}, "attrs"),
        ]

        for tag, pattern, selector_type in selectors:
            if selector_type == "class":
                elem = soup.find(tag, class_=pattern)
            else:
                elem = soup.find(tag, pattern)

            if elem:
                return elem.get_text(strip=True)

        return "Location not found"

    def _extract_posting_date(self, soup):
        """Extract posting date"""
        # Try common date patterns
        for pattern in [
            r'Posted\s+(\d{1,2}\s+\w+\s+\d{4})',
            r'(\d{1,2}\s+\w+\s+\d{4})',
            r'Posted\s+(\d+\s+days?\s+ago)',
        ]:
            text = soup.get_text()
            match = re.search(pattern, text)
            if match:
                return match.group(1)

        return "Date not found"

    def _extract_requirements(self, soup):
        """Extract key requirements (first few bullet points)"""
        requirements = []

        # Find bullet points
        bullets = soup.find_all(['li', 'div'], class_=re.compile("requirement|skill|qualify"))

        for bullet in bullets[:5]:  # First 5 bullets
            text = bullet.get_text(strip=True)
            if text and len(text) > 10:
                requirements.append(text[:100])  # Truncate

        if requirements:
            return " | ".join(requirements)

        return "Requirements not parsed"

    def generate_summary(self):
        """Generate markdown summary of parsed jobs"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        markdown = f"# Parsed Job URLs\n\n"
        markdown += f"**Last parsed:** {timestamp}\n"
        markdown += f"**Total:** {len(self.jobs)} job(s) parsed\n\n"

        if self.jobs:
            markdown += "## Jobs Found\n\n"
            for i, job in enumerate(self.jobs, 1):
                markdown += f"### {i}. {job['title']}\n\n"
                markdown += f"- **Company:** {job['company']}\n"
                markdown += f"- **Location:** {job['location']}\n"
                markdown += f"- **Posted:** {job['posting_date']}\n"
                markdown += f"- **URL:** [{job['url'].split('/')[2]}]({job['url']})\n"
                markdown += f"- **Requirements:** {job['requirements']}\n\n"

        if self.errors:
            markdown += "## Errors / Failed Parses\n\n"
            for error in self.errors:
                markdown += f"- {error}\n"

        return markdown

    def run(self):
        """Main execution"""
        print("=" * 60)
        print("Job URL Parser")
        print("=" * 60)

        try:
            urls = self.read_urls()

            if not urls:
                print("No URLs to parse.")
                return

            print("\nParsing job postings...\n")

            for i, url in enumerate(urls, 1):
                print(f"[{i}/{len(urls)}] {url[:60]}...", end=" ")
                job = self.fetch_and_parse(url)

                if job:
                    self.jobs.append(job)
                    print("[OK]")
                else:
                    print("[FAILED]")

            # Generate and save summary
            summary = self.generate_summary()
            OUTPUT_PATH.write_text(summary, encoding='utf-8')

            print("\n" + "=" * 60)
            print(f"✓ Summary saved to: {OUTPUT_PATH}")
            print(f"✓ Successfully parsed: {len(self.jobs)} job(s)")

            if self.errors:
                print(f"⚠️  Errors: {len(self.errors)}")

            print("=" * 60)

        except FileNotFoundError as e:
            print(f"ERROR: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"FATAL ERROR: {e}")
            sys.exit(1)

if __name__ == "__main__":
    parser = JobParser()
    parser.run()

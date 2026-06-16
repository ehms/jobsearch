# Complete Job Application Workflow

End-to-end guide: from finding a job to submitting an application.

## Phase 1: Job Discovery & Capture

### Manual capture (no automation)
1. Find a job posting online (LinkedIn, Indeed, Jobindex, etc.)
2. Copy the job description
3. Create file: `jobs/prospective/company_role.md` using `jobs/job-template.md`
4. Paste job description into the template
5. Go to Phase 2

### Automated email capture
1. Receive job email or forward interesting postings to yourself
2. **Star** the email + add **`job-leads`** label in Gmail
3. Wait for automation (runs hourly):
   - Google Apps Script → syncs to Google Drive
   - Python script → saves directly to `jobs/prospective/`
4. Review the created markdown file
5. Edit metadata if needed (company name, salary, location)
6. Go to Phase 2

### Using the built-in scraper
1. Run `/scrape` in Claude Code
2. Claude searches job portals matching your profile
3. Select a job from the results
4. Claude runs `/apply` directly on selected job
5. Skip to Phase 3

---

## Phase 2: Pre-Application Review

**File location:** `jobs/prospective/company_role.md`

Before applying, quickly assess fit:

```markdown
## My Fit Assessment

### Strengths
- [Match these job keywords to your experience]
- [What you're excited about in this role]
- [Relevant projects or skills]

### Gaps
- [Skills you don't have yet]
- [Experience areas that don't align]
- [Geographic or commute concerns]
```

**Decision points:**
- ✓ Ready to apply? → Phase 3
- ✗ Not a good fit? → Move to `jobs/applied/` with rejection note
- ? Unsure? → Use `/upskill` to analyze the gap

---

## Phase 3: Full Application Workflow

**Command:**
```bash
/apply jobs/prospective/company_role.md
```

This runs the **drafter-reviewer pipeline**:

1. **Parse** - Extract job requirements
2. **Fit evaluation** - Score against your profile
   - Skills match (0-10)
   - Experience match (0-10)
   - Culture/behavioral fit (0-10)
   - Location/commute (0-10)
   - Career alignment (0-10)
   - **Final recommendation:** ✓ Apply / ⚠️ Apply with caution / ✗ Skip
3. **Ask permission** - Review fit assessment, decide to proceed
4. **Draft CV** - Create targeted `cv/main_company.md`
5. **Draft cover letter** - Create targeted `cover_letters/cover_company_role.md`
6. **Reviewer review** - Second Claude agent critiques drafts
   - Keywords match?
   - Framing strong?
   - Completeness?
   - Length budgets?
7. **Revise** - First Claude agent refines based on feedback
8. **Final review** - Verify:
   - [ ] CV is ~2 pages (markdown)
   - [ ] Cover letter is 250-300 words
   - [ ] No broken formatting or placeholders
   - [ ] All facts are accurate
9. **Output** - Get final markdown files ready to convert/upload

---

## Phase 4: Document Export & Submission

**Files created:**
- `cv/main_company.md` - Your tailored CV
- `cover_letters/cover_company_role.md` - Tailored cover letter

### Convert to PDF (if needed)

Using Pandoc (free):

```bash
# Install (one-time)
choco install pandoc

# Convert
pandoc cv/main_company.md -o cv/main_company.pdf
pandoc cover_letters/cover_company_role.md -o cover_letters/cover_company_role.pdf
```

Or use an online tool: [Markdown to PDF](https://markdowntopdf.com/)

### Upload to job portal
1. Create account on job board (if needed)
2. Fill in application form
3. Upload CV PDF
4. Paste cover letter text or upload
5. Submit

---

## Phase 5: Tracking & Follow-up

### After submission:
1. Move the prospective job file to `jobs/applied/`:
   ```bash
   move jobs/prospective/company_role.md jobs/applied/
   ```

2. Add a submission note to the file:
   ```markdown
   ---
   company: "ACME Corp"
   role: "Senior Engineer"
   status: "applied"
   submitted: "2026-06-12"
   application_id: "[if provided]"
   ---
   ```

3. Update your personal tracker:
   - Email, date, portal, status
   - Any follow-up items

### Interview preparation (if called):
1. Run `/expand` to enrich your profile with public sources
2. Review `07-interview-prep.md` for STAR examples
3. Run `/upskill <company_name>` to analyze the company's tech/culture
4. Prepare talking points based on job requirements

---

## Workflow Diagram

```
Job Discovery
    ├─ Manual capture (copy-paste)
    ├─ Email automation (Gmail → Drive → local)
    └─ Built-in scraper (/scrape)
           ↓
       Prospective folder
           ├─ Review fit
           └─ Edit metadata
           ↓
      /apply command
           ├─ Fit evaluation
           ├─ Draft CV + Cover
           ├─ Review feedback
           └─ Final output
           ↓
      Export & Submit
           ├─ Convert to PDF (if needed)
           └─ Upload to job board
           ↓
      Track in Applied folder
           ├─ Move file
           ├─ Add status metadata
           └─ Prepare for interviews
```

---

## Tips for Best Results

### Before applying:
- **Read the full job description** - Don't assume from the title
- **Research the company** - Culture, tech stack, reviews
- **Time your application** - Apply early in the day (less competition)
- **Check for referrals** - Knowing someone increases callback rate 3x

### CV tailoring:
- Lead with most relevant experience
- Use job posting keywords naturally
- Quantify achievements where possible
- Keep formatting clean and simple

### Cover letter:
- Address specific person if possible ("Dear [Hiring Manager Name]")
- Reference specific requirements from the job posting
- Keep it to 250-300 words (one printed page)
- Make it personal - avoid generic templates

### Follow-up:
- Wait 2 weeks, then check status on job board
- If contacted for interview, reply within 24 hours
- Send thank-you note after interview

---

## Quick Reference

| What | Command | Output |
|------|---------|--------|
| Capture job | Star + label in Gmail | Markdown in `jobs/prospective/` |
| Assess fit | Edit `My Fit Assessment` section | None (internal decision) |
| Apply | `/apply jobs/prospective/job.md` | CV + cover letter |
| Search jobs | `/scrape` | Ranked list of matches |
| Analyze gaps | `/upskill <url>` | Skill gap heatmap + learning plan |
| Enrich profile | `/expand` | Updated skills from online sources |
| Prepare interviews | Edit `07-interview-prep.md` | STAR examples ready |
| Convert PDF | `pandoc input.md -o output.pdf` | PDF file |

---

See also:
- `jobs/README.md` - Prospecting folder guide
- `README.md` - Automation setup options
- `SETUP_EMAIL_CAPTURE.md` - Email capture detailed setup

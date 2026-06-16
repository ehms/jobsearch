# Job Prospecting

Store job leads here before applying.

## Structure

- **prospective/** - Jobs you've found but haven't applied to yet
- **applied/** - Jobs you've submitted applications for (tracked separately from `cv/` and `cover_letters/`)

## How to capture jobs

### Option 1: Email forward (recommended)
Forward job postings to yourself, then:
1. Copy the job description
2. Use the template below to create `prospective/<company>_<role>.md`
3. Run `/apply prospective/<company>_<role>.md` when ready

### Option 2: Browser extension
Use a web clipper (Notion, Pocket, or custom extension) to save job postings directly to this folder as markdown.

### Option 3: Manual
See `job-template.md` for the standard format.

## Naming convention

`<company>_<role-title>.md` - e.g., `acme-corp_senior-backend-engineer.md`

## Template

```markdown
---
company: ""
role: ""
url: ""
posted: ""
salary: ""
location: ""
source: ""
---

# [Company] - [Role Title]

## About the Role

[Job description copied here]

## My Notes

- [ ] Skills match
- [ ] Experience match
- [ ] Culture fit
- [ ] Location/commute
- [ ] Ready to apply

```

Once you mark "Ready to apply", run:
```bash
/apply <file path>
```

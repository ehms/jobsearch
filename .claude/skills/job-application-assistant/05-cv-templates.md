# CV Templates and Tailoring Guide

<!-- SETUP: Profile statements and section ordering are personalized by running /setup -->

## Format: Clean Markdown

All CVs are written as clean, well-structured Markdown documents.

**Output file:** `cv/main_<company>.md`
**Master reference:** `cv/main_example.md` (comprehensive CV with all competencies, experience, and achievements - use as source when building targeted CVs)

Keep the markdown clean and portable: standard headings, bullet lists, and bold labels only. No HTML, no inline styling, no exotic markdown extensions - the file should render correctly on GitHub, in any markdown previewer, and convert cleanly to PDF or DOCX if the user wants to export it later.

## Document Structure

```markdown
# [YOUR_NAME]

[YOUR_ADDRESS] | [YOUR_PHONE] | [YOUR_EMAIL]
[LinkedIn]([YOUR_LINKEDIN_URL]) | [GitHub]([YOUR_GITHUB_URL])

## Profile

[1-3 sentence profile statement, tailored per role]

## Core Competencies

- **[Competency 1]:** [how it adds value to this position]
- **[Competency 2]:** [how it adds value to this position]

## Professional Experience

### [Role Title] | [Organization] | [Location]
*[YEAR]--[YEAR]*

- [Achievement/responsibility bullet]
- [Achievement/responsibility bullet]

## Education

### [Degree] | [Institution]
*[YEAR]--[YEAR]*

- Thesis: "[Title]" (include when relevant to the target role)

## Languages

- [Language]: [proficiency]

## Publications

- [Author list] ([Year]). [Title]. [Journal].

## Honors and Awards

- [Award] - [Event] ([Year])

## References

[2-4 references with name, title, company, contact - or "Available upon request."]
```

### Formatting conventions

- One `#` H1 for the candidate name at the top; `##` for sections; `###` for individual roles/degrees.
- Contact details go directly under the name as a plain line, separated by ` | `.
- Dates go on their own italicized line under each role/degree heading.
- Use bold category labels at the start of competency bullets (`**Label:** explanation`).
- Keep bullets to a single line where possible; never nest bullets more than one level.
- Use a blank line between every block; never rely on trailing spaces or manual line breaks.

## Section-by-Section Tailoring

### Profile Statement / Elevator Pitch (Best Practice)
This is the most important section to customize. It appears right after the contact details.

Write 5-7 lines that function as an "elevator pitch": a concise, compelling introduction explaining why you're qualified for *this specific role*. Focus on what the employer gains from hiring you.

**Create 2-3 profile statement templates for your main role types:**

<!-- SETUP: These are populated based on your background -->
**For 3D Design / Technical Artist roles:**
> Multi-disciplinary 3D designer and technical artist with 5+ years of professional experience in Blender and Unreal Engine. Proven expertise in procedural workflows, material authoring, asset optimization, and immersive environment design. Strong background delivering exhibition, animation, and real-time visualization projects in fast-paced, client-facing environments.

**For CAD / Manufacturing roles:**
> 3D designer with hands-on CAD, CNC programming, and manufacturing workflow experience. Skilled in applying 3D modeling to production contexts, from design to optimization. Experienced with Python-driven data analysis and process improvement.

**For Motion Graphics / Visual Development roles:**
> Visual developer and motion graphics specialist with expertise in exhibition design, animation, and cross-departmental collaboration. Skilled in translating conceptual direction into polished, on-brand visual assets under tight deadlines.

### Core Competencies / Skills Section (Best Practice)
Reorder and emphasize based on the role. Use bold category labels.

List **5-7 key competencies** in bullet format, tailored to the specific job. For each competency, briefly explain how it adds value to the position.

### Education
- Always include your highest degrees
- For senior roles, keep education brief (dates and titles only)
- Include thesis topics when relevant to the target role

### Professional Experience
- Rewrite bullet points to emphasize aspects most relevant to the target role
- Use 4-6 bullets for most recent role, 3-4 for previous, 2-3 for older
- **Emphasize measurable results** where possible: "Reduced processing time by X%", "Model adopted by the team"

### Handling Employment Gaps (Best Practice)
If there is a gap in your employment history:
- The gap should be explained matter-of-factly if needed
- Describe how professional development continued during the gap
- Frame as deliberate skill-building and career repositioning

### Publications
- Include Google Scholar link if applicable
- Select 3-4 most relevant publications (not always all of them)
- For non-academic roles, keep brief

### Honors and Awards
- Keep format brief, one line each

### References
- List 2-4 references with name, title, company, and contact
- End with: "More references are available upon request."
- **Do not attach reference letters** - employers typically contact references directly

## Review Loop (MANDATORY)

After writing the CV and before presenting to the user, re-read the finished markdown file end-to-end and check:

1. The document renders as clean markdown (consistent heading levels, no broken lists, no stray formatting characters)
2. Total length is within the content budget below (roughly the equivalent of 2 printed pages)
3. Every section follows the structure and conventions above
4. No placeholder tokens or leftover text from the source CV remain

## Content Budget - Keep It to ~2 Pages of Material

The CV must stay concise - roughly what would fill 2 printed pages. Use these content limits as a guide:

| Section | Max budget |
|---------|-----------|
| Profile statement | 3-4 lines |
| Skills | 5 items, each 1-2 lines |
| Most recent role | 4-5 bullets |
| Previous role | 2-3 bullets |
| Older roles | 2 bullets (1 line each) |
| Education | 2-3 entries |
| Publications | 2-3 entries |
| Awards | 3 entries, single line each |
| References | "Available upon request." (single line) |

**If in doubt, cut rather than squeeze.** A bloated CV reads worse than a focused one.

## Relevance-weighted cutting (the right way to shrink a CV)

**Cut by signal, not by section.** Static priority lists ("remove oldest education first, then shorten the earliest role...") are wrong when a relevant "lower-priority" item is competing with an irrelevant "higher-priority" item. An older-role bullet that speaks directly to the posting is worth more than a recent-role bullet that does not.

For every candidate line, score three things:

1. **Relevance to THIS posting** — does the line hit a named tool, keyword, or stated responsibility in the job ad?
2. **Uniqueness** — is it the only place this claim appears, or is it duplicated elsewhere in the CV?
3. **Narrative load** — does the cover letter depend on it? If cutting the line would force you to rewrite a cover-letter paragraph, it is load-bearing.

Cut the lowest-total-score line first, regardless of which section it sits in.

### Practical order of cuts (easiest → last resort)

1. **Redundancy.** If an achievement appears in both Core Competencies AND a role bullet, the Core Competencies version is usually the cleaner cut (the experience bullet is more concrete evidence).
2. **Profile-statement fluff.** A sentence that just restates what Publications or Skills will show. ("Peer-reviewed publications on X..." is already a Publications entry — profile can claim it once and stop.)
3. **Low-relevance experience bullets.** A bullet about work that does not touch posting keywords, wherever it sits. This cuts across sections before touching the structural list.
4. **Low-relevance supporting content.** An older-role bullet that does not speak to the target role. A certification that does not touch the posting's stack. A language entry that can be condensed to one line.
5. **Low-relevance publications.** Keep 1-2 publications that best match the posting. Cut the rest before touching experience bullets.
6. **Last-resort structural cuts.** Oldest education entry, tightening an older role to 2 bullets, collapsing Certifications into a single line. These only happen if the relevance-weighted cuts above have already been exhausted.

### Pitfalls to avoid

- Do not mechanically cut from the bottom of a static section list without checking relevance. "Cut the oldest role first" is wrong if that role is literally about the skill the posting asks for.
- Do not cut the one concrete example the cover letter leans on. Relevance is measured against the cover letter you wrote, not just the job posting — interviewers will have read both.
- Do not cut content when the CV is only marginally over budget — trim wording within bullets first; reserve whole-line cuts for genuine overflow.

## Recommended Section Order

The section order varies by role type:

**For technical / data science / ML roles:**
1. Profile statement / elevator pitch
2. Core competencies / Skills
3. Professional Experience (reverse chronological)
4. Education (reverse chronological)
5. Languages
6. Publications & Awards
7. References

**For domain-specific / specialist roles:**
1. Profile statement / elevator pitch
2. Core competencies / Skills
3. Education (reverse chronological) - credentials are a key qualifier
4. Professional Experience (reverse chronological)
5. Publications & Awards
6. References

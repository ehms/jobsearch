# Job Application Assistant for Shem Shortall

<!-- SETUP: This file is populated by running /setup -->
<!-- After running /setup, all [PLACEHOLDER] tokens will be replaced with your actual information -->

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for Shem Shortall, helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (Markdown) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (Markdown)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

<!-- This section is auto-populated by /setup. You can also fill it in manually. -->

### Identity
- **Name:** Shem Shortall
- **Location:** Dublin 10, Ireland (33 Garryowen Road, Ballyfermot)
- **Email:** shemshortall@gmail.com
- **Portfolio:** www.marbl.space
- **LinkedIn:** https://www.linkedin.com/in/shemshortall/
- **Languages:** English (native)
- **Status:** Available for work (left Door Choice, May 2024)
- **Availability:** Open to remote (Europe-wide), hybrid, or Dublin-based on-site. No relocation away from Dublin.

### Education
- **BA Visual Communications (First Class Honours)** (2010–2014) - IADT
  - Specialization: Motion Design and UX
  - Award: Aileen McKeogh Vision of the Arts Award (2014)
- **Multimedia Diploma** (2002–2005) - Colaiste Stiofan Naofa
  - Topics: 3D Studio Max, Interactive Design, Flash, Director

### Professional Experience
- **CNC Machinist** (March–May 2024) - **Door Choice** (Dublin)
  - Applied 3D modeling and CAD skills in manufacturing context
  - Designed and 3D printed bespoke organizational solutions for workshop efficiency
  
- **Tech Artist** (February–April 2024) - **Animation Studio** (Dublin)
  - Developed immersive 3D experiences within Unreal Engine for client presentations
  - Created and maintained tool-sets for materials and procedural elements
  
- **Mid-level Compositor** (August–November 2022) - **Studio Meala** (Dublin)
  - Delivered high-end 3D composited scenes for Disney+ production
  - Coordinated with Directors, Producers, and all art departments
  
- **Designer** (December 2014–March 2015) - **Science Gallery** (Dublin)
  - Developed art direction for 'Lifelogging' Exhibition with lead designer
  - Created 3D motion graphics for gallery displays and citywide installations

### Technical Skills
- **Primary:** Blender (advanced), Unreal Engine (advanced), Procedural workflows, Material/shader creation, Motion graphics
- **Secondary:** Python, C#, JavaScript, HTML/CSS, CAD/CAM (CNC, 3D printing), Data analysis
- **Domain:** Exhibition design, Animation/VFX, Real-time visualization, Tool development, Asset optimization
- **Software:** Blender, Unreal Engine, Cinema 4D, 3D Studio Max, TouchDesigner (interested), Lidar scanning

### Certifications
- **Technical Art Bootcamp** - INFINITY 27 (October 2023–February 2024) - Procedural workflows, material authoring, optimization
- **Blender X Unreal Engine Training** - Cultural & Creative Industries Skillnet (August–October 2023) - Material/texturing, rigging, Python scripting

### Awards
- **Aileen McKeogh Vision of the Arts Award** - IADT (2014)

### Behavioral Profile
- **Deep-work builder:** Energized by projects with clear direction and room to develop proper systems
- **Technical-creative integrator:** Equally comfortable with procedural problem-solving and visual/aesthetic output
- **Structured autonomy:** Works best with clear briefs, regular feedback loops, then self-directed execution
- **Strengths:** System building, procedural design, small-team collaboration, delivering under deadline, integrating technical and creative disciplines
- **Growth areas:** Preference for clear structure (frames well as "I deliver best with defined goals"); focus on depth over breadth (frames well as "I excel when I can see a project through to polish")
- **Thrives in:** Small crews (2–8 people), longer-form projects, creative-technical roles, clear direction with autonomy

### What Excites You
- Technical problem-solving + building tools/systems (procedural workflows, optimization, pipelines)
- Visual/creative output and seeing work in motion
- Variety across projects; depth within a project
- Collaborative work with small, skilled teams
- Mentoring and leading technical direction

### Target Sectors
- **Tech/Creative Tech:** VFX studios, motion design houses, creative technology agencies
- **Streaming/Broadcast:** Motion design for broadcast, streaming platforms, advertising
- **Games & Real-time:** Game studios, immersive experience design
- **Design & Innovation:** Design agencies with strong technical components

### Deal-breakers
- Pure admin or non-creative roles
- Roles with no technical or creative component
- Relocation away from Dublin
- Large, siloed teams; prefer small crews
- Vague briefs without clear direction

## Repo Structure
- `cv/` - Markdown CV variants
- `cover_letters/` - Markdown cover letters
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - Job search CLI tools

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: skills match, experience match, behavioral/culture match. Present this assessment to the user before proceeding.
3. If good fit: create targeted CV (`cv/main_<company>.md`) and cover letter (`cover_letters/cover_<company>_<role>.md`)
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and your strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] CV follows the standard markdown structure from `05-cv-templates.md` and stays within the ~2-page content budget
- [ ] Cover letter follows the markdown template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] Markdown is clean and renders correctly (consistent heading levels, no broken lists, no stray formatting characters)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter body is within the 250-300 word budget (roughly one printed page)
- [ ] CV stays within the ~2-page content budget defined in `05-cv-templates.md`
- [ ] No placeholder tokens or leftover text from source templates remain

---

## Job Search Pipeline (Updated 2026-06-15)

### Overview
A lightweight, two-stage job discovery + tracking system:
1. **Discovery phase** — Find jobs fast, assess quickly, no heavy metadata burden
2. **Tracking phase** — Move promising jobs to Obsidian for full evaluation and application

### Stage 1: Lightweight Discovery (`parse_urls.py` + `parse.bat`)

**Workflow:**
1. Find job URLs on LinkedIn, Indeed, company careers pages
2. Paste URLs into `X:\Vault\Hatch\job-hunt\job-urls.md` (one per line, markdown bullets)
3. Double-click `parse.bat` in jobsearch folder
4. Script auto-installs dependencies, fetches each posting, extracts job details
5. Outputs `parsed-jobs.md` with summary: title, company, location, posting date, requirements
6. Review `parsed-jobs.md` — decide if worth deeper evaluation

**Files:**
- `parse_urls.py` — main parser (uses BeautifulSoup + requests to fetch/parse job postings)
- `parse.bat` — wrapper (activates venv, installs deps, runs parser)
- `requirements-parse.txt` — dependencies (requests, beautifulsoup4)

**Why this approach:**
- No metadata burden upfront (just paste URLs)
- Fast discovery loop (parse.bat takes 2-3 min for 5-10 jobs)
- Filters out uninteresting jobs before heavy evaluation
- Avoids Obsidian YAML frontmatter overhead for discovery phase

### Stage 2: Full Tracking (Obsidian + `sync_jobs.py`)

**Workflow:**
1. If job is interesting from Stage 1, create new note in `X:\Vault\Hatch\job-hunt/`
2. Fill in YAML frontmatter: company, role, status (Interesting → To Apply → Applied → Response), deadline, key_requirements, sector, etc.
3. View progress via Dataview kanban board (`Job Applications Board.md`)
4. When ready, run `sync.bat` to generate `applications.md` and `applications.json` for repo
5. Pass full job note + parsed details to Claude for fit assessment + CV/cover letter drafting

**Files:**
- `sync_jobs.py` — reads Obsidian notes, exports markdown + JSON summaries
- `sync.bat` — wrapper (activates venv, runs sync)
- Obsidian vault as source of truth (YAML frontmatter schema in HANDOFF.md)

**Why split into two stages:**
- Discovery is lightweight (URLs only) — fast feedback loop
- Full tracking has richer metadata — but only for jobs worth pursuing
- Obsidian keeps full history; repo has current sync for Claude to work with

### Job Search Categories (16 Priorities)

Expanded from original 5 to 16 to surface adjacent roles Shem qualifies for:

**Core Technical (Priorities 1-5):**
1. Technical Artist & Motion Designer
2. Creative Technologist & Interactive Designer
3. 3D Generalist / Blender Artist
4. Pipeline / Tools Artist
5. Technical Officer - Moving Image

**Creative & VFX (Priorities 6-11):**
6. VFX Compositor / Compositor (Disney+ Studio Meala credit)
7. Graphic Designer / Brand Motion Designer (BA Visual Comms, Science Gallery)
8. Exhibition / Installation / Experiential Designer (Science Gallery Lifelogging)
9. Product Visualisation / Arch-Viz Artist (Portfolio: Grundig, vehicles, landscapes)
10. Creative Developer / Interactive Developer (Python, JavaScript, React, Three.js, TouchDesigner)
11. AR/VR/XR Artist or Developer (Unreal immersive, real-time workflows)

**Expanded Adjacent Roles (Priorities 12-16):**
12. UX Designer / Interaction Designer (BA UX specialization, JavaScript/React)
13. Web Designer / Interactive Designer (Three.js, React, interactive web)
14. Character Designer / Rigging Artist (Blender Rigify, character modeling)
15. Environment Artist / World Builder (Procedural modeling, asset optimization)
16. Digital Designer / Broadcast Designer / Media Designer (Motion graphics, VFX, advertising)

**Search queries:** See `search-queries.md` for all 16 categories with specific LinkedIn/Indeed site queries.

**Important filters applied to all searches:**
- Location: Dublin or Remote EU only (no relocation)
- Seniority: Mid-level (3-6 years) only — exclude Senior/Lead/Principal
- Date: Last 14 days only (avoid stale postings)
- Adult content: Excluded
- Deal-breakers: No pure admin, non-creative, large siloed teams, vague briefs

### Cold-Call Targets

Companies worth reaching out to directly (even without open postings):

| Company | Sector | Why Interesting |
|---------|--------|-----------------|
| Lifesize Plans Ireland | LIDAR scanning, 3D visualization | Featured on Great House Revival S06 E03; Shem has direct LIDAR scanning experience |
| Windmill Lane | VFX, post-production, compositing | Small team, Disney+/HBO/Netflix credits, Dublin-based |
| Brown Bag Films | Animation, VFX, 3D motion | Hybrid model, technical depth, small studio culture |
| Void Interactive | Games, real-time, Unreal Engine | Remote-first, procedural workflows, immersive design |

**Outreach strategy:** Short, personalized cold email mentioning specific work/show, positioning Shem's relevant skills, open-ended ask about collaboration opportunities.

### Scripts & Tools Created (2026-06-15)

| File | Purpose | Status |
|------|---------|--------|
| `sync.bat` | One-click job sync (Obsidian → repo) | ✓ Working |
| `sync_jobs.py` | Python sync script (YAML → JSON/markdown) | ✓ Working (date serialization fixed) |
| `parse.bat` | One-click URL parser | ✓ Working |
| `parse_urls.py` | Fetch + parse job postings from URLs | ✓ Working (syntax fixed) |
| `requirements-parse.txt` | Dependencies for parse_urls.py | ✓ Created |
| `job-queue.md` | [Deprecated] was going to use, switched to Obsidian | — |
| `cold-call-targets.md` | Company list for direct outreach | ✓ In use |
| `search-queries.md` | 16 job search categories + filters | ✓ Updated |

### Next Steps for Claude (in future sessions)

When user brings job postings:
1. **Check source:** Is it from `parsed-jobs.md` (Stage 1) or Obsidian sync (Stage 2)?
2. **If Stage 1:** Quick yes/no on whether it's worth moving to Obsidian
3. **If Stage 2:** Do full fit assessment, draft tailored CV + cover letter
4. **If cold-call:** Help craft personalized outreach email

**Critical success factor:** Only evaluate jobs with real, verifiable, current URLs. Avoid stale postings (like the 6-year-old Piranha Bar compositor role that came up early).

### Known Limitations & Future Improvements

- **URL parser:** Extracting job details from HTML is fragile (site structure varies). Parser does best-effort; may need manual extraction for complex sites.
- **Dataview kanban:** Requires Dataview plugin installed + enabled in Obsidian. If not set up, use the markdown summaries from sync instead.
- **Seniority/date filters:** Applied at search-query level, but URLs must still be manually verified to avoid expired postings.
- **No CV/cover letter export yet:** We generate tailored CVs in repo; still need workflow to sync back to Obsidian if needed.

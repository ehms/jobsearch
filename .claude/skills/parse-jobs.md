# Job URL Parser Skill

**name:** parse-jobs
**description:** Parse job URLs from Obsidian vault and generate parsed-jobs.md summary
**trigger-phrases:** /parse, parse jobs, parse urls
**allowed-tools:** Bash, Read, Write

---

## How It Works

1. Reads job URLs from `X:\Vault\Hatch\job-hunt\job-urls.md`
2. Runs `parse.bat` to fetch and parse each job posting
3. Generates `parsed-jobs.md` with job details
4. Returns summary of parsed jobs

## Usage

```
/parse
```

Done! Jobs will be parsed and summary available in `parsed-jobs.md`.

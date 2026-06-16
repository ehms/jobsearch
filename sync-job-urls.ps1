# Job URLs Sync Script
# Pulls new job URLs from GitHub repo and merges into Obsidian job-urls.md

param(
    [string]$JobsRepoPath = "C:\repos\jobs",
    [string]$ObsidianJobUrlsPath = "X:\Vault\Hatch\job-hunt\job-urls.md.md"
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Job URLs Sync" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Clone or pull the jobs repo
if (-not (Test-Path $JobsRepoPath)) {
    Write-Host "Cloning jobs repo..." -ForegroundColor Yellow
    git clone https://github.com/ehms/jobs $JobsRepoPath
} else {
    Write-Host "Pulling latest from jobs repo..." -ForegroundColor Yellow
    Push-Location $JobsRepoPath
    git pull
    Pop-Location
}

# Read URLs from jobs/urls.md
$jobsUrlsFile = Join-Path $JobsRepoPath "jobs\urls.md"
if (-not (Test-Path $jobsUrlsFile)) {
    Write-Host "No jobs/urls.md found in repo yet. Nothing to sync." -ForegroundColor Yellow
    exit 0
}

$jobsUrls = Get-Content $jobsUrlsFile -Raw

# Extract URLs (lines starting with -)
$newUrls = $jobsUrls -split "`n" | Where-Object { $_ -match "^-\s+https?://" }

if ($newUrls.Count -eq 0) {
    Write-Host "No URLs found in jobs/urls.md. Nothing to sync." -ForegroundColor Yellow
    exit 0
}

Write-Host "Found $($newUrls.Count) URL(s) in jobs repo" -ForegroundColor Green

# Read current Obsidian file
if (-not (Test-Path $ObsidianJobUrlsPath)) {
    Write-Host "ERROR: job-urls.md not found at $ObsidianJobUrlsPath" -ForegroundColor Red
    exit 1
}

$obsidianContent = Get-Content $ObsidianJobUrlsPath -Raw

# Find Job Postings section and extract existing URLs
$postingsSection = $obsidianContent -match '## Job Postings[\s\S]*?(?=## Cold-Call|$)' | ForEach-Object {
    $_ -split "`n" | Where-Object { $_ -match "^-\s+https?://" }
}

$existingUrls = @($postingsSection)
Write-Host "Found $($existingUrls.Count) existing URL(s) in job-urls.md" -ForegroundColor Green

# Extract just the URLs for duplicate checking
$existingUrlStrings = $existingUrls | ForEach-Object {
    if ($_ -match "(https?://[^\s|]+)") { $matches[1] }
}

# Find new URLs to add
$urlsToAdd = @()
foreach ($urlLine in $newUrls) {
    if ($urlLine -match "(https?://[^\s|]+)") {
        $url = $matches[1]
        if ($url -notin $existingUrlStrings) {
            $urlsToAdd += $urlLine
        }
    }
}

if ($urlsToAdd.Count -eq 0) {
    Write-Host "No new URLs to add (all already present)." -ForegroundColor Yellow
    exit 0
}

Write-Host "Adding $($urlsToAdd.Count) new URL(s)..." -ForegroundColor Cyan

# Insert new URLs into Job Postings section
$updatedContent = $obsidianContent -replace `
    "(## Job Postings \(to parse with \/parse\))", `
    "`$1`n`n$($urlsToAdd -join "`n")"

# Write back to file
Set-Content $ObsidianJobUrlsPath -Value $updatedContent -Encoding UTF8

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "SYNC COMPLETE" -ForegroundColor Green
Write-Host "Added: $($urlsToAdd.Count) new URL(s)" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green

foreach ($url in $urlsToAdd) {
    Write-Host "  + $url" -ForegroundColor Green
}

Write-Host "`nUpdated: $ObsidianJobUrlsPath" -ForegroundColor Cyan

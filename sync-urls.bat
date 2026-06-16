@echo off
REM Job URLs Sync Wrapper
REM Run this to sync new job URLs from GitHub repo to Obsidian

cd /d E:\job_applications\jobsearch

powershell -NoProfile -ExecutionPolicy Bypass -File .\sync-job-urls.ps1

echo.
pause

@echo off
REM ============================================================
REM Job Applications Sync Script
REM Syncs Obsidian vault to applications.md and applications.json
REM ============================================================

cd /d E:\job_applications\jobsearch

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found in PATH
    echo Please install Python or add it to your system PATH
    pause
    exit /b 1
)

REM Check for virtual environment and activate if it exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo No venv found - using system Python
)

REM Run the sync script
echo.
echo Running sync_jobs.py...
echo.
python sync_jobs.py

REM Check if sync was successful
if %errorlevel% equ 0 (
    echo.
    echo SUCCESS: Sync complete
    echo Applications summary written to:
    echo   - applications.md
    echo   - applications.json
) else (
    echo.
    echo ERROR: Sync failed with exit code %errorlevel%
)

echo.
pause

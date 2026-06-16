@echo off
REM ============================================================
REM Job URL Parser
REM Parses job URLs from Obsidian, outputs parsed-jobs.md
REM ============================================================

cd /d E:\job_applications\jobsearch

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found in PATH
    pause
    exit /b 1
)

REM Check for virtual environment and activate if it exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Install/upgrade dependencies
echo.
echo Checking dependencies...
python -m pip install -q -r requirements-parse.txt

REM Run the parser
echo.
echo Parsing job URLs...
echo.
python parse_urls.py

echo.
echo Parse complete. Check parsed-jobs.md for results.

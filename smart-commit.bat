@echo off
REM Enhanced commit script that creates descriptive commit messages based on prompts

setlocal enabledelayedexpansion

if "%~1"=="" (
    echo Usage: %0 "commit description based on your prompt"
    echo Example: %0 "Add constitution for Physical AI & Humanoid Robotics book"
    exit /b 1
)

REM Get the commit message from the first argument
set "COMMIT_MSG=%~1"

REM Check if there are staged changes, if not, stage all changes
git diff --cached --quiet
if errorlevel 1 (
    REM There are staged changes, proceed with commit
    echo Committing with message: !COMMIT_MSG!
) else (
    REM No staged changes, stage all and commit
    echo Staging all changes and committing with message: !COMMIT_MSG!
    git add .
)

REM Perform the commit with the descriptive message
git commit -m "!COMMIT_MSG!"

REM The post-commit hook will automatically push the changes
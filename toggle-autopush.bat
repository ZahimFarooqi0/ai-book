@echo off
REM Script to enable or disable auto-push functionality

if "%1"=="enable" (
    git config hooks.autopush true
    echo Auto-push has been ENABLED
    echo The repository will now automatically push changes after each commit
) else if "%1"=="disable" (
    git config hooks.autopush false
    echo Auto-push has been DISABLED
    echo You will need to manually push changes with 'git push'
) else if "%1"=="status" (
    for /f %%i in ('git config hooks.autopush') do set autopush_status=%%i
    if "!autopush_status!"=="true" (
        echo Auto-push is CURRENTLY ENABLED
    ) else (
        echo Auto-push is CURRENTLY DISABLED
    )
) else (
    echo Usage: %0 [enable^|disable^|status]
    echo   enable  - Enable automatic pushing after commits
    echo   disable - Disable automatic pushing (requires manual git push)
    echo   status  - Check current auto-push status
)
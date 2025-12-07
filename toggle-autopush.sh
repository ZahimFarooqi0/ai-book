#!/bin/sh
# Script to enable or disable auto-push functionality

case "$1" in
  "enable")
    git config hooks.autopush true
    echo "Auto-push has been ENABLED"
    echo "The repository will now automatically push changes after each commit"
    ;;
  "disable")
    git config hooks.autopush false
    echo "Auto-push has been DISABLED"
    echo "You will need to manually push changes with 'git push'"
    ;;
  "status")
    STATUS=$(git config hooks.autopush)
    if [ "$STATUS" = "true" ]; then
      echo "Auto-push is CURRENTLY ENABLED"
    else
      echo "Auto-push is CURRENTLY DISABLED"
    fi
    ;;
  *)
    echo "Usage: $0 [enable|disable|status]"
    echo "  enable  - Enable automatic pushing after commits"
    echo "  disable - Disable automatic pushing (requires manual git push)"
    echo "  status  - Check current auto-push status"
    ;;
esac
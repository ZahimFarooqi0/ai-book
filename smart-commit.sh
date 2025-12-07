#!/bin/sh
# Enhanced commit script that creates descriptive commit messages based on prompts

if [ -z "$1" ]; then
    echo "Usage: $0 \"commit description based on your prompt\""
    echo "Example: $0 \"Add constitution for Physical AI & Humanoid Robotics book\""
    exit 1
fi

COMMIT_MSG="$1"

# Check if there are staged changes, if not, stage all changes
if ! git diff --cached --quiet; then
    # There are staged changes, proceed with commit
    echo "Committing with message: $COMMIT_MSG"
else
    # No staged changes, stage all and commit
    echo "Staging all changes and committing with message: $COMMIT_MSG"
    git add .
fi

# Perform the commit with the descriptive message
git commit -m "$COMMIT_MSG"

# The post-commit hook will automatically push the changes
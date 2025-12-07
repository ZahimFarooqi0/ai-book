#!/usr/bin/env python3
"""
Smart commit script that can analyze prompts and create more descriptive commit messages
"""
import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip(), result.stderr.strip(), 0
    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip(), e.returncode

def analyze_prompt_for_commit_message(prompt):
    """Analyze the prompt to generate a more descriptive commit message"""
    # This is a simple implementation - in a more advanced version, 
    # we could use NLP to better understand the prompt intent
    prompt_lower = prompt.lower()
    
    # Identify common patterns in prompts
    if "add" in prompt_lower or "create" in prompt_lower:
        action = "Add"
    elif "update" in prompt_lower or "modify" in prompt_lower or "change" in prompt_lower:
        action = "Update"
    elif "fix" in prompt_lower or "bug" in prompt_lower:
        action = "Fix"
    elif "remove" in prompt_lower or "delete" in prompt_lower:
        action = "Remove"
    else:
        action = "Update"
    
    # Extract relevant keywords for the commit message
    # This is a simplified approach
    if "constitution" in prompt_lower:
        return f"{action} constitution document for Physical AI & Humanoid Robotics book"
    elif "documentation" in prompt_lower:
        return f"{action} documentation for Physical AI & Humanoid Robotics book"
    elif "feature" in prompt_lower:
        return f"{action} new feature based on prompt"
    else:
        return prompt  # fallback to the original prompt

def main():
    if len(sys.argv) < 2:
        print("Usage: python smart-commit.py \"description of your changes based on prompt\"")
        print("Example: python smart-commit.py \"Add constitution for Physical AI & Humanoid Robotics book\"")
        sys.exit(1)
    
    original_prompt = " ".join(sys.argv[1:])
    commit_message = analyze_prompt_for_commit_message(original_prompt)
    
    # Check if there are staged changes
    stdout, stderr, code = run_command('git diff --cached --quiet')
    
    if code != 0:
        # There are staged changes, proceed with commit
        print(f"Committing with message: {commit_message}")
    else:
        # No staged changes, stage all and commit
        print(f"No staged changes detected. Staging all changes and committing with message: {commit_message}")
        run_command('git add .')
    
    # Perform the commit with the descriptive message
    commit_stdout, commit_stderr, commit_code = run_command(f'git commit -m "{commit_message}"')
    
    if commit_code != 0:
        print(f"Commit failed with error: {commit_stderr}")
        sys.exit(1)
    
    # Show the commit result
    print(commit_stdout)
    if commit_stderr:
        print(commit_stderr)

if __name__ == "__main__":
    main()
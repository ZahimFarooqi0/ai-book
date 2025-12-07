#!/usr/bin/env python3
"""
Script to enable or disable auto-push functionality
"""
import subprocess
import sys

def get_config():
    """Get the current hooks.autopush configuration"""
    try:
        result = subprocess.run(['git', 'config', 'hooks.autopush'], 
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def set_config(value):
    """Set the hooks.autopush configuration"""
    subprocess.run(['git', 'config', 'hooks.autopush', value], check=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: python toggle-autopush.py [enable|disable|status]")
        print("  enable  - Enable automatic pushing after commits")
        print("  disable - Disable automatic pushing (requires manual git push)")
        print("  status  - Check current auto-push status")
        sys.exit(1)

    command = sys.argv[1]

    if command == "enable":
        set_config("true")
        print("Auto-push has been ENABLED")
        print("The repository will now automatically push changes after each commit")
    elif command == "disable":
        set_config("false")
        print("Auto-push has been DISABLED")
        print("You will need to manually push changes with 'git push'")
    elif command == "status":
        config_value = get_config()
        if config_value == "true":
            print("Auto-push is CURRENTLY ENABLED")
        else:
            print("Auto-push is CURRENTLY DISABLED")
    else:
        print(f"Unknown command: {command}")
        print("Usage: python toggle-autopush.py [enable|disable|status]")

if __name__ == "__main__":
    main()
# Auto-Git-Push Automation Setup

This repository now has an automated Git push feature enabled. Any changes you commit will be automatically pushed to the remote repository.

## How It Works

1. The setup uses Git's `post-commit` hook to automatically execute a push command after each commit
2. The hook is located at `.git/hooks/post-commit`
3. A configuration setting `hooks.autopush` controls whether the feature is enabled or disabled
4. The current branch is automatically detected and pushed to the corresponding remote branch

## Enhanced Commit Tools

For more descriptive commit messages based on your prompts, you can use one of these enhanced commit tools:

### Python Smart Commit (Recommended):
```bash
python smart-commit.py "Add constitution for Physical AI & Humanoid Robotics book"
```
This analyzes your prompt and creates an appropriate commit message.

### Batch Smart Commit (Windows):
```bash
smart-commit.bat "Add constitution for Physical AI & Humanoid Robotics book"
```

### Shell Smart Commit (Unix-like environments):
```bash
sh smart-commit.sh "Add constitution for Physical AI & Humanoid Robotics book"
```

## Controlling Auto-Push

You can enable/disable the auto-push functionality using one of these methods:

### Using Python Script (Recommended):
```bash
python toggle-autopush.py enable   # Enable auto-push
python toggle-autopush.py disable  # Disable auto-push
python toggle-autopush.py status   # Check current status
```

### Using Git Config Directly:
```bash
git config hooks.autopush true   # Enable auto-push
git config hooks.autopush false  # Disable auto-push
```

## What Happens When You Make Changes

### Default Process (Auto-push enabled):
1. Edit your files as normal
2. Stage your changes: `git add <files>`
3. Commit your changes: `git commit -m "Your descriptive commit message"`
4. **Automatically**, the post-commit hook will execute `git push origin <current-branch>`
5. Your changes are now on the remote repository

### Enhanced Process (Using Smart Commit):
1. Edit your files as normal
2. Use the smart commit script: `python smart-commit.py "Description based on your prompt"`
   - This will analyze your prompt and create a more descriptive commit message
   - It will automatically stage all changes if none are staged
   - Then commit with the generated message and auto-push

## Important Notes

- **Remote Connection Required**: You need to be connected to the internet and have proper authentication to the remote repository
- **Conflicts**: If there are newer changes on the remote, the push will fail. You'll need to pull the latest changes first
- **Credentials**: Make sure your Git credentials are properly configured (either with SSH keys or credential helper)

## Troubleshooting

If auto-push isn't working:

1. Check if it's enabled: `python toggle-autopush.py status`
2. Verify the hook exists: look for `.git/hooks/post-commit`
3. Make sure you have proper permissions to push to the remote repository

## Disabling Auto-Push

If you need to temporarily disable auto-push:
```bash
python toggle-autopush.py disable
```

To re-enable later:
```bash
python toggle-autopush.py enable
```
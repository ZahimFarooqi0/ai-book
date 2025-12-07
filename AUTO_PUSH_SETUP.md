# Auto-Git-Push Setup

This repository is configured with a Git hook that automatically pushes your committed changes to the remote repository.

## How it Works

After every `git commit`, the post-commit hook will automatically execute `git push origin <current-branch>`, keeping your remote repository in sync with your local commits.

## Enable/Disable Auto-Pushing

### To Enable:
```bash
git config hooks.autopush true
```

### To Disable:
```bash
git config hooks.autopush false
```

By default, the auto-push feature is disabled until you explicitly enable it.

## Important Notes

1. **Authentication**: Make sure your Git credentials are properly configured for pushing to the remote repository (either with SSH keys or credential manager)

2. **Conflicts**: If there are newer changes on the remote, the push may fail. In this case, you'll need to pull the latest changes, resolve any conflicts, and commit again.

3. **Safety**: The hook won't run if you're in a detached HEAD state to prevent accidental loss of commits.

4. **Branch Handling**: The hook detects your current branch and pushes to the corresponding remote branch.

## Manual Override

Even with auto-pushing enabled, you can still perform manual pushes if needed:
```bash
git push origin <branch-name>
```

## Troubleshooting

If the hook doesn't seem to be working:

1. Verify the configuration: `git config hooks.autopush`
2. Check that the hook file exists: `.git/hooks/post-commit`
3. Make sure you've enabled the feature with: `git config hooks.autopush true`
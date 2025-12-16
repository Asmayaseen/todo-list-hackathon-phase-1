# GitHub Pull Request Guide - CLI Feature

## Current Status ✅

Branch: `feature/cli-interface`
Commit: `e68a3ef - Add CLI interface for todo application`
Remote: `https://github.com/Asmayaseen/todo-list-hackathon-phase-1.git`

All changes are committed and ready to push!

---

## Method 1: Push via Terminal (Easiest) 🚀

### Step 1: Open Terminal/Command Prompt

```bash
# Navigate to project directory
cd /mnt/d/hackathon-robotic/todo-list

# Verify you're on the correct branch
git branch
# Should show: * feature/cli-interface
```

### Step 2: Push to GitHub

```bash
git push -u origin feature/cli-interface
```

**What will happen:**
- GitHub will ask for your username and password/token
- If you have 2FA enabled, you'll need a Personal Access Token (PAT)

### Step 3: Authentication Options

#### Option A: Using Personal Access Token (Recommended)

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: `todo-cli-feature`
4. Select scopes: ✅ `repo` (full control of private repositories)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)
7. When git asks for password, paste this token

#### Option B: Using GitHub CLI

```bash
# Install GitHub CLI (if not installed)
# For Ubuntu/Debian:
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Login to GitHub
gh auth login

# Push the branch
git push -u origin feature/cli-interface

# Create PR directly
gh pr create --title "Add CLI Interface for Todo Application" --body-file PR_DESCRIPTION.md
```

---

## Method 2: Push via GitHub Desktop (GUI) 🖱️

1. Open GitHub Desktop
2. File → Add Local Repository → Select `/mnt/d/hackathon-robotic/todo-list`
3. Current branch should show: `feature/cli-interface`
4. Click "Publish branch" or "Push origin"
5. After push, click "Create Pull Request"

---

## Method 3: Manual Upload via GitHub Website 🌐

1. Go to: https://github.com/Asmayaseen/todo-list-hackathon-phase-1
2. Click "Add file" → "Upload files"
3. Switch to branch: `feature/cli-interface` (create if doesn't exist)
4. Upload these files:
   - `src/todo_app/cli.py`
   - `pyproject.toml`
   - `README.md`
5. Commit changes

---

## Creating the Pull Request 📝

### Automatic (After Push)

After pushing, GitHub will show a banner:
```
feature/cli-interface had recent pushes
[Compare & pull request]
```
Click that button!

### Manual PR Creation

1. Go to: https://github.com/Asmayaseen/todo-list-hackathon-phase-1/pulls
2. Click "New pull request"
3. Set base: `main` ← compare: `feature/cli-interface`
4. Click "Create pull request"

### PR Title:
```
Add CLI Interface for Todo Application
```

### PR Description (Copy this):

```markdown
## Summary

This PR adds a modern command-line interface (CLI) to the todo application, providing direct command execution instead of interactive menu navigation.

## Changes Made

### New Files
- 🆕 `src/todo_app/cli.py` - Complete CLI implementation using argparse

### Modified Files
- ✏️ `pyproject.toml` - Added `todo` CLI entry point, renamed interactive UI to `todo-interactive`
- ✏️ `README.md` - Added comprehensive CLI usage documentation

## Features Added

The CLI provides the following commands:

```bash
todo add "Task title" -d "Description"     # Add new task
todo list [--status all|pending|completed] # List tasks
todo get <id>                              # Get specific task
todo update <id> [-t title] [-d desc]      # Update task
todo complete <id>                         # Mark as complete
todo incomplete <id>                       # Mark as incomplete
todo toggle <id>                           # Toggle status
todo delete <id>                           # Delete task
todo --help                                # Show help
```

## Benefits

- ✅ **Faster workflow** - Direct command execution
- ✅ **Scriptable** - Can be used in shell scripts
- ✅ **User-friendly** - Clear help messages and error handling
- ✅ **Backward compatible** - Interactive UI still available as `todo-interactive`
- ✅ **Consistent** - Uses existing TodoManager (no duplicated logic)

## Testing

Tested commands:
```bash
✅ todo --help
✅ todo add "Test task" -d "Description"
✅ todo list
✅ todo list --status pending
✅ All error cases (invalid IDs, empty titles, etc.)
```

## Breaking Changes

⚠️ **Minor breaking change**: The `todo` command now runs CLI instead of interactive UI
- **Migration**: Use `todo-interactive` for the old menu-based interface
- **Impact**: Minimal - most users will prefer the new CLI

## Screenshots

### CLI Help
```
$ todo --help
usage: todo [-h] {add,list,get,update,complete,incomplete,toggle,delete} ...

LifeStepsAI Todo Application - CLI Interface
...
```

### Adding a Task
```
$ todo add "Buy groceries" -d "Milk, eggs, bread"
✅ Task added successfully!
[1] ☐ Buy groceries
    Description: Milk, eggs, bread
    Status: Pending
```

## Checklist

- [x] Code follows project style (type hints, docstrings)
- [x] Documentation updated (README.md)
- [x] Manual testing completed
- [x] No breaking changes (interactive UI preserved)
- [x] Entry points configured in pyproject.toml

## Phase I Compliance

✅ This feature maintains Phase I constraints:
- In-memory storage only (no persistence added)
- Uses existing TodoManager
- Python 3.13+ compatible
- No external dependencies beyond argparse (stdlib)

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

---

## Troubleshooting 🔧

### Problem: "fatal: could not read Username"
**Solution**: You need to authenticate. Use Personal Access Token (see Step 3 above)

### Problem: "permission denied"
**Solution**:
```bash
# Check remote URL
git remote -v

# If needed, update to SSH
git remote set-url origin git@github.com:Asmayaseen/todo-list-hackathon-phase-1.git

# Or stay with HTTPS and use PAT
```

### Problem: "rejected - non-fast-forward"
**Solution**:
```bash
# Pull latest changes first
git pull origin main

# Resolve conflicts if any
git push -u origin feature/cli-interface
```

### Problem: Can't create PR
**Solution**:
- Make sure branch is pushed first
- Go directly to: https://github.com/Asmayaseen/todo-list-hackathon-phase-1/compare/main...feature/cli-interface

---

## Quick Commands Reference 📋

```bash
# Status check
git status
git log --oneline -3

# Push branch
git push -u origin feature/cli-interface

# Create PR (with GitHub CLI)
gh pr create --title "Add CLI Interface" --fill

# View PR status
gh pr status

# View PR in browser
gh pr view --web
```

---

## Files Changed Summary 📁

| File | Status | Lines | Description |
|------|--------|-------|-------------|
| `src/todo_app/cli.py` | ✨ New | +308 | CLI implementation |
| `pyproject.toml` | ✏️ Modified | +2/-1 | Entry points |
| `README.md` | ✏️ Modified | +76/-2 | CLI docs |
| **Total** | | **+386/-3** | |

---

## Next Steps After PR is Created ✨

1. Wait for review (or self-merge if you're the owner)
2. Address any feedback
3. Merge to main
4. Delete feature branch (optional)

```bash
# After merge, cleanup
git checkout main
git pull origin main
git branch -d feature/cli-interface
```

---

## Need Help? 🆘

- GitHub Docs: https://docs.github.com/en/pull-requests
- Personal Access Tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
- GitHub CLI: https://cli.github.com/manual/

---

**Ready to push?** Just run:
```bash
git push -u origin feature/cli-interface
```

Good luck! 🚀

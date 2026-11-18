---
name: git-branch-manager
description: Guide the agent and user in creating, naming, switching, merging, and cleaning up Git branches according to best practices.
---

# Git Branch Manager Skill

Use this skill whenever the user asks to create a new branch, switch branches, clean up old branches, or prepare a branch for merging.

## 1. Branch Naming Conventions
Follow standardized branch naming prefixes:
- `feature/<short-description>`: Net-new functionality or experiments (e.g., `feature/login-form`).
- `bugfix/<issue-name>`: Fixes for defects or unexpected behavior (e.g., `bugfix/typo-fix`).
- `chore/<task-name>`: Tooling, configs, or maintenance tasks (e.g., `chore/update-readme`).

## 2. Common Branch Workflows

### A. Creating and Switching to a New Branch
```bash
git checkout -b <branch-name>
# or modern Git:
git switch -c <branch-name>
```

### B. Listing Active Branches
```bash
git branch -v
```

### C. Merging into Main/Master
1. Switch to the target branch:
   ```bash
   git switch main
   ```
2. Pull latest changes:
   ```bash
   git pull origin main
   ```
3. Merge the feature branch:
   ```bash
   git merge <branch-name>
   ```

### D. Safe Branch Deletion
- Delete branch locally once merged:
  ```bash
  git branch -d <branch-name>
  ```
- Force delete an unmerged experimental branch (only if user confirms):
  ```bash
  git branch -D <branch-name>
  ```

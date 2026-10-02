---
name: git-conflict-resolver
description: Guide the agent on how to detect, analyze, and safely resolve Git merge conflicts in this repository.
---

# Git Conflict Resolver Skill

This skill provides a standardized workflow to detect, inspect, and resolve Git merge conflicts in this project.

## Workflow Steps

### 1. Identify Conflicted Files
- Run `git status` in the terminal.
- Look under the section `Unmerged paths:` to list all files with conflicts.

### 2. Inspect Conflict Markers
Open each conflicted file and identify the sections:
- `<<<<<<< HEAD`: The changes currently on your active branch.
- `=======`: The separator between conflicting versions.
- `>>>>>>> <branch-name>`: The incoming changes from the branch being merged.

### 3. Resolve the Conflict
- Review both sides of the change.
- Keep the desired code (or combine both if needed).
- Delete all conflict marker lines (`<<<<<<<`, `=======`, `>>>>>>>`).

### 4. Stage and Finalize
- Stage the resolved file:
  ```bash
  git add <filename>
  ```
- Check that all conflicts are resolved with `git status`.
- Complete the merge:
  ```bash
  git commit -m "Resolve merge conflict in <filename>"
  ```

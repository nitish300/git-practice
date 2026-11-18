---
name: git-history-undo
description: Guide the agent and user in safely undoing mistakes, discarding uncommitted edits, reverting commits, or using git stash.
---

# Git History Undo Skill

Use this skill whenever the user asks to undo a commit, unstage files, discard local changes, stash work in progress, or recover lost work.

## 1. Quick Decision Matrix

| Situation | Recommended Command | Data Loss Risk? |
| :--- | :--- | :--- |
| Temporarily set aside uncommitted work | `git stash` | No (stored safely in stash) |
| Restore stashed work | `git stash pop` | No |
| Unstage a file without losing code edits | `git restore --staged <file>` | No |
| Discard uncommitted changes in working tree | `git restore <file>` | **Yes** (uncommitted edits erased) |
| Undo last commit but keep edits staged | `git reset --soft HEAD~1` | No |
| Undo last commit and unstage edits | `git reset HEAD~1` | No |
| Safely reverse a commit already pushed | `git revert <commit-hash>` | No (creates an opposite commit) |

## 2. Safety Rules
1. **Never** run `git reset --hard` without clearly warning the user that uncommitted changes will be permanently lost.
2. If changes were accidentally lost, inspect `git reflog` to recover orphaned commit hashes.

---
name: git-commit-styler
description: Guide the agent to compose atomic, well-formatted Conventional Commit messages and review staged changes before committing.
---

# Git Commit Styler Skill

Use this skill whenever the user is ready to commit changes, asks for help writing a commit message, or wants to follow Conventional Commits format.

## 1. Commit Message Structure
All commit messages must follow the Conventional Commits format:
```text
<type>(<optional-scope>): <concise description in imperative mood>

[optional body explaining 'why' and context]
```

### Commit Types
- `feat`: A new feature or functionality.
- `fix`: A bug fix.
- `docs`: Documentation-only updates (README, guides).
- `style`: Formatting, missing semicolons, white-space changes.
- `refactor`: Code change that neither fixes a bug nor adds a feature.
- `test`: Adding or correcting tests.
- `chore`: Maintenance, updating build scripts or package dependencies.

## 2. Review and Stage Workflow
1. Check what has changed:
   ```bash
   git diff
   ```
2. Check staged vs unstaged status:
   ```bash
   git status
   ```
3. Stage specific files:
   ```bash
   git add <filename>
   ```
4. Commit with a meaningful message:
   ```bash
   git commit -m "feat(auth): add email validation check"
   ```

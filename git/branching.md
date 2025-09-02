# 🌿 Git Branching

## 📜 What is a Git Branch?  
A branch is a lightweight movable pointer to a commit. It allows parallel development, feature isolation, and safer collaboration.

---

## 🔧 Basic Commands

```bash
# Create a new branch
git branch feature/new-feature

# Switch to a branch
git checkout feature/new-feature

# Create and switch
git checkout -b feature/new-feature

# List all local branches
git branch

# Delete local branch
git branch -d feature/new-feature

# Merge branch into current
git merge feature/new-feature

# Push branch to GitHub
git push origin feature/new-feature

# Delete branch from GitHub
git push origin --delete feature/new-feature
```

---

## 🌐 Working with Branches in Teams

Using branches is a core part of collaborative development.

- `main` / `master` — main stable branch
- `feature/xxx` — branches for new features
- `bugfix/xxx` — branches for fixing bugs
- `hotfix/xxx` — branches for urgent fixes
- `experiment/xxx` — experimental branches

Use pull requests (PR) to merge into `main` safely.

Many teams follow [GitHub Flow](https://guides.github.com/introduction/flow/).

---

## 💡 Tips

- Always pull before creating a new branch.
- Use clear names like `feature/login-form`.
- One task = one branch.
- Remove merged branches.
- Don't push broken code to shared branches.

---

📁 Back to [Git Basics](./basics.md)

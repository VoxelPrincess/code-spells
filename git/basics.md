# 🌐 Git Basics

A practical guide to using Git — a version control system used by developers worldwide.

---

## 🧰 Installation

### 🐧 Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install git
```

### 💻 macOS:

```bash
brew install git
```

### ✅ Check installation:

```bash
git --version
```

---

## 🔑 Key Git Commands

| Command                        | Description                                  |
|--------------------------------|----------------------------------------------|
| `git init`                     | Initialize a new repository                  |
| `git clone <url>`              | Clone an existing repository                 |
| `git status`                   | Show changes and tracked files               |
| `git add <file>`               | Stage a file for commit                      |
| `git commit -m "msg"`          | Save changes with a message                  |
| `git push`                     | Push changes to remote repo                  |
| `git pull`                     | Get latest changes from remote               |
| `git log`                      | Show commit history                          |
| `git diff`                     | Show file differences                        |

---

## 🌿 Branching

| Command                           | Description                                 |
|-----------------------------------|---------------------------------------------|
| `git branch`                      | List branches                               |
| `git branch <name>`               | Create a new branch                         |
| `git checkout <branch>`           | Switch to a branch                          |
| `git checkout -b <branch>`        | Create and switch to a branch               |
| `git merge <branch>`              | Merge a branch into the current one         |
| `git branch -d <branch>`          | Delete a branch                             |

---

## ❌ Undoing Changes

| Command                              | Description                                  |
|--------------------------------------|----------------------------------------------|
| `git checkout -- <file>`             | Discard local changes                        |
| `git restore <file>`                 | Restore a file to the last commit            |
| `git reset HEAD <file>`              | Unstage a file                               |
| `git revert <commit>`                | Create a commit that undoes a previous commit|
| `git reset --hard <commit>`          | Reset to a specific commit (dangerous)       |

---

## 📁 .gitignore

### What is `.gitignore`?

Files listed in `.gitignore` are not tracked by Git.

### Example contents:

```
node_modules/
.env
.DS_Store
*.log
dist/
```

### Commit `.gitignore`

```bash
git add .gitignore
git commit -am ".gitignore"
git status     # Check the output
git push       # Push if everything is OK
```

---

## 🌱 Fork & Pull Request

### 🔁 Fork

A **fork** is a copy of a repository that you manage. You can propose changes without affecting the original.

```bash
# Add original repo as upstream
git remote add upstream https://github.com/original/repo.git

# Fetch changes from upstream
git fetch upstream
git merge upstream/main
```

---

### 🔃 Pull Request

A **Pull Request** is a way to propose changes to the original repository.

1. Create a new branch:

```bash
git checkout -b feature/your-feature
```

2. Make changes and commit:

```bash
git add .
git commit -m "Add new feature"
git push origin feature/your-feature
```

3. On GitHub, open a **Pull Request**.

---

## 💡 Tips

- Work in branches, not directly in `main`.
- Write clear commit messages.
- Use `.gitignore` to exclude temporary and sensitive files.
- Use `git status` often to avoid surprises.
- Sync your fork regularly with the original repo.

---

📘 *File: `git/basics.md`*

```bash
# To use:
git clone https://github.com/yourname/yourrepo.git
cd yourrepo
code .
```

- [README](../README.md)
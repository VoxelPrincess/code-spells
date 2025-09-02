# 🖥️ GitHub CLI

**GitHub CLI** is a command-line tool for interacting with GitHub without leaving the terminal.

---

## 📦 Installation

### macOS (Homebrew)

```bash
brew install gh
```

### Linux (Debian/Ubuntu)

```bash
type -p curl >/dev/null || sudo apt install curl

curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg |
  sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg

sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" |
  sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

sudo apt update
sudo apt install gh
```

---

## ✅ Authentication

```bash
gh auth login
```

Runs an interactive setup to log into your GitHub account using HTTPS or SSH.

---

## 🔄 Common Commands

```bash
gh repo clone user/repo   # Clone a repo
gh issue list             # List issues
gh pr list                # List pull requests
gh pr create              # Create a new pull request
gh pr checkout 123        # Checkout PR by number
gh auth status            # Check login status
```

---

## 🌐 GitHub CLI & .gitignore

If you're using `gh` to manage repos, don't forget to configure `.gitignore` properly.

```bash
echo "node_modules" >> .gitignore
echo ".env" >> .gitignore

git add .gitignore
git commit -am ".gitignore added"
git push
```

---

## 💡 Bonus: Fork & Pull Request

- Use `gh repo fork` to fork a repository.
- Use `gh pr create` to open a pull request from your fork.

---

🧠 Use `gh help` to see all available commands.

- [README](../README.md)
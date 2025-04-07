# 🌐 Git Basics / Основы Git

Практическое руководство по работе с Git — системой контроля версий, которую используют разработчики по всему миру.

---

## 🧰 Installation / Установка

### 🐧 Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install git
```

### 💻 macOS:

```bash
brew install git
```


### ✅ Check installation / Проверка установки:

```bash
git --version
```

---

## 🔑 Key Git Commands / Основные команды Git

| Command                        | Description (EN)                                  | Описание (RU)                               |
|-------------------------------|---------------------------------------------------|---------------------------------------------|
| `git init`                    | Initialize a new repository                       | Инициализировать новый репозиторий          |
| `git clone <url>`             | Clone an existing repository                      | Клонировать репозиторий                     |
| `git status`                  | Show changes and tracked files                    | Показать статус файлов                      |
| `git add <file>`              | Stage a file for commit                          | Добавить файл к коммиту                     |
| `git commit -m "msg"`         | Save changes with a message                      | Сохранить изменения с сообщением            |
| `git push`                    | Push changes to remote repo                      | Отправить изменения на сервер               |
| `git pull`                    | Get latest changes from remote                   | Получить и слить изменения                  |
| `git log`                     | Show commit history                              | Показать историю коммитов                   |
| `git diff`                    | Show file differences                            | Показать отличия в файлах                   |

---

## 🌿 Branching / Работа с ветками

| Command                           | Description (EN)                    | Описание (RU)                             |
|----------------------------------|-------------------------------------|-------------------------------------------|
| `git branch`                     | List branches                       | Показать список веток                     |
| `git branch <name>`              | Create a new branch                 | Создать новую ветку                       |
| `git checkout <branch>`          | Switch to a branch                  | Переключиться на ветку                    |
| `git checkout -b <branch>`       | Create and switch to a branch       | Создать и переключиться на ветку         |
| `git merge <branch>`            | Merge a branch into current one     | Слить ветку в текущую                     |
| `git branch -d <branch>`         | Delete a branch                     | Удалить ветку                             |

---

## ❌ Undoing Changes / Отмена изменений

| Command                              | Description (EN)                                  | Описание (RU)                               |
|-------------------------------------|---------------------------------------------------|---------------------------------------------|
| `git checkout -- <file>`           | Discard local changes                             | Отменить изменения в файле                  |
| `git restore <file>`               | Restore a file to last commit                     | Восстановить файл                          |
| `git reset HEAD <file>`            | Unstage a file                                    | Убрать файл из индекса                     |
| `git revert <commit>`              | Create a commit that undoes a previous commit     | Создать коммит, отменяющий предыдущий       |
| `git reset --hard <commit>`        | Reset to a specific commit (dangerous)            | Жёсткий откат до определённого коммита      |

---

## 📁 .gitignore

### What is `.gitignore`?

Files listed in `.gitignore` are not tracked by Git.  
Файлы, указанные в `.gitignore`, игнорируются Git и не попадают в репозиторий.

### Example contents / Пример содержимого:

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
**Fork** — это копия чужого репозитория, в которую вы можете вносить изменения, не затрагивая оригинал.

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
**Pull Request** — это запрос на внесение изменений в оригинальный проект.

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

## 💡 Tips / Полезные советы

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
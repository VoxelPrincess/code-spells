# Branching# 🌿 Git Branching

## 📜 What is a Git Branch?  
A branch is a lightweight movable pointer to a commit. It allows parallel development, feature isolation, and safer collaboration.  
Ветка — это легковесный указатель на коммит. Позволяет параллельную разработку, изоляцию фич и безопасную совместную работу.

---

## 🔧 Basic Commands / Основные команды

```bash
# Create a new branch / Создать новую ветку
git branch feature/new-feature

# Switch to a branch / Переключиться на ветку
git checkout feature/new-feature

# Create and switch / Создать и сразу переключиться
git checkout -b feature/new-feature

# List all local branches / Показать все локальные ветки
git branch

# Delete local branch / Удалить локальную ветку
git branch -d feature/new-feature

# Merge branch into current / Слить ветку в текущую
git merge feature/new-feature

# Push branch to GitHub / Отправить ветку на GitHub
git push origin feature/new-feature

# Delete branch from GitHub / Удалить ветку на GitHub
git push origin --delete feature/new-feature
```

---

## 🌐 Working with Branches in Teams / Работа с ветками в команде

Using branches is a core part of collaborative development.  
Использование веток — важная часть командной разработки.

- `main` / `master` — main stable branch / основная стабильная ветка
- `feature/xxx` — branches for new features / ветки для новых функций
- `bugfix/xxx` — branches for fixing bugs / ветки для исправления багов
- `hotfix/xxx` — branches for urgent fixes / ветки для срочных исправлений
- `experiment/xxx` — experimental branches / экспериментальные ветки

Use pull requests (PR) to merge into `main` safely.  
Используйте pull request для безопасного слияния в `main`.

Many teams follow [GitHub Flow](https://guides.github.com/introduction/flow/).  
Многие команды используют GitHub Flow.

---

## 💡 Tips / Советы

- Always pull before creating a new branch / Всегда делай `git pull` перед созданием новой ветки  
- Use clear names like `feature/login-form` / Используй понятные имена типа `feature/login-form`  
- One task = one branch / Одна задача — одна ветка  
- Remove merged branches / Удаляй слитые ветки  
- Don't push broken code to shared branches / Не пушь нерабочий код в общие ветки  

---

📁 Back to [Git Basics](./basics.md)

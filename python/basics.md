# 🐍 Python Basics / Основы Python

Практическое руководство по основам языка программирования Python.

---

## 📥 Installation / Установка


### Linux (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### macOS:
```bash
brew install python
```

---

## 🧠 Key Concepts / Ключевые понятия

- **Variable** — a container for storing data / переменная — контейнер для хранения данных.
- **Function** — reusable block of code / функция — многократно используемый блок кода.
- **List** — ordered, mutable collection / список — упорядоченная изменяемая коллекция.
- **Tuple** — ordered, immutable collection / кортеж — упорядоченная неизменяемая коллекция.
- **Dictionary** — key-value pairs / словарь — пары ключ-значение.
- **Loop** — repeat a block of code / цикл — повторение блока кода.
- **Condition** — branching logic (if/else) / условие — логика ветвления.
- **Module** — file containing Python definitions / модуль — файл с определениями на Python.

---

## ✍️ Syntax Examples / Примеры синтаксиса

### Hello World:
```python
print("Hello, world!")
```

### Variables and Types:
```python
name = "Anna"
age = 40
height = 1.65
```

### List:
```python
colors = ["red", "green", "blue"]
colors.append("purple")
```

### Dictionary:
```python
person = {"name": "Anna", "age": 40}
print(person["name"])
```

### Function:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Anna"))
```

### Condition:
```python
if age > 18:
    print("Adult")
else:
    print("Minor")
```

### Loop:
```python
for color in colors:
    print(color)
```

---

## 📚 Further Topics / Дополнительные темы

- Working with files (`open`, `read`, `write`)
- Exception handling (`try`, `except`)
- Using external libraries (`pip install`)
- Virtual environments (`venv`)
- Object-Oriented Programming (OOP)

---

## ✅ Practice Tip / Советы по практике

- Practice short scripts daily
- Use Python Tutor (pythontutor.com) to visualize code
- Try small challenges on sites like LeetCode, HackerRank, or Replit

---

- [README](../README.md)
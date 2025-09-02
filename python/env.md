# Python Virtual Environments

How to create and use virtual environments in Python.

# 📝 Cheatsheet: How to Create a Project with Separate `venv`

---

## 📦 When to Use
- Each **separate project** should have **its own virtual environment (`venv`)**.
- To keep project libraries **isolated**.
- To make projects portable and easy to maintain.

---

## 🛠️ Steps for Every New Project

1. **Go to your main repository folder** (e.g., `coding_school/`):

   ```bash
   cd ~/projects/coding_school
   ```

2. **Create a folder for the new project**:

   ```bash
   mkdir project_name
   cd project_name
   ```

3. **Create a virtual environment inside this folder**:

   ```bash
   python3 -m venv venv
   ```

   🔹 Why `venv` twice?
   - First `venv` = Python module to create virtual environments.
   - Second `venv` = The folder name for your environment (you can name it anything, but `venv` is common).

4. **Activate the virtual environment**:

   ```bash
   source venv/bin/activate
   ```

5. **Install necessary libraries**:

   ```bash
   pip install requests
   pip install Pillow
   ```

6. **Save installed libraries into `requirements.txt`**:

   ```bash
   pip freeze > requirements.txt
   ```

7. **Create your main code file**:

   ```bash
   touch main.py
   ```

8. **Check your `.gitignore` at repository root**:  
   Add this line:

   ```bash
   */venv/
   ```

   To make sure Git does **not track** your `venv` folders.

---

## 📍 Example Project Structure

```
coding_school/
├── .gitignore
├── project1/
│   ├── venv/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── project2/
│   ├── venv/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
```

---

# 🧠 Quick Reference Table

| Action                  | Command |
|:-------------------------|:--------|
| Create a new project     | `mkdir project_name` |
| Create a new venv        | `python3 -m venv venv` |
| Activate the venv        | `source venv/bin/activate` |
| Install libraries        | `pip install ...` |
| Save dependencies        | `pip freeze > requirements.txt` |
| Protect venv in Git      | Add `*/venv/` to `.gitignore` |

---

# ✨ SUMMARY

**One project → One folder → One venv → One requirements.txt**

Stay organized and professional!
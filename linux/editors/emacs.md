# 📝 GNU Emacs

## 🔹 1. Definition  
**GNU Emacs** is a highly extensible and customizable text editor, built on Emacs Lisp. It's used for coding, writing, terminal emulation, and more.

## 🔹 2. Installation  
```bash
sudo apt install emacs
```

## 🔹 3. Help and Learning  
- `man emacs` — manual page  
- `emacs --help` — command line help  
- [GNU Emacs Manual](https://www.gnu.org/software/emacs/manual/)  
- [Emacs Wiki](https://www.emacswiki.org/)  

## 🔹 4. Launching Emacs  
```bash
emacs filename.txt
```
Or simply launch `emacs` to start in GUI or terminal mode (depending on your setup).

## 🔹 5. Key Commands

| Key Combination       | Action                       |
|------------------------|------------------------------|
| `Ctrl + x Ctrl + f`    | Open file                    |
| `Ctrl + x Ctrl + s`    | Save file                    |
| `Ctrl + x Ctrl + c`    | Exit Emacs                   |
| `Ctrl + g`             | Cancel current command       |
| `Alt + x`              | Run a command (M-x)          |
| `Ctrl + _`             | Undo                         |
| `Ctrl + s`             | Search forward               |
| `Ctrl + r`             | Search backward              |
| `Ctrl + k`             | Cut (kill) line              |
| `Ctrl + y`             | Paste (yank)                 |

## 🔹 6. Modes and Buffers  
- Emacs opens files in **buffers** (in-memory representations).  
- It uses **major modes** for file types and **minor modes** for features (like line numbers).  
- Examples: `python-mode`, `text-mode`, `fundamental-mode`

## 🔹 7. Package Management  
Emacs supports built-in package installation via `M-x list-packages`.  
Popular package managers:
- **ELPA** (default)
- **MELPA** (community)
- **Straight.el**

To install packages, use:
```emacs-lisp
M-x list-packages
```

## 🔹 8. Configuration  
Your config file is located at:
```bash
~/.emacs
# or
~/.emacs.d/init.el
```
Written in **Emacs Lisp**, this file customizes everything: key bindings, themes, plugins, behaviors.

## 🔹 9. Exit  
```emacs-lisp
Ctrl + x Ctrl + c   # save and quit
```
# Linux CLI Essentials

Essential commands for working with the Linux command line.

### 📅 Date: 04.04.2025

---

## 🔹 1. Terminal
A text-based interface to interact with the shell.  

---

---

## 🔹 2. Shell
A program that interprets and runs user commands in the terminal.  

```bash
echo $SHELL
bash
```

---

---

## 🔹 3. Installing CLI Tools
How to install key tools for Linux terminal work.  

```bash
sudo apt install vim neovim emacs tree jq graphviz htop sed gzip python3
```

---

---

## 🔹 4. System Maintenance Commands
Useful daily commands for keeping your Linux system up-to-date and clean.  

```bash
sudo apt update && sudo apt upgrade
```
- `sudo apt update` — Updates the list of available packages.  
  Обновляет список доступных пакетов.
- `sudo apt upgrade` — Installs the latest versions of installed packages.  
  Устанавливает последние версии установленных программ.

```bash
sudo apt remove package-name
```
- Removes the specified package from the system.  
  Удаляет указанный пакет из системы.

```bash
sudo apt autoremove
```
- Removes unused dependencies and old package remnants.  
  Удаляет неиспользуемые зависимости и остатки от старых пакетов.

📌 It is recommended to run these commands regularly (e.g., daily or weekly) to keep your system clean and secure.

---

## 🔹 5. Files and Directories (Viewing and Navigation)
Everything in Linux is a file or directory.  

```bash
pwd                  # Print current working directory
ls                   # List directory contents (short format)
ls -l                # Long format: permissions, owner, group, size, date, filename
ls -lrt              # Long format + sorted by time (most recent last)
tree -L 2            # Show directory structure as a tree, limited to 2 levels
```

### 🔸 `ls` options explained:
- `-l` — long format with detailed file info (permissions, size, date).  
- `-r` — reverse order (e.g. oldest files first).  
- `-t` — sort by modification time, newest first.  
- Other useful options:  
  - `-a` — show all files, including hidden (`.` prefix)  
  - `-h` — human-readable sizes (`ls -lh`)

---

---

## 🔹 6. Permissions
Rules that define who can read, write, or execute a file.  

```bash
ls -l
chmod 755 folder
```

- `r` — read permission
- `w` — write permission
- `x` — execute permission
- `d` — directory (if the first character in `ls -l` — `d`)

Example: `drwxr-xr-x`
- `d` — directory
- `rwx` — owner: read, write, execute
- `r-x` — group: read, execute
- `r-x` — others: read, execute

---

---

## 🔹 7. Root User & sudo
The most powerful user with full access to the system.  

```bash
sudo apt update
```

---

---

## 🔹 8. User and Group Management
Managing users and assigning them to groups for permissions.  

```bash
groups                  # Show groups for current user
groups username         # Show groups for another user
sudo usermod -aG sudo username     # Add user to sudo group
sudo gpasswd -d username sudo      # Remove user from sudo group
getent group sudo                  # List all members of sudo group
```

---

---

## 🔹 9. Useful Shortcuts
Shortcuts to navigate and control the terminal efficiently.  

```bash
history
history | less
Ctrl+D     # exit shell or Python
```

---

---

## 🔹 10. Searching Command History with `grep`
Search for specific commands you've used in your history.  

```bash
history | grep vim
history | grep sudo
history | grep install
```

---

---

## 🔹 11. Vim / Neovim / Emacs

**Install:**
```bash
sudo apt install emacs
```

**Install:**
```bash
sudo apt install neovim
```

**Install:**
```bash
sudo apt install vim
```
Terminal-based text editors used to write and edit code or configuration files.  

```bash
vim file.txt
nvim file.txt
emacs file.txt
```

```vim
i       # insert mode
Esc     # back to command mode
:wq     # save and quit
:q!     # quit without saving
```

---

---

## 🔹 12. sed

**Install:**
```bash
sudo apt install sed
```
A stream editor used to find and replace text in files.  

```bash
sed 's/old/new/' file.txt
sed -i 's/old/new/g' file.txt
```

---

---

## 🔹 13. jq

**Install:**
```bash
sudo apt install jq
```
A command-line tool for processing and formatting JSON data.  

```bash
jq '.key' file.json
jq 'keys' file.json
jq '.users[].name' file.json
```

---

---

## 🔹 14. tree

**Install:**
```bash
sudo apt install tree
```
Displays the directory structure in a tree format.  

```bash
tree -L 2
```

- `-L` — limit display depth to N levels (e.g., 2)
- `-a` — show all files (including hidden)
- `-d` — only show directories

---

---

## 🔹 15. gzip / gunzip / tar
Tools for compressing and decompressing files.  

```bash
gzip file.txt
gunzip file.txt.gz
tar -czvf archive.tar.gz folder/
tar -xzvf archive.tar.gz
```

---

---

## 🔹 16. Graphviz / digraph

**Install:**
```bash
sudo apt install graphviz
```
A tool for visualizing graphs described in DOT language.  

```dot
digraph authn {
  A -> B
  B -> C
}
```

```bash
dot -Tpng file.dot -o output.png
```

---

---

## 🔹 17. Python 3
A popular and easy-to-learn programming language.  

```bash
python3
print("Hello")
Ctrl+D   # exit
```

---

---

## 🔹 18. Networking with nmcli

**Install:**
```bash
nmcli is included in the network-manager package (default on Debian)
```
A command-line tool to manage network connections.  

```bash
nmcli connection show
```

---
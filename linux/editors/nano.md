# Nano Editor

Nano is a simple and user-friendly text editor for Linux.

## 🔹 1. Definition  
**Nano** is a simple, user-friendly command-line text editor designed for ease of use. It’s often the default editor in many Linux distributions.

## 🔹 2. Installation  
```bash
sudo apt install nano
```

## 🔹 3. Help and Learning  
- `man nano` — manual page  
- `nano --help` — quick help in terminal  
- [GNU Nano Docs](https://www.nano-editor.org/docs.php)

## 🔹 4. Launching Nano  
```bash
nano filename.txt
```

If the file does not exist, it will be created when saved.

## 🔹 5. Key Commands

| Key             | Action              |
|------------------|---------------------|
| `Ctrl + O`       | Write (save) file   |
| `Ctrl + X`       | Exit nano           |
| `Ctrl + G`       | Show help menu      |
| `Ctrl + K`       | Cut line            |
| `Ctrl + U`       | Paste line          |
| `Ctrl + C`       | Show cursor position|
| `Ctrl + W`       | Search text         |
| `Alt + U`        | Undo                |
| `Alt + E`        | Redo                |

## 🔹 6. Basic Editing  
- Start typing to insert text.  
- Use arrow keys to move the cursor.  
- Use Ctrl-based shortcuts shown at the bottom two lines of the nano screen.

## 🔹 7. Search and Replace  
To search:
```bash
Ctrl + W → type text → Enter
```
To replace (after search):
```bash
Ctrl + \ → type search → Enter → type replace → Enter
```

## 🔹 8. UI Preview  
![Nano screenshot](https://upload.wikimedia.org/wikipedia/commons/4/4b/Gnu-nano.png)  
Screenshot from Wikipedia: a basic Nano editing session

## 🔹 9. Exit  
```bash
Ctrl + X   # exit
Ctrl + O   # save (when prompted)
```
# Vim Editor

Vim is a powerful and highly configurable text editor for Linux.

## 🔹 1. Definition  
**Vim** is a modal command-line text editor based on vi.  

## 🔹 2. Installation  
```bash
sudo apt install vim
```


## 🔹 3. Help and Learning  
- `man vim` — manual page  
- `vimtutor` — interactive tutorial for beginners  
- [Vim Wiki](https://vim.fandom.com/wiki/Vim_Tips_Wiki) — community tips  
- [Vim Manual](https://vimhelp.org/) — full reference  
- [Vim on Wikipedia](https://en.wikipedia.org/wiki/Vim_(text_editor)) — history and features


## 🔹 4. Modes  

| Mode         | Description             | How to enter | How to leave |
|--------------|-------------------------|--------------|--------------|
| Normal       | For commands/navigation | (default)    | —            |
| Insert       | For editing text        | `i`, `a`     | `Esc`        |
| Visual       | For selection           | `v`, `V`     | `Esc`        |
| Command-line | For `:w`, `:q`, search  | `:`          | `Enter`/`Esc`|

## 🔹 5. Navigation  
Use these keys for efficient movement:  
```
h ←   j ↓   k ↑   l →
```

You can also use the arrow keys: ↑ ↓ ← →

Other movement commands:
```vim
gg       # go to beginning of file
G        # go to end of file
0        # go to beginning of line
$        # go to end of line
w / b    # move by word forward/backward
```

## 🔹 6. Common Commands  
```vim
:q        # quit
:q!       # quit without saving
:w        # save
:wq       # save and quit
:w file   # save to file
:enew     # open a new empty file
```

## 🔹 7. Editing and Selection  
```vim
i         # insert before cursor
v / V     # visual mode (char / line)
y         # yank (copy)
p         # paste after cursor
d         # delete (e.g. dd = delete line)
u         # undo
Ctrl+r    # redo
```

## 🔹 8. Search and Replace  
```vim
/word         # search forward
n             # next result
N             # previous result

:%s/old/new/g       # replace all
:s/old/new/         # replace in current line
```

**Regular Expressions supported** — [What is Regex?](https://en.wikipedia.org/wiki/Regular_expression)

## 🔹 9. Exit  
Press `Esc` to return to normal mode, then use:  
```vim
:q       # quit
:q!      # quit without saving
:w       # save
:wq      # save and quit
```
# 📝 Neovim

## 🔹 1. Definition  
**Neovim** is a modern fork of Vim that focuses on extensibility and usability. It supports asynchronous plugins and Lua-based configuration.

## 🔹 2. Installation  
```bash
sudo apt install neovim
```


## 🔹 3. Help and Learning  
- `man nvim` — manual page  
- `nvim -u NONE` — start without config  
- [Neovim Docs](https://neovim.io/doc/)  
- [Neovim GitHub](https://github.com/neovim/neovim)  
- [Neovim Lua Guide](https://github.com/nanotee/nvim-lua-guide)  
- [Awesome Neovim](https://github.com/rockerBOO/awesome-neovim) — curated plugins and tools


## 🔹 4. Modes  

| Mode         | Description             | How to enter | How to leave |
|--------------|-------------------------|--------------|--------------|
| Normal       | For commands/navigation | (default)    | —            |
| Insert       | For editing text        | `i`, `a`     | `Esc`        |
| Visual       | For selection           | `v`, `V`     | `Esc`        |
| Command-line | For `:w`, `:q`, search  | `:`          | `Enter`/`Esc`|

## 🔹 5. Navigation  
```
h ←   j ↓   k ↑   l →
```
Also usable: arrow keys → ← ↑ ↓

Other movement:
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
:enew     # new empty file
```

## 🔹 7. Editing and Selection  
```vim
i         # insert mode
v / V     # visual mode (char / line)
y         # yank (copy)
p         # paste
d         # delete (dd = delete line)
u         # undo
Ctrl+r    # redo
```

## 🔹 8. Search and Replace  
```vim
/word         # search forward
n             # next match
N             # previous match

:%s/old/new/g     # replace all
:s/old/new/       # replace in current line
```
**Regular Expressions supported** — [What is Regex?](https://en.wikipedia.org/wiki/Regular_expression)

## 🔹 9. Lua Configuration  
Neovim supports config in `~/.config/nvim/init.lua` (or `init.vim`).  
Lua is fast and preferred in Neovim for advanced users.

Docs: [Neovim Lua Guide](https://github.com/nanotee/nvim-lua-guide)

## 🔹 10. Exit  
Press `Esc` to return to normal mode, then use:
```vim
:q       # quit
:q!      # quit without saving
:w       # save
:wq      # save and quit
```
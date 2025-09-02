# Neovim-Qt

## 🔹 1. Definition  
**Neovim Qt** is a graphical user interface (GUI) frontend for Neovim. It provides a modern and user-friendly interface for using Neovim outside of the terminal.

Official repo: [https://github.com/equalsraf/neovim-qt](https://github.com/equalsraf/neovim-qt)

## 🔹 2. Installation  
```bash
sudo apt install neovim-qt
```

## 🔹 3. Help and Resources  
- `man neovim-qt` — manual page  
- [GitHub - Neovim Qt](https://github.com/equalsraf/neovim-qt)  
- [Neovim Docs](https://neovim.io/doc/)  
- [Awesome Neovim](https://github.com/rockerBOO/awesome-neovim)

## 🔹 4. Launching Neovim Qt  
From terminal:
```bash
neovim-qt
```

Or find it via the application launcher (usually listed as “Neovim Qt” or “nvim-qt”).

You can also open a specific file:
```bash
neovim-qt myfile.txt
```

## 🔹 5. Features  
- Full GUI window with fonts, menus, tabs  
- Mouse support  
- Configurable via `~/.config/nvim/init.lua` or `init.vim`  
- Integrates with Neovim plugins and LSP

## 🔹 6. Differences from Terminal Neovim  

| Feature              | Neovim (CLI)     | Neovim Qt (GUI)       |
|----------------------|------------------|------------------------|
| Interface            | Terminal-based   | Graphical Qt-based     |
| Mouse support        | Limited          | Native Qt support      |
| Font configuration   | Terminal         | GUI preferences        |
| Clipboard            | Terminal dependent | System clipboard     |
| Appearance/themes    | Colorschemes     | Font rendering, themes |

## 🔹 7. Configuration  
Uses the same configuration files as Neovim:
- `~/.config/nvim/init.lua`
- `~/.config/nvim/init.vim`

You can also create GUI-specific settings using `g:GuiFont`, `g:GuiLinespace`, etc.

Example in `init.vim`:
```vim
if exists('g:neovide')
  let g:GuiFont = "FiraCode Nerd Font:h14"
endif
```

## 🔹 8. Exit  
To exit, use:
- GUI: File → Quit  
- Command: `:q`, `:wq`, etc.
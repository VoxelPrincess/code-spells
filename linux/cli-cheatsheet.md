# Linux CLI Cheatsheet

A collection of useful Linux command-line examples.

```bash
# File and directory operations
pwd
ls -l
ls -a
cd /path/to/dir
mkdir new_folder
cp source target
mv old_name new_name
rm file.txt

# Permissions
chmod 755 file.sh
chown user:group file.txt

# Process and disk info
htop
df -h
du -sh *

# Package management
sudo apt update
sudo apt upgrade
sudo apt install package-name
sudo apt remove package-name
sudo apt autoremove

# Navigation and search
history
history | grep keyword
grep "text" filename
find . -name "*.txt"

# Editors
vim file.txt
nano file.txt
emacs file.txt

# JSON and text tools
jq '.' file.json
sed 's/old/new/g' file.txt

# Network
nmcli connection show

# Python
python3
print("Hello")
Ctrl+D  # exit
```
# 📝 Sed

## 🔹 1. Definition  
**Sed** is a stream editor used to perform basic text transformations on an input stream (a file or input from a pipeline).

## 🔹 2. Installation  
```bash
sudo apt install sed
```

## 🔹 3. Help and Learning  
- `man sed` — manual page  
- `sed --help` — command line help  
- [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)  
- [Sed One-Liners](https://github.com/learnbyexample/Command-line-text-processing#sed-one-liners)  

## 🔹 4. Basic Usage  
```bash
sed 's/old/new/' file.txt       # replace first occurrence in each line
sed 's/old/new/g' file.txt      # replace all occurrences in each line
```

Use with `-i` for in-place edit:
```bash
sed -i 's/old/new/g' file.txt
```

## 🔹 5. Use in Pipelines  
```bash
echo "hello world" | sed 's/world/universe/'
```

## 🔹 6. Exit  
Sed exits automatically after processing the stream.
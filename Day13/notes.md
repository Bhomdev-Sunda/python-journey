# 📘 Day 13 Notes – Python File Handling

## What is File Handling?
File handling is the process of creating, opening, reading, writing, appending and managing files.

## Why File Handling is Used
- Permanent storage
- Save records
- Read existing data
- Generate reports
- Log information

## File Modes
| Mode | Purpose |
|---|---|
| r | Read |
| w | Write (overwrites) |
| a | Append |
| r+ | Read & Write |
| w+ | Write & Read (overwrites) |
| a+ | Append & Read |

## open()
```python
file = open("Day13/data.txt","r")
```

## close()
```python
file.close()
```

## with open()
Automatically closes the file.

## read()
Reads the whole file or specified characters.

## readline()
Reads one line.

## readlines()
Returns all lines as a list.

## write()
Writes text to a file.

## writelines()
Writes multiple strings.

## seek()
Moves the file pointer.

## tell()
Returns current pointer position.

## File Pointer
Tracks the current reading/writing location in a file.

## Common Mistakes
- Wrong mode
- Wrong path
- Forgetting close()
- Using w instead of a

## Interview Questions

**What is file handling?**
Managing files using Python.

**Why do we use files?**
To store data permanently.

**Difference between "w" and "a"?**
w overwrites, a appends.

**Difference between "r" and "r+"?**
r = read only, r+ = read & write.

**What does readline() do?**
Reads one line.

**Difference between read() and readlines()?**
read() returns one string, readlines() returns a list.

**Why is with open() preferred?**
It automatically closes the file.

**What does seek() do?**
Moves the file pointer.

**What does tell() do?**
Returns the pointer position.

**What happens if you open a file in "w" mode?**
Existing contents are erased before writing.

## Key Takeaways
- Use the correct mode.
- Prefer with open().
- Understand file pointer.
- Use seek() and tell().

## Revision Summary
- File handling
- Modes
- open/close
- with
- read/readline/readlines
- write/writelines
- seek/tell

# ==========================================================
#            Python File Methods - Day 13
# ==========================================================

print("=" * 70)
print("              PYTHON FILE METHODS")
print("=" * 70)

# ==========================================================
# WHAT ARE FILE METHODS?
# ==========================================================

# File methods are built-in functions that help us
# read, write, move, and manage file data.

print("\nFile methods make working with files easier.")

# ==========================================================
# 1. read()
# ==========================================================

print("\n" + "=" * 70)
print("1. read()")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.read())

# ==========================================================
# 2. read(size)
# ==========================================================

print("\n" + "=" * 70)
print("2. read(size)")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.read(25))

# ==========================================================
# 3. readline()
# ==========================================================

print("\n" + "=" * 70)
print("3. readline()")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.readline(), end="")
    print(file.readline())

# ==========================================================
# 4. readlines()
# ==========================================================

print("\n" + "=" * 70)
print("4. readlines()")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    lines = file.readlines()

    print(lines)

# ==========================================================
# 5. write()
# ==========================================================

print("\n" + "=" * 70)
print("5. write()")
print("=" * 70)

with open("Day13/data.txt", "w") as file:

    file.write("Python File Handling\n")
    file.write("Learning File Methods\n")
    file.write("write() Method Example\n")

print("Data Written Successfully!")

# ==========================================================
# 6. writelines()
# ==========================================================

print("\n" + "=" * 70)
print("6. writelines()")
print("=" * 70)

fruits = [

    "Apple\n",
    "Banana\n",
    "Mango\n",
    "Orange\n"

]

with open("Day13/data.txt", "w") as file:

    file.writelines(fruits)

print("Multiple Lines Written!")

# ==========================================================
# VERIFY FILE
# ==========================================================

print("\n" + "=" * 70)
print("VERIFY FILE")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.read())

# ==========================================================
# 7. seek()
# ==========================================================

print("\n" + "=" * 70)
print("7. seek()")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.read(6))

    file.seek(0)

    print("\nAfter seek(0):")

    print(file.read(6))

# ==========================================================
# 8. tell()
# ==========================================================

print("\n" + "=" * 70)
print("8. tell()")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print("Initial Position :", file.tell())

    file.read(10)

    print("After Reading :", file.tell())

# ==========================================================
# 9. flush()
# ==========================================================

print("\n" + "=" * 70)
print("9. flush()")
print("=" * 70)

file = open("Day13/data.txt", "a")

file.write("Flush Example\n")

file.flush()

print("Data Written to Disk.")

file.close()

# ==========================================================
# 10. readable() & writable()
# ==========================================================

print("\n" + "=" * 70)
print("10. readable() & writable()")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print("Readable :", file.readable())

    print("Writable :", file.writable())

with open("Day13/data.txt", "a") as file:

    print("Readable :", file.readable())

    print("Writable :", file.writable())

# ==========================================================
# 11. name, mode, closed
# ==========================================================

print("\n" + "=" * 70)
print("11. FILE ATTRIBUTES")
print("=" * 70)

file = open("Day13/data.txt", "r")

print("Name   :", file.name)

print("Mode   :", file.mode)

print("Closed :", file.closed)

file.close()

print("Closed After close() :", file.closed)

# ==========================================================
# LOOP THROUGH FILE
# ==========================================================

print("\n" + "=" * 70)
print("12. LOOP THROUGH FILE")
print("=" * 70)

with open("Day13/students.txt", "r") as file:

    for line in file:

        print(line.strip())

# ==========================================================
# COMMON FILE METHODS
# ==========================================================

print("\n" + "=" * 70)
print("COMMON FILE METHODS")
print("=" * 70)

methods = [

    "read()",

    "readline()",

    "readlines()",

    "write()",

    "writelines()",

    "seek()",

    "tell()",

    "flush()",

    "close()",

    "readable()",

    "writable()"

]

for method in methods:

    print("✔", method)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to close the file.")
print("❌ Using write mode when append is needed.")
print("❌ Forgetting seek() before reading again.")
print("❌ Calling methods on a closed file.")
print("❌ Using the wrong file path.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use with statement whenever possible.")
print("✔ Close files properly.")
print("✔ Use seek() carefully.")
print("✔ Check readable() and writable().")
print("✔ Handle errors with try-except.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ read() reads file content.")
print("✔ readline() reads one line.")
print("✔ readlines() returns all lines as a list.")
print("✔ write() writes text.")
print("✔ writelines() writes multiple lines.")
print("✔ seek() moves the file pointer.")
print("✔ tell() returns the current pointer position.")
print("✔ flush() writes buffered data immediately.")
print("✔ readable() checks read permission.")
print("✔ writable() checks write permission.")

print("=" * 70)
print("End of 06_file_methods.py")
print("=" * 70)
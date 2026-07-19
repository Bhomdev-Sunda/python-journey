# ==========================================================
#          Python File Reading - Day 13
# ==========================================================

print("=" * 70)
print("              PYTHON FILE READING")
print("=" * 70)

# ==========================================================
# WHAT IS FILE READING?
# ==========================================================

# File reading means retrieving data stored inside
# a text file so that we can use it in our program.

print("\nReading a file allows us to access stored information.")

# ==========================================================
# READ ENTIRE FILE
# ==========================================================

print("\n" + "=" * 70)
print("1. READ ENTIRE FILE")
print("=" * 70)

file = open("Day13/data.txt", "r")

content = file.read()

print(content)

file.close()

# ==========================================================
# READ FIRST 20 CHARACTERS
# ==========================================================

print("\n" + "=" * 70)
print("2. READ SPECIFIC NUMBER OF CHARACTERS")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read(20))

file.close()

# ==========================================================
# READ ONE LINE
# ==========================================================

print("\n" + "=" * 70)
print("3. READ FIRST LINE")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.readline())

file.close()

# ==========================================================
# READ MULTIPLE LINES
# ==========================================================

print("\n" + "=" * 70)
print("4. READ MULTIPLE LINES")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.readline())
print(file.readline())

file.close()

# ==========================================================
# READ ALL LINES AS A LIST
# ==========================================================

print("\n" + "=" * 70)
print("5. READLINES()")
print("=" * 70)

file = open("Day13/data.txt", "r")

lines = file.readlines()

print(lines)

file.close()

# ==========================================================
# LOOP THROUGH FILE
# ==========================================================

print("\n" + "=" * 70)
print("6. LOOP THROUGH FILE")
print("=" * 70)

file = open("Day13/data.txt", "r")

for line in file:

    print(line.strip())

file.close()

# ==========================================================
# READ STUDENTS FILE
# ==========================================================

print("\n" + "=" * 70)
print("7. READ STUDENTS FILE")
print("=" * 70)

file = open("Day13/students.txt", "r")

print(file.read())

file.close()

# ==========================================================
# COUNT TOTAL LINES
# ==========================================================

print("\n" + "=" * 70)
print("8. COUNT TOTAL LINES")
print("=" * 70)

file = open("Day13/students.txt", "r")

count = 0

for line in file:

    count += 1

print("Total Lines :", count)

file.close()

# ==========================================================
# COUNT TOTAL CHARACTERS
# ==========================================================

print("\n" + "=" * 70)
print("9. COUNT TOTAL CHARACTERS")
print("=" * 70)

file = open("Day13/data.txt", "r")

content = file.read()

print("Total Characters :", len(content))

file.close()

# ==========================================================
# COUNT TOTAL WORDS
# ==========================================================

print("\n" + "=" * 70)
print("10. COUNT TOTAL WORDS")
print("=" * 70)

file = open("Day13/data.txt", "r")

content = file.read()

words = content.split()

print("Total Words :", len(words))

file.close()

# ==========================================================
# FILE POINTER
# ==========================================================

print("\n" + "=" * 70)
print("11. FILE POINTER")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read(15))

print("\nReading Again...")

print(file.read())

file.close()

# ==========================================================
# REOPEN FILE
# ==========================================================

print("\n" + "=" * 70)
print("12. REOPEN FILE")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read())

file.close()

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to close the file.")
print("❌ Reading a file that doesn't exist.")
print("❌ Reading after the pointer reaches the end.")
print("❌ Using the wrong file mode.")
print("❌ Forgetting to reopen the file when needed.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Reading student records",

    "Reading employee data",

    "Loading configuration files",

    "Reading log files",

    "Reading reports",

    "Loading game data",

    "Reading CSV files",

    "Reading text documents"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ read() reads the entire file.")
print("✔ read(n) reads a specific number of characters.")
print("✔ readline() reads one line.")
print("✔ readlines() returns all lines as a list.")
print("✔ Files can be read using loops.")
print("✔ File pointer moves after every read.")
print("✔ Close the file after reading.")

print("=" * 70)
print("End of 02_read_file.py")
print("=" * 70)
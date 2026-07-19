# ==========================================================
#          Python with Statement - Day 13
# ==========================================================

print("=" * 70)
print("            PYTHON WITH STATEMENT")
print("=" * 70)

# ==========================================================
# WHAT IS THE WITH STATEMENT?
# ==========================================================

# The 'with' statement is the recommended way to work
# with files in Python.
#
# It automatically closes the file after the work
# is completed, even if an error occurs.

print("\nThe 'with' statement automatically closes the file.")

# ==========================================================
# WHY USE WITH?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE THE WITH STATEMENT?")
print("=" * 70)

print("1. Automatically closes the file.")
print("2. Cleaner code.")
print("3. Safer than using close().")
print("4. Prevents resource leaks.")
print("5. Recommended by Python.")

# ==========================================================
# READ FILE USING WITH
# ==========================================================

print("\n" + "=" * 70)
print("1. READ FILE USING WITH")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    content = file.read()

    print(content)

print("\nFile Closed Automatically!")

# ==========================================================
# READ FILE LINE BY LINE
# ==========================================================

print("\n" + "=" * 70)
print("2. READ LINE BY LINE")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    for line in file:

        print(line.strip())

# ==========================================================
# READ STUDENT RECORDS
# ==========================================================

print("\n" + "=" * 70)
print("3. READ STUDENT RECORDS")
print("=" * 70)

with open("Day13/students.txt", "r") as file:

    print(file.read())

# ==========================================================
# WRITE USING WITH
# ==========================================================

print("\n" + "=" * 70)
print("4. WRITE USING WITH")
print("=" * 70)

with open("Day13/data.txt", "w") as file:

    file.write("Learning Python File Handling\n")
    file.write("Using the with statement\n")
    file.write("Files close automatically.\n")

print("Data Written Successfully!")

# ==========================================================
# VERIFY WRITTEN DATA
# ==========================================================

print("\n" + "=" * 70)
print("5. VERIFY WRITTEN DATA")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.read())

# ==========================================================
# APPEND USING WITH
# ==========================================================

print("\n" + "=" * 70)
print("6. APPEND USING WITH")
print("=" * 70)

with open("Day13/data.txt", "a") as file:

    file.write("\nThis line was added using the with statement.")

print("Data Appended Successfully!")

# ==========================================================
# VERIFY APPENDED DATA
# ==========================================================

print("\n" + "=" * 70)
print("7. VERIFY APPENDED DATA")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.read())

# ==========================================================
# FILE INFORMATION
# ==========================================================

print("\n" + "=" * 70)
print("8. FILE INFORMATION")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print("File Name :", file.name)
    print("File Mode :", file.mode)
    print("Readable? :", file.readable())
    print("Writable? :", file.writable())

# ==========================================================
# CHECK FILE STATUS
# ==========================================================

print("\n" + "=" * 70)
print("9. CHECK FILE STATUS")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print("Inside with Block :", file.closed)

print("Outside with Block :", file.closed)

# ==========================================================
# READ FIRST TWO LINES
# ==========================================================

print("\n" + "=" * 70)
print("10. READ FIRST TWO LINES")
print("=" * 70)

with open("Day13/data.txt", "r") as file:

    print(file.readline(), end="")
    print(file.readline())

# ==========================================================
# COUNT TOTAL LINES
# ==========================================================

print("\n" + "=" * 70)
print("11. COUNT TOTAL LINES")
print("=" * 70)

count = 0

with open("Day13/data.txt", "r") as file:

    for line in file:

        count += 1

print("Total Lines :", count)

# ==========================================================
# DIFFERENCE BETWEEN open() AND with
# ==========================================================

print("\n" + "=" * 70)
print("12. open() vs with")
print("=" * 70)

print("Using open()")
print("✔ Need to call close() manually.")
print("✔ Easier to forget closing the file.")

print()

print("Using with")
print("✔ Automatically closes the file.")
print("✔ Cleaner and safer.")
print("✔ Recommended for all file operations.")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to indent inside the with block.")
print("❌ Using the file after the with block ends.")
print("❌ Wrong file path.")
print("❌ Using the wrong file mode.")
print("❌ Forgetting '\\n' while writing multiple lines.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Reading Configuration Files",

    "Saving Student Records",

    "Writing Log Files",

    "Generating Reports",

    "Exporting Data",

    "Reading CSV Files",

    "Saving User Data",

    "Managing Text Documents"

]

for app in applications:

    print("✔", app)

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Always prefer the with statement.")
print("✔ Use meaningful file names.")
print("✔ Use the correct file mode.")
print("✔ Keep file operations inside the with block.")
print("✔ Handle missing files using try-except.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ 'with' automatically closes the file.")
print("✔ Cleaner and more readable code.")
print("✔ No need to call close().")
print("✔ Works with read(), write(), and append.")
print("✔ Recommended for professional Python projects.")
print("✔ Prevents resource leaks.")

print("=" * 70)
print("End of 05_with_statement.py")
print("=" * 70)
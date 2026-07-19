# ==========================================================
#           Python File Writing - Day 13
# ==========================================================

print("=" * 70)
print("              PYTHON FILE WRITING")
print("=" * 70)

# ==========================================================
# WHAT IS FILE WRITING?
# ==========================================================

# File writing means storing data into a file.
# If the file already contains data, write mode ('w')
# removes the old content and writes the new content.

print("\nWriting allows us to save information into a file.")

# ==========================================================
# WRITE SINGLE LINE
# ==========================================================

print("\n" + "=" * 70)
print("1. WRITE SINGLE LINE")
print("=" * 70)

file = open("Day13/data.txt", "w")

file.write("Welcome to Python File Handling.\n")

file.close()

print("Data Written Successfully!")

# ==========================================================
# WRITE MULTIPLE LINES
# ==========================================================

print("\n" + "=" * 70)
print("2. WRITE MULTIPLE LINES")
print("=" * 70)

file = open("Day13/data.txt", "w")

file.write("Python File Handling\n")
file.write("Learning write() function\n")
file.write("This is the third line.\n")
file.write("Have a great day!\n")

file.close()

print("Multiple Lines Written Successfully!")

# ==========================================================
# READ FILE AFTER WRITING
# ==========================================================

print("\n" + "=" * 70)
print("3. READ FILE AFTER WRITING")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read())

file.close()

# ==========================================================
# WRITE STUDENT RECORDS
# ==========================================================

print("\n" + "=" * 70)
print("4. WRITE STUDENT RECORDS")
print("=" * 70)

file = open("Day13/students.txt", "w")

file.write("101,Bhomdev,Python,95\n")
file.write("102,Rahul,Java,88\n")
file.write("103,Priya,C++,91\n")
file.write("104,Aman,Data Science,90\n")

file.close()

print("Student Records Saved!")

# ==========================================================
# READ STUDENT RECORDS
# ==========================================================

print("\n" + "=" * 70)
print("5. READ STUDENT RECORDS")
print("=" * 70)

file = open("Day13/students.txt", "r")

print(file.read())

file.close()

# ==========================================================
# USING writelines()
# ==========================================================

print("\n" + "=" * 70)
print("6. WRITELINES()")
print("=" * 70)

lines = [

    "Apple\n",
    "Banana\n",
    "Mango\n",
    "Orange\n",
    "Grapes\n"

]

file = open("Day13/data.txt", "w")

file.writelines(lines)

file.close()

print("List Written Successfully!")

# ==========================================================
# VERIFY WRITELINES()
# ==========================================================

print("\n" + "=" * 70)
print("7. VERIFY FILE CONTENT")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read())

file.close()

# ==========================================================
# CHECK FILE PROPERTIES
# ==========================================================

print("\n" + "=" * 70)
print("8. FILE PROPERTIES")
print("=" * 70)

file = open("Day13/data.txt", "w")

print("File Name :", file.name)
print("Mode      :", file.mode)
print("Writable? :", file.writable())
print("Readable? :", file.readable())

file.close()

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Using 'w' when you want to keep old data.")
print("❌ Forgetting to close the file.")
print("❌ Missing '\\n' while writing multiple lines.")
print("❌ Using wrong file path.")
print("❌ Trying to read while file is opened only in write mode.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Saving Student Records",
    "Creating Reports",
    "Generating Bills",
    "Saving User Information",
    "Exporting Data",
    "Writing Log Files",
    "Creating Configuration Files",
    "Saving Game Scores"

]

for app in applications:

    print("✔", app)

# ==========================================================
# IMPORTANT NOTE
# ==========================================================

print("\n" + "=" * 70)
print("IMPORTANT NOTE")
print("=" * 70)

print("Write mode (w) always removes the old file content")
print("before writing new data.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ write() writes text into a file.")
print("✔ writelines() writes multiple lines.")
print("✔ 'w' mode overwrites existing data.")
print("✔ Always close the file after writing.")
print("✔ Use '\\n' for new lines.")
print("✔ Verify the file after writing.")

print("=" * 70)
print("End of 03_write_file.py")
print("=" * 70)
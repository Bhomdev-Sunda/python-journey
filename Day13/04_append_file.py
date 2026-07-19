# ==========================================================
#          Python File Append Mode - Day 13
# ==========================================================

print("=" * 70)
print("             PYTHON FILE APPEND MODE")
print("=" * 70)

# ==========================================================
# WHAT IS APPEND MODE?
# ==========================================================

# Append mode ("a") adds new data to the END of a file.
# It does NOT remove the existing content.

print("\nAppend mode adds new data without deleting old data.")

# ==========================================================
# APPEND A SINGLE LINE
# ==========================================================

print("\n" + "=" * 70)
print("1. APPEND A SINGLE LINE")
print("=" * 70)

file = open("Day13/data.txt", "a")

file.write("\nThis line was added using append mode.")

file.close()

print("Line Appended Successfully!")

# ==========================================================
# READ FILE AFTER APPENDING
# ==========================================================

print("\n" + "=" * 70)
print("2. READ UPDATED FILE")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read())

file.close()

# ==========================================================
# APPEND MULTIPLE LINES
# ==========================================================

print("\n" + "=" * 70)
print("3. APPEND MULTIPLE LINES")
print("=" * 70)

file = open("Day13/data.txt", "a")

file.write("\nPython is easy to learn.")
file.write("\nFile handling is very useful.")
file.write("\nPractice makes perfect.")

file.close()

print("Multiple Lines Appended Successfully!")

# ==========================================================
# VERIFY UPDATED FILE
# ==========================================================

print("\n" + "=" * 70)
print("4. VERIFY FILE CONTENT")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read())

file.close()

# ==========================================================
# APPEND STUDENT RECORD
# ==========================================================

print("\n" + "=" * 70)
print("5. APPEND STUDENT RECORD")
print("=" * 70)

file = open("Day13/students.txt", "a")

file.write("\n105,Rohit,Python,89")

file.close()

print("Student Record Added Successfully!")

# ==========================================================
# READ STUDENT FILE
# ==========================================================

print("\n" + "=" * 70)
print("6. UPDATED STUDENT RECORDS")
print("=" * 70)

file = open("Day13/students.txt", "r")

print(file.read())

file.close()

# ==========================================================
# APPEND USING A LOOP
# ==========================================================

print("\n" + "=" * 70)
print("7. APPEND NUMBERS")
print("=" * 70)

file = open("Day13/data.txt", "a")

file.write("\n")

for number in range(1, 6):

    file.write(f"Number {number}\n")

file.close()

print("Numbers Appended Successfully!")

# ==========================================================
# VERIFY AGAIN
# ==========================================================

print("\n" + "=" * 70)
print("8. FINAL FILE CONTENT")
print("=" * 70)

file = open("Day13/data.txt", "r")

print(file.read())

file.close()

# ==========================================================
# FILE INFORMATION
# ==========================================================

print("\n" + "=" * 70)
print("9. FILE INFORMATION")
print("=" * 70)

file = open("Day13/data.txt", "a")

print("File Name :", file.name)
print("Mode      :", file.mode)
print("Readable? :", file.readable())
print("Writable? :", file.writable())

file.close()

# ==========================================================
# DIFFERENCE BETWEEN WRITE AND APPEND
# ==========================================================

print("\n" + "=" * 70)
print("10. WRITE vs APPEND")
print("=" * 70)

print("Write Mode (w)")
print("✔ Deletes old content")
print("✔ Writes new content")

print()

print("Append Mode (a)")
print("✔ Keeps old content")
print("✔ Adds new content at the end")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting '\\n' before new data.")
print("❌ Expecting append mode to overwrite data.")
print("❌ Using the wrong file path.")
print("❌ Forgetting to close the file.")
print("❌ Opening the file in 'w' instead of 'a'.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Adding Student Records",
    "Updating Employee Logs",
    "Saving Chat Messages",
    "Recording Game Scores",
    "Maintaining Attendance",
    "Writing Server Logs",
    "Saving Transactions",
    "Daily Reports"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ 'a' mode appends data to the end of a file.")
print("✔ Existing data remains unchanged.")
print("✔ write() can be used in append mode.")
print("✔ '\\n' helps write data on a new line.")
print("✔ Append mode is ideal for logs and records.")
print("✔ Always close the file after appending.")

print("=" * 70)
print("End of 04_append_file.py")
print("=" * 70)
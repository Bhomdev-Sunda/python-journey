# ==========================================================
#          Python File Open & Close - Day 13
# ==========================================================

print("=" * 70)
print("            PYTHON FILE OPEN & CLOSE")
print("=" * 70)

# ==========================================================
# WHAT IS FILE HANDLING?
# ==========================================================

# File handling is used to create, read, write,
# update, and manage files stored on your computer.

print("\nFile handling allows Python programs to work with files.")

# ==========================================================
# WHY FILE HANDLING?
# ==========================================================

print("\n" + "=" * 70)
print("WHY FILE HANDLING?")
print("=" * 70)

print("1. Store data permanently")
print("2. Read saved information")
print("3. Write new information")
print("4. Update existing files")
print("5. Share data between programs")

# ==========================================================
# OPENING A FILE
# ==========================================================

print("\n" + "=" * 70)
print("OPENING A FILE")
print("=" * 70)

# Open the file in read mode
file = open("Day13/data.txt", "r")

print("File Opened Successfully!")

# Close the file
file.close()

print("File Closed Successfully!")

# ==========================================================
# FILE MODES
# ==========================================================

print("\n" + "=" * 70)
print("FILE MODES")
print("=" * 70)

print("r  -> Read")
print("w  -> Write")
print("a  -> Append")
print("x  -> Create")
print("t  -> Text Mode (Default)")
print("b  -> Binary Mode")
print("r+ -> Read and Write")
print("w+ -> Write and Read")
print("a+ -> Append and Read")

# ==========================================================
# CHECKING FILE STATUS
# ==========================================================

print("\n" + "=" * 70)
print("CHECK FILE STATUS")
print("=" * 70)

file = open("Day13/data.txt", "r")

print("Is File Closed? :", file.closed)

file.close()

print("After Closing :", file.closed)

# ==========================================================
# FILE INFORMATION
# ==========================================================

print("\n" + "=" * 70)
print("FILE INFORMATION")
print("=" * 70)

file = open("Day13/data.txt", "r")

print("File Name :", file.name)
print("File Mode :", file.mode)
print("Readable? :", file.readable())
print("Writable? :", file.writable())

file.close()

# ==========================================================
# TRYING TO READ AFTER CLOSE
# ==========================================================

print("\n" + "=" * 70)
print("READ AFTER CLOSE")
print("=" * 70)

file = open("Day13/data.txt", "r")

file.close()

try:

    print(file.read())

except ValueError as error:

    print("Error :", error)

# ==========================================================
# OPEN DIFFERENT FILES
# ==========================================================

print("\n" + "=" * 70)
print("OPEN ANOTHER FILE")
print("=" * 70)

student_file = open("Day13/students.txt", "r")

print("Opened :", student_file.name)

student_file.close()

print("Closed :", student_file.closed)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to close the file.")
print("❌ Opening a file that doesn't exist.")
print("❌ Using the wrong file mode.")
print("❌ Reading from a closed file.")
print("❌ Misspelling the file name.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Student Management System",

    "Employee Records",

    "Banking Applications",

    "Hospital Management",

    "Billing System",

    "Inventory Management",

    "Log Files",

    "Saving Game Progress"

]

for app in applications:

    print("✔", app)

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Always close files after use.")
print("✔ Use the correct file mode.")
print("✔ Handle exceptions for missing files.")
print("✔ Use 'with' statement whenever possible.")
print("✔ Keep file names meaningful.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ open() is used to open files.")
print("✔ close() releases the file resource.")
print("✔ File modes decide how a file is accessed.")
print("✔ closed returns the file status.")
print("✔ name returns the file name.")
print("✔ mode returns the file mode.")
print("✔ readable() checks if the file can be read.")
print("✔ writable() checks if the file can be written.")

print("=" * 70)
print("End of 01_open_close.py")
print("=" * 70)
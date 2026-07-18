# ==========================================================
#               practice.py - Day 11
#        Student Result Management System
# ==========================================================

print("=" * 65)
print("      STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 65)

# ----------------------------------------------------------
# Global Variable
# ----------------------------------------------------------

school_name = "Bhomdev Coding Academy"

# ----------------------------------------------------------
# Function 1
# ----------------------------------------------------------

def welcome():
    print("\nWelcome to", school_name)
    print("-" * 65)

# ----------------------------------------------------------
# Function 2
# ----------------------------------------------------------

def student_details(name, age, course="Python"):
    print("\nStudent Details")
    print("-" * 30)
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

# ----------------------------------------------------------
# Function 3
# ----------------------------------------------------------

def total_marks(*marks):
    return sum(marks)

# ----------------------------------------------------------
# Function 4
# ----------------------------------------------------------

def average(total, subjects):
    return total / subjects

# ----------------------------------------------------------
# Function 5
# ----------------------------------------------------------

def grade(avg):

    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    elif avg >= 40:
        return "D"

    else:
        return "Fail"

# ----------------------------------------------------------
# Function 6
# ----------------------------------------------------------

def student_information(**info):

    print("\nExtra Information")
    print("-" * 30)

    for key, value in info.items():
        print(f"{key.title():<12}: {value}")

# ----------------------------------------------------------
# Function 7
# ----------------------------------------------------------

counter = 0

def increase_counter():
    global counter
    counter += 1

# ----------------------------------------------------------
# Lambda Functions
# ----------------------------------------------------------

percentage = lambda total: total / 3

is_pass = lambda avg: "Pass" if avg >= 40 else "Fail"

# ----------------------------------------------------------
# Main Program
# ----------------------------------------------------------

welcome()

name = input("\nEnter Student Name : ")
age = int(input("Enter Age          : "))

print("\nEnter Marks")

m1 = int(input("Python      : "))
m2 = int(input("SQL         : "))
m3 = int(input("Statistics  : "))

student_details(name, age)

total = total_marks(m1, m2, m3)

avg = average(total, 3)

per = percentage(total)

student_grade = grade(avg)

status = is_pass(avg)

increase_counter()

print("\n" + "=" * 65)
print("RESULT CARD")
print("=" * 65)

print("School      :", school_name)
print("Student     :", name)
print("Age         :", age)

print("\nMarks")
print("-" * 30)
print("Python      :", m1)
print("SQL         :", m2)
print("Statistics  :", m3)

print("-" * 30)

print("Total       :", total)
print("Average     :", round(avg, 2))
print("Percentage  :", round(per, 2), "%")
print("Grade       :", student_grade)
print("Status      :", status)

student_information(
    City="Patiala",
    Course="Python",
    Batch="Day 11"
)

print("\nStudents Processed :", counter)

print("\n" + "=" * 65)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 65)
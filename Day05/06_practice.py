#           SMART STUDENT MANAGEMENT SYSTEM
print("=" * 60)
print("           SMART STUDENT MANAGEMENT SYSTEM")
print("=" * 60)

# Student Information
student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number : ")

print("\nEnter Marks of 5 Subjects (Out of 100)")

subject1 = float(input("Subject 1 : "))
subject2 = float(input("Subject 2 : "))
subject3 = float(input("Subject 3 : "))
subject4 = float(input("Subject 4 : "))
subject5 = float(input("Subject 5 : "))

# Calculations
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

percentage = total_marks / 5

# Pass / Fail
if (
    subject1 >= 33 and
    subject2 >= 33 and
    subject3 >= 33 and
    subject4 >= 33 and
    subject5 >= 33
):
    result = "PASS"
else:
    result = "FAIL"

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 33:
    grade = "E"
else:
    grade = "F"

# Scholarship Eligibility
if percentage >= 90 and result == "PASS":
    scholarship = "Eligible"
else:
    scholarship = "Not Eligible"

# Student Report
print("\n")
print("=" * 60)
print("                 STUDENT REPORT")
print("=" * 60)

print(f"Student Name        : {student_name.title()}")
print(f"Roll Number         : {roll_number}")

print("\n----------------- MARKS -----------------")

print(f"Subject 1           : {subject1}")
print(f"Subject 2           : {subject2}")
print(f"Subject 3           : {subject3}")
print(f"Subject 4           : {subject4}")
print(f"Subject 5           : {subject5}")

print("-----------------------------------------")

print(f"Total Marks         : {total_marks}/500")
print(f"Percentage          : {percentage:.2f}%")
print(f"Grade               : {grade}")
print(f"Result              : {result}")
print(f"Scholarship         : {scholarship}")

print("=" * 60)

# Performance Message
if result == "PASS":

    if percentage >= 90:
        print("Outstanding Performance! Keep it up.")

    elif percentage >= 75:
        print("Excellent Work! You performed very well.")

    elif percentage >= 60:
        print("Good Job! Keep improving.")

    else:
        print("You Passed. Work harder for better results.")

else:
    print("Unfortunately, You Failed. Better Luck Next Time.")

print("=" * 60)
print("      THANK YOU FOR USING THE SYSTEM")
print("=" * 60)
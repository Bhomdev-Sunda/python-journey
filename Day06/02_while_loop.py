#                 WHILE LOOP IN PYTHON
print("=" * 60)
print("            EMPLOYEE ID VERIFICATION")
print("=" * 60)

# Employee Details
correct_employee_id = "EMP101"
employee_id = ""

# While Loop
while employee_id != correct_employee_id:
    employee_id = input("Enter Employee ID : ")

    if employee_id != correct_employee_id:
        print("❌ Invalid Employee ID. Please try again.\n")

# Verification Successful
print("\n✅ Employee ID Verified Successfully!")
print("Welcome to the Company Portal.")

# End
print("\n" + "=" * 60)
print("Thank You for Using Employee Verification System.")
print("=" * 60)
#                IF ELSE STATEMENT IN PYTHON

print("=" * 60)
print("              EMPLOYEE ACCESS SYSTEM")
print("=" * 60)

# Employee Details

employee_name = input("Enter Employee Name : ")
employee_age = int(input("Enter Employee Age : "))

# If Else Statement

if employee_age >= 18:
    print("\nAccess Granted!")
    print(f"Welcome, {employee_name}.")
    print("You are eligible to enter the company.")
else:
    print("\nAccess Denied!")
    print(f"Sorry, {employee_name}.")
    print("You must be at least 18 years old to enter the company.")

# End
print("\nThank You for Using Employee Access System.")
print("=" * 60)
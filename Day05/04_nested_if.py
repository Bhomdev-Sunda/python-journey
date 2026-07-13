#              NESTED IF STATEMENT IN PYTHON
print("=" * 60)
print("            EMPLOYEE LOGIN SYSTEM")
print("=" * 60)

# Employee Details
employee_name = input("Enter Employee Name : ")
employee_id = input("Enter Employee ID : ")
employee_age = int(input("Enter Employee Age : "))

# Nested If Statement
if employee_age >= 18:
    print("\nAge Verification Successful.")
    if employee_id == "EMP101":
        print("Employee ID Verified.")
        print(f"Welcome, {employee_name}!")
        print("Login Successful.")
    else:
        print("Invalid Employee ID.")
        print("Login Failed.")
else:
    print("\nAccess Denied!")
    print("Employee must be at least 18 years old.")

# End
print("\nThank You for Using Employee Login System.")
print("=" * 60)
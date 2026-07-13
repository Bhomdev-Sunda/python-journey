#                  IF STATEMENT IN PYTHON

print("=" * 60)
print("              EMPLOYEE ACCESS SYSTEM")
print("=" * 60)

# Employee Details
 
employee_name = input("Enter Employee Name : ")
employee_age = int(input("Enter Employee Age : "))

# If Statement
 
if employee_age >= 18:
    print("\nAccess Granted!")
    print(f"Welcome, {employee_name}.")

 # End
print("\nThank You for Using Employee Access System.")
print("=" * 60)
#             MATCH CASE STATEMENT IN PYTHON
print("=" * 60)
print("           EMPLOYEE DEPARTMENT PORTAL")
print("=" * 60)

# Employee Details
employee_name = input("Enter Employee Name : ")

print("\nAvailable Departments")
print("1. HR")
print("2. IT")
print("3. Finance")
print("4. Sales")
print("5. Marketing")

department = input("\nEnter Department Name : ").title()

# Match Case Statement

match department:

    case "Hr":
        print("\nDepartment : Human Resources")
        print(f"Welcome, {employee_name}.")
        print("You can manage employee records and recruitment.")

    case "It":
        print("\nDepartment : Information Technology")
        print(f"Welcome, {employee_name}.")
        print("You can manage software and technical support.")

    case "Finance":
        print("\nDepartment : Finance")
        print(f"Welcome, {employee_name}.")
        print("You can manage company accounts and payroll.")

    case "Sales":
        print("\nDepartment : Sales")
        print(f"Welcome, {employee_name}.")
        print("You can manage customer sales and revenue.")

    case "Marketing":
        print("\nDepartment : Marketing")
        print(f"Welcome, {employee_name}.")
        print("You can manage promotions and advertising.")

    case _:
        print("\nInvalid Department!")
        print("Please enter a valid department name.")

# End
print("\nThank You for Using Employee Department Portal.")
print("=" * 60)
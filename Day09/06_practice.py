#          EMPLOYEE MANAGEMENT SYSTEM
print("=" * 70)
print("          EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 70)

# NESTED DICTIONARY DATABASE

employees = {

    101: {
        "name": "Rahul",
        "department": "HR",
        "salary": 35000
    },

    102: {
        "name": "Aman",
        "department": "IT",
        "salary": 50000
    },

    103: {
        "name": "Bhomdev",
        "department": "Developer",
        "salary": 60000
    }

}

# DISPLAY ALL EMPLOYEES

print("\nALL EMPLOYEES")
print("-" * 70)

for emp_id, details in employees.items():

    print(f"\nEmployee ID : {emp_id}")

    for key, value in details.items():
        print(f"{key.title():<12}: {value}")

# SEARCH EMPLOYEE

print("\n" + "=" * 70)

search = int(input("Enter Employee ID to Search : "))

if search in employees:

    print("\nEmployee Found")

    print("-" * 40)

    for key, value in employees[search].items():
        print(f"{key.title():<12}: {value}")

else:

    print("Employee Not Found.")

# ADD NEW EMPLOYEE

print("\n" + "=" * 70)
print("ADD NEW EMPLOYEE")
print("=" * 70)

emp_id = int(input("Employee ID : "))
name = input("Name : ").title()
department = input("Department : ").title()
salary = float(input("Salary : "))

employees[emp_id] = {
    "name": name,
    "department": department,
    "salary": salary
}

print("\nEmployee Added Successfully.")

# UPDATE EMPLOYEE

print("\n" + "=" * 70)
print("UPDATE EMPLOYEE")
print("=" * 70)

update_id = int(input("Enter Employee ID : "))

if update_id in employees:

    new_salary = float(input("Enter New Salary : "))

    employees[update_id].update({
        "salary": new_salary
    })

    print("Salary Updated Successfully.")

else:

    print("Employee Not Found.")

# DELETE EMPLOYEE

print("\n" + "=" * 70)
print("DELETE EMPLOYEE")
print("=" * 70)

delete_id = int(input("Enter Employee ID : "))

if delete_id in employees:

    employees.pop(delete_id)

    print("Employee Deleted Successfully.")

else:

    print("Employee Not Found.")

# DISPLAY UPDATED DATABASE

print("\n" + "=" * 70)
print("UPDATED EMPLOYEE DATABASE")
print("=" * 70)

for emp_id, details in employees.items():

    print(f"\nEmployee ID : {emp_id}")

    for key, value in details.items():
        print(f"{key.title():<12}: {value}")

# DICTIONARY METHODS

print("\n" + "=" * 70)
print("DICTIONARY METHODS")
print("=" * 70)

print("Keys")
print(employees.keys())

print("\nValues")
print(employees.values())

print("\nItems")
print(employees.items())

employee_copy = employees.copy()

print("\nCopy Created Successfully.")

# DICTIONARY COMPREHENSION

print("\n" + "=" * 70)
print("DICTIONARY COMPREHENSION")
print("=" * 70)

salary_bonus = {
    emp_id: details["salary"] * 1.10
    for emp_id, details in employees.items()
}

print("Salary After 10% Bonus")

for emp_id, bonus in salary_bonus.items():
    print(f"Employee {emp_id} : ₹{bonus:.2f}")

# HIGH SALARY EMPLOYEES

print("\n" + "=" * 70)
print("HIGH SALARY EMPLOYEES")
print("=" * 70)

high_salary = {

    emp_id: details

    for emp_id, details in employees.items()

    if details["salary"] >= 50000

}

for emp_id, details in high_salary.items():

    print(f"\nEmployee ID : {emp_id}")

    for key, value in details.items():
        print(f"{key.title():<12}: {value}")

# SUMMARY

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("Total Employees :", len(employees))

print("\nEmployee IDs")

for emp_id in employees.keys():
    print(emp_id)

print("\nDepartments")

for details in employees.values():
    print(details["department"])

print("\nProject Completed Successfully!")

print("=" * 70)
print("End of dictionary_practice.py")
print("=" * 70)
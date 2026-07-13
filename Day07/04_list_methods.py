#               LIST METHODS IN PYTHON
print("=" * 60)
print("          EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 60)

# Employee List
employees = [
    "Bhomdev",
    "Rahul",
    "Priya",
    "Aman",
    "Neha"
]

print("\nOriginal Employee List")
print(employees)

# append()
print("\n" + "-" * 60)
print("append()")
print("-" * 60)

employees.append("Rohit")

print("After Adding One Employee")
print(employees)

# extend()
print("\n" + "-" * 60)
print("extend()")
print("-" * 60)

employees.extend(["Simran", "Karan"])

print("After Adding Multiple Employees")
print(employees)

# insert()
print("\n" + "-" * 60)
print("insert()")
print("-" * 60)

employees.insert(2, "Anjali")

print("After Inserting Employee")
print(employees)

# remove()
print("\n" + "-" * 60)
print("remove()")
print("-" * 60)

employees.remove("Rahul")

print("After Removing Rahul")
print(employees)

# pop()
print("\n" + "-" * 60)
print("pop()")
print("-" * 60)

removed_employee = employees.pop()

print(f"Removed Employee : {removed_employee}")
print(employees)

# index()
print("\n" + "-" * 60)
print("index()")
print("-" * 60)

position = employees.index("Priya")

print(f"Priya is at Index : {position}")

# count()
print("\n" + "-" * 60)
print("count()")
print("-" * 60)

employees.append("Bhomdev")

total = employees.count("Bhomdev")

print("Updated Employee List")
print(employees)

print(f"Bhomdev Appears {total} Time(s)")

# sort()
print("\n" + "-" * 60)
print("sort()")
print("-" * 60)

employees.sort()

print("Employees Sorted Alphabetically")
print(employees)

# reverse()
print("\n" + "-" * 60)
print("reverse()")
print("-" * 60)

employees.reverse()

print("Employees in Reverse Order")
print(employees)

# copy()
print("\n" + "-" * 60)
print("copy()")
print("-" * 60)

employee_backup = employees.copy()

print("Backup Employee List")
print(employee_backup)

# clear()
print("\n" + "-" * 60)
print("clear()")
print("-" * 60)

temporary_list = employee_backup.copy()

temporary_list.clear()

print("Temporary List After clear()")
print(temporary_list)

# List Information
print("\n" + "-" * 60)
print("LIST INFORMATION")
print("-" * 60)

print(f"Current Employee List : {employees}")
print(f"Total Employees       : {len(employees)}")

# END
print("\n" + "=" * 60)
print("Employee List Methods Demonstration Completed.")
print("=" * 60)
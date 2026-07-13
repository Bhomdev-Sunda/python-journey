#        BREAK, CONTINUE & PASS IN PYTHON
print("=" * 60)
print("        EMPLOYEE ACCESS MANAGEMENT SYSTEM")
print("=" * 60)

employees = [
    "Bhomdev",
    "Rahul",
    "Priya",
    "Admin",
    "Aman",
    "Neha"
]

# BREAK
print("\n" + "-" * 60)
print("BREAK STATEMENT")
print("-" * 60)

for employee in employees:

    if employee == "Admin":
        print("Admin Found!")
        print("Stopping Employee Verification...\n")
        break

    print(f"Verified Employee : {employee}")

# CONTINUE
print("-" * 60)
print("CONTINUE STATEMENT")
print("-" * 60)

for employee in employees:

    if employee == "Admin":
        print("Skipping Admin Account...\n")
        continue

    print(f"Employee : {employee}")

# PASS
print("-" * 60)
print("PASS STATEMENT")
print("-" * 60)

for employee in employees:

    if employee == "Admin":
        pass

    print(f"Employee Record : {employee}")

# END
print("\n" + "=" * 60)
print("Employee Management Process Completed Successfully.")
print("=" * 60)
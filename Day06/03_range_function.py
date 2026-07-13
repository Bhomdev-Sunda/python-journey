#               RANGE() FUNCTION IN PYTHON
print("=" * 60)
print("          EMPLOYEE ID GENERATION SYSTEM")
print("=" * 60)

# Generate Employee IDs Using range()
print("\nNew Employee IDs:\n")

for employee_id in range(101, 111):
    print(f"Employee ID : EMP{employee_id}")

# Different Uses of range()
print("\n" + "-" * 60)
print("FIRST 5 EMPLOYEE NUMBERS")
print("-" * 60)

for number in range(1, 6):
    print(f"Employee Number : {number}")

print("\n" + "-" * 60)
print("EMPLOYEE IDs WITH STEP VALUE")
print("-" * 60)

for employee_id in range(100, 111, 2):
    print(f"Employee ID : EMP{employee_id}")

print("\n" + "-" * 60)
print("COUNTDOWN TO OFFICE CLOSING")
print("-" * 60)

for time in range(5, 0, -1):
    print(f"Office closes in {time} minutes...")

print("\nOffice Closed!")

# End
print("\n" + "=" * 60)
print("Employee ID Generation Completed Successfully.")
print("=" * 60)
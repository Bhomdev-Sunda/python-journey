#          Python Looping Through Dictionaries
print("=" * 65)
print("          LOOPING THROUGH DICTIONARIES")
print("=" * 65)

# SAMPLE DICTIONARY

student = {
    "Name": "Bhomdev",
    "Age": 22,
    "Course": "Python",
    "City": "Patiala"
}

print("\nOriginal Dictionary")
print(student)

# LOOP THROUGH KEYS

print("\n" + "=" * 65)
print("1. LOOP THROUGH KEYS")
print("=" * 65)

for key in student:
    print(key)

# LOOP THROUGH VALUES

print("\n" + "=" * 65)
print("2. LOOP THROUGH VALUES")
print("=" * 65)

for value in student.values():
    print(value)

# LOOP THROUGH KEYS USING keys()

print("\n" + "=" * 65)
print("3. LOOP THROUGH KEYS USING keys()")
print("=" * 65)

for key in student.keys():
    print(key)

# LOOP THROUGH KEY-VALUE PAIRS

print("\n" + "=" * 65)
print("4. LOOP THROUGH KEY-VALUE PAIRS")
print("=" * 65)

for key, value in student.items():
    print(f"{key} : {value}")

# PRINT DICTIONARY IN PROFESSIONAL FORMAT

print("\n" + "=" * 65)
print("5. STUDENT INFORMATION")
print("=" * 65)

for key, value in student.items():
    print(f"{key:<10}: {value}")

# LOOP THROUGH EMPLOYEE DICTIONARY

employee = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "IT",
    "Salary": 50000,
    "Experience": "2 Years"
}

print("\n" + "=" * 65)
print("6. EMPLOYEE DETAILS")
print("=" * 65)

for key, value in employee.items():
    print(f"{key:<12}: {value}")

# LOOP WITH SERIAL NUMBER

print("\n" + "=" * 65)
print("7. LOOP WITH SERIAL NUMBER")
print("=" * 65)

count = 1

for key, value in employee.items():
    print(f"{count}. {key:<12}: {value}")
    count += 1

# NESTED DICTIONARY LOOP

students = {
    101: {
        "Name": "Rahul",
        "Course": "Python"
    },

    102: {
        "Name": "Aman",
        "Course": "Java"
    },

    103: {
        "Name": "Bhomdev",
        "Course": "Data Science"
    }
}

print("\n" + "=" * 65)
print("8. LOOP THROUGH NESTED DICTIONARY")
print("=" * 65)

for roll, details in students.items():

    print(f"\nRoll Number : {roll}")

    for key, value in details.items():
        print(f"{key:<10}: {value}")

# DISPLAY ONLY KEYS

print("\n" + "=" * 65)
print("9. DISPLAY ONLY KEYS")
print("=" * 65)

for key in employee.keys():
    print(key)

# DISPLAY ONLY VALUES

print("\n" + "=" * 65)
print("10. DISPLAY ONLY VALUES")
print("=" * 65)

for value in employee.values():
    print(value)

# SEARCH VALUE USING LOOP

print("\n" + "=" * 65)
print("11. SEARCH A KEY")
print("=" * 65)

search_key = input("Enter Key : ").title()

found = False

for key, value in employee.items():

    if key.lower() == search_key.lower():

        print(f"\n{key} : {value}")

        found = True
        break

if not found:
    print("\nKey Not Found.")

# COUNT TOTAL ITEMS

print("\n" + "=" * 65)
print("12. TOTAL ITEMS")
print("=" * 65)

count = 0

for key in employee:
    count += 1

print("Total Items :", count)

# SUMMARY

print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)

print("✔ for key in dictionary")
print("✔ for value in dictionary.values()")
print("✔ for key in dictionary.keys()")
print("✔ for key, value in dictionary.items()")
print("✔ Loop through nested dictionaries")
print("✔ Search keys using loops")
print("✔ Count dictionary items manually")

print("=" * 65)
print("End of looping_dictionary.py")
print("=" * 65)
print("=" * 65)
print("           PYTHON NESTED DICTIONARIES")
print("=" * 65)

# WHAT IS A NESTED DICTIONARY?
# A nested dictionary is a dictionary inside another dictionary.

students = {
    101: {
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    },

    102: {
        "name": "Aman",
        "age": 22,
        "course": "Java"
    },

    103: {
        "name": "Bhomdev",
        "age": 22,
        "course": "Data Science"
    }
}

print("\nStudent Database")
print(students)

# ACCESSING COMPLETE RECORD

print("\n" + "=" * 65)
print("ACCESSING COMPLETE RECORD")
print("=" * 65)

print(students[101])

# ACCESSING INDIVIDUAL VALUES

print("\n" + "=" * 65)
print("ACCESSING INDIVIDUAL VALUES")
print("=" * 65)

print("Student Name :", students[101]["name"])
print("Age          :", students[101]["age"])
print("Course       :", students[101]["course"])

print()

print("Student Name :", students[103]["name"])
print("Age          :", students[103]["age"])
print("Course       :", students[103]["course"])

# ADDING NEW STUDENT

print("\n" + "=" * 65)
print("ADDING NEW STUDENT")
print("=" * 65)

students[104] = {
    "name": "Neha",
    "age": 20,
    "course": "AI"
}

print(students[104])

# UPDATING DATA

print("\n" + "=" * 65)
print("UPDATING STUDENT DETAILS")
print("=" * 65)

students[102]["course"] = "Full Stack Python"

print(students[102])

# ADDING NEW KEY

print("\n" + "=" * 65)
print("ADDING NEW KEY")
print("=" * 65)

students[101]["city"] = "Patiala"

print(students[101])

# DELETING A KEY

print("\n" + "=" * 65)
print("DELETING A KEY")
print("=" * 65)

del students[101]["age"]

print(students[101])

# LOOP THROUGH NESTED DICTIONARY

print("\n" + "=" * 65)
print("DISPLAY ALL STUDENTS")
print("=" * 65)

for roll_no, details in students.items():

    print("-" * 40)

    print("Roll No :", roll_no)

    for key, value in details.items():
        print(f"{key.capitalize():<10}: {value}")

# SEARCH STUDENT

print("\n" + "=" * 65)
print("SEARCH STUDENT")
print("=" * 65)

search_roll = int(input("Enter Roll Number : "))

if search_roll in students:

    print("\nStudent Found")

    print("-" * 40)

    for key, value in students[search_roll].items():
        print(f"{key.capitalize():<10}: {value}")

else:

    print("\nStudent Not Found.")

# COUNT TOTAL STUDENTS

print("\n" + "=" * 65)
print("TOTAL STUDENTS")
print("=" * 65)

print("Total Students :", len(students))

# REAL-LIFE EXAMPLE

print("\n" + "=" * 65)
print("EMPLOYEE DATABASE")
print("=" * 65)

employees = {

    1001: {
        "name": "Rahul",
        "department": "HR",
        "salary": 35000
    },

    1002: {
        "name": "Aman",
        "department": "IT",
        "salary": 50000
    },

    1003: {
        "name": "Priya",
        "department": "Finance",
        "salary": 45000
    }

}

for emp_id, details in employees.items():

    print("\nEmployee ID :", emp_id)

    for key, value in details.items():
        print(f"{key.capitalize():<12}: {value}")

# NESTED DICTIONARY INSIDE DICTIONARY

print("\n" + "=" * 65)
print("COMPANY INFORMATION")
print("=" * 65)

company = {

    "Company": "Tech Solutions",

    "Manager": {

        "Name": "Rohit",
        "Experience": 8,
        "Department": "IT"
    },

    "Address": {

        "City": "Chandigarh",
        "State": "Punjab",
        "Country": "India"
    }

}

print("Company :", company["Company"])

print("Manager :", company["Manager"]["Name"])

print("Experience :", company["Manager"]["Experience"], "Years")

print("City :", company["Address"]["City"])

print("Country :", company["Address"]["Country"])

# SUMMARY

print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)

print("✔ Nested Dictionary = Dictionary inside another dictionary")
print("✔ Access data using multiple keys")
print("✔ Supports add, update and delete operations")
print("✔ Can be looped using nested for loops")
print("✔ Useful for storing structured real-world data")
print("✔ Widely used in JSON, APIs and Databases")

print("=" * 65)
print("End of nested_dictionary.py")
print("=" * 65)
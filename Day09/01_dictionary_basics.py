print("=" * 60)
print("        PYTHON DICTIONARY BASICS")
print("=" * 60)

# WHAT IS A DICTIONARY?

# A dictionary stores data in key-value pairs.

student = {
    "name": "Bhomdev",
    "age": 22,
    "course": "Python",
    "city": "Patiala"
}

print("\nStudent Dictionary")
print(student)

# ACCESSING VALUES

print("\nAccessing Values")

print("Name   :", student["name"])
print("Age    :", student["age"])
print("Course :", student["course"])
print("City   :", student["city"])

# DICTIONARY WITH DIFFERENT DATA TYPES

employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 45000.50,
    "is_active": True
}

print("\nEmployee Details")
print(employee)

# EMPTY DICTIONARY

empty_dict = {}

print("\nEmpty Dictionary")
print(empty_dict)

# USING dict() CONSTRUCTOR

car = dict(
    brand="Toyota",
    model="Fortuner",
    year=2024
)

print("\nCar Dictionary")
print(car)

# DICTIONARY KEYS MUST BE UNIQUE

student_marks = {
    "Python": 95,
    "Java": 88,
    "Python": 99      # Duplicate key
}

print("\nDuplicate Key Example")
print(student_marks)

print("Notice: The last value replaces the previous one.")

# VALUES CAN BE DUPLICATE
subjects = {
    "Subject1": "Python",
    "Subject2": "Python",
    "Subject3": "Java"
}

print("\nDuplicate Values Example")
print(subjects)

# LENGTH OF DICTIONARY
print("\nTotal Student Details :", len(student))

# TYPE OF DICTIONARY
print("\nData Type")
print(type(student))

# DICTIONARY INSIDE A VARIABLE
company = {
    "company": "OpenAI",
    "location": "USA",
    "employees": 5000
}

print("\nCompany Details")

print("Company  :", company["company"])
print("Location :", company["location"])
print("Employees:", company["employees"])

# REAL-LIFE EXAMPLE
mobile = {
    "brand": "Samsung",
    "model": "Galaxy S25",
    "price": 79999,
    "storage": "256GB",
    "color": "Black"
}

print("\nMobile Information")

for key in mobile:
    print(f"{key} : {mobile[key]}")

# MEMBERSHIP OPERATOR
print("\nMembership Operator")

print("brand" in mobile)
print("battery" in mobile)

# SUMMARY
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("✔ Dictionary stores data in key-value pairs.")
print("✔ Keys must be unique.")
print("✔ Values can be duplicated.")
print("✔ Dictionaries are mutable.")
print("✔ Dictionaries can store different data types.")
print("✔ Values are accessed using keys.")
print("✔ Dictionaries are created using {} or dict().")

print("=" * 60)
print("End of dictionary_basics.py")
print("=" * 60)
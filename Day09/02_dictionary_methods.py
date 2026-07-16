print("=" * 60)
print("          PYTHON DICTIONARY METHODS")
print("=" * 60)

# SAMPLE DICTIONARY

student = {
    "name": "Bhomdev",
    "age": 22,
    "course": "Python",
    "city": "Patiala"
}

print("\nOriginal Dictionary")
print(student)

# get()

print("\n1. get() Method")

print("Name :", student.get("name"))
print("Course :", student.get("course"))
print("Phone :", student.get("phone"))      # Returns None

# keys()

print("\n2. keys() Method")

print(student.keys())

# values()

print("\n3. values() Method")

print(student.values())

# items()

print("\n4. items() Method")

print(student.items())

# update()

print("\n5. update() Method")

student.update({
    "city": "Chandigarh",
    "email": "bhomdev@gmail.com"
})

print(student)

# pop()

print("\n6. pop() Method")

removed = student.pop("age")

print("Removed Value :", removed)
print(student)

# popitem()

print("\n7. popitem() Method")

last_item = student.popitem()

print("Removed Pair :", last_item)
print(student)

# copy()

print("\n8. copy() Method")

student_copy = student.copy()

print("Copied Dictionary")
print(student_copy)

# setdefault()

print("\n9. setdefault() Method")

student.setdefault("country", "India")

print(student)

student.setdefault("city", "Delhi")

print(student)

# fromkeys()

print("\n10. fromkeys() Method")

subjects = ("Python", "Java", "SQL")

marks = dict.fromkeys(subjects, 0)

print(marks)

# clear()

print("\n11. clear() Method")

temp = {
    "A": 10,
    "B": 20,
    "C": 30
}

print("Before Clear :", temp)

temp.clear()

print("After Clear :", temp)

# LOOP USING items()

print("\nLooping Through Dictionary")

employee = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "IT",
    "Salary": 50000
}

for key, value in employee.items():
    print(f"{key} : {value}")

# LOOP USING keys()

print("\nUsing keys()")

for key in employee.keys():
    print(key)

# LOOP USING values()

print("\nUsing values()")

for value in employee.values():
    print(value)

# REAL-LIFE EXAMPLE

print("\nEmployee Profile")

profile = {
    "Name": "Bhomdev",
    "Role": "Python Developer",
    "Experience": "Fresher",
    "Skills": "Python"
}

profile.update({
    "Location": "Punjab"
})

for key, value in profile.items():
    print(f"{key} : {value}")

# SUMMARY TABLE

print("\n" + "=" * 60)
print("METHOD SUMMARY")
print("=" * 60)

print("get()        -> Returns value of a key")
print("keys()       -> Returns all keys")
print("values()     -> Returns all values")
print("items()      -> Returns key-value pairs")
print("update()     -> Updates dictionary")
print("pop()        -> Removes a specific key")
print("popitem()    -> Removes last key-value pair")
print("copy()       -> Creates a copy")
print("setdefault() -> Adds key if missing")
print("fromkeys()   -> Creates a new dictionary")
print("clear()      -> Removes all items")

print("=" * 60)
print("End of dictionary_methods.py")
print("=" * 60)
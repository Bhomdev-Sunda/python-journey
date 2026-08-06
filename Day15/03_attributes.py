print("=" * 60)
print("PYTHON ATTRIBUTES")
print("=" * 60)


# ==================================================
# What are Attributes?
# ==================================================

print("\n1. Creating a Student Object")


class Student:
    pass


student1 = Student()

# Adding attributes dynamically
student1.name = "Bhomdev"
student1.age = 22
student1.course = "Python"
student1.marks = 95

print("Student object created successfully.")


# ==================================================
# Accessing Attributes
# ==================================================

print("\n2. Accessing Attributes")

print("Name   :", student1.name)
print("Age    :", student1.age)
print("Course :", student1.course)
print("Marks  :", student1.marks)


# ==================================================
# Creating Another Object
# ==================================================

print("\n3. Multiple Objects Have Different Attributes")

student2 = Student()

student2.name = "Rahul"
student2.age = 21
student2.course = "AI"
student2.marks = 88

print("\nStudent 1")
print(student1.name, student1.age, student1.course, student1.marks)

print("\nStudent 2")
print(student2.name, student2.age, student2.course, student2.marks)


# ==================================================
# Modifying Attributes
# ==================================================

print("\n4. Updating Attributes")

print("Old Marks :", student1.marks)

student1.marks = 99

print("New Marks :", student1.marks)


# ==================================================
# Adding New Attribute
# ==================================================

print("\n5. Adding New Attribute")

student1.city = "Delhi"

print("City :", student1.city)


# ==================================================
# hasattr()
# ==================================================

print("\n6. hasattr()")

print("Has name? :", hasattr(student1, "name"))
print("Has salary? :", hasattr(student1, "salary"))
print("Has city? :", hasattr(student1, "city"))


# ==================================================
# getattr()
# ==================================================

print("\n7. getattr()")

print(getattr(student1, "name"))
print(getattr(student1, "course"))

# Default value if attribute does not exist
print(getattr(student1, "salary", "Not Available"))


# ==================================================
# setattr()
# ==================================================

print("\n8. setattr()")

setattr(student1, "college", "ABC College")

print(student1.college)

setattr(student1, "marks", 100)

print("Updated Marks :", student1.marks)


# ==================================================
# delattr()
# ==================================================

print("\n9. delattr()")

print("City exists :", hasattr(student1, "city"))

delattr(student1, "city")

print("City exists after delete :", hasattr(student1, "city"))


# ==================================================
# Printing Object Dictionary
# ==================================================

print("\n10. __dict__")

print(student1.__dict__)

print(student2.__dict__)


# ==================================================
# Another Example
# ==================================================

print("\n11. Car Example")


class Car:
    pass


car = Car()

car.brand = "Toyota"
car.model = "Fortuner"
car.color = "Black"
car.price = 4500000

print("Brand :", car.brand)
print("Model :", car.model)
print("Color :", car.color)
print("Price :", car.price)


# ==================================================
# Employee Example
# ==================================================

print("\n12. Employee Example")


class Employee:
    pass


emp = Employee()

emp.name = "Amit"
emp.department = "IT"
emp.salary = 65000

print(emp.name)
print(emp.department)
print(emp.salary)


# ==================================================
# Identity Check
# ==================================================

print("\n13. Different Objects")

print(student1 is student2)
print(id(student1))
print(id(student2))


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Attributes store data inside objects.

✔ Each object has its own attributes.

✔ Objects created from the same class can store different values.

✔ Attributes can be added dynamically.

✔ hasattr() checks whether an attribute exists.

✔ getattr() gets an attribute safely.

✔ setattr() creates or updates an attribute.

✔ delattr() removes an attribute.

✔ __dict__ shows all attributes stored in an object.
""")

print("=" * 60)
print("End of Day15 - Attributes")
print("=" * 60)
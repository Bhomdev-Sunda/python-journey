print("=" * 50)
print("PYTHON CLASSES & OBJECTS")
print("=" * 50)


# ==================================================
# What is a Class?
# ==================================================

print("\n1. Creating Our First Class")


class Student:
    pass


print("Student class created successfully.")


# ==================================================
# What is an Object?
# ==================================================

print("\n2. Creating Objects")

student1 = Student()
student2 = Student()
student3 = Student()

print("Three Student objects created.")

print("student1 :", student1)
print("student2 :", student2)
print("student3 :", student3)


# ==================================================
# Checking Object Type
# ==================================================

print("\n3. Type of Object")

print(type(student1))
print(type(student2))


# ==================================================
# Are Objects Different?
# ==================================================

print("\n4. Object Identity")

print(student1 is student2)
print(student1 == student2)

print(id(student1))
print(id(student2))
print(id(student3))


# ==================================================
# Creating Another Class
# ==================================================

print("\n5. Another Class")


class Car:
    pass


car1 = Car()
car2 = Car()

print("Car objects created.")

print(car1)
print(car2)

print(type(car1))


# ==================================================
# Multiple Classes
# ==================================================

print("\n6. Multiple Classes")


class Mobile:
    pass


class Laptop:
    pass


mobile = Mobile()
laptop = Laptop()

print(type(mobile))
print(type(laptop))


# ==================================================
# One Class -> Many Objects
# ==================================================

print("\n7. One Class Can Create Many Objects")


class Dog:
    pass


dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
dog4 = Dog()

print("Dogs created successfully.")

print(dog1)
print(dog2)
print(dog3)
print(dog4)


# ==================================================
# Real-Life Example
# ==================================================

print("\n8. Real-Life Example")


class Employee:
    pass


emp1 = Employee()
emp2 = Employee()

print("Employee 1 :", emp1)
print("Employee 2 :", emp2)


# ==================================================
# Class Names
# ==================================================

print("\n9. Class Naming Convention")

print("Class names use PascalCase.")

print("""
Examples:

Student
BankAccount
Employee
MovieTicket
HotelRoom
Restaurant
ShoppingCart
""")


# ==================================================
# Object Variables
# ==================================================

print("\n10. Object Variables")

student_a = Student()
student_b = Student()

print(student_a)
print(student_b)

print("Both variables store different objects.")


# ==================================================
# Memory Demonstration
# ==================================================

print("\n11. Memory Demonstration")

print("Address of student_a :", id(student_a))
print("Address of student_b :", id(student_b))

if student_a is student_b:
    print("Same Object")
else:
    print("Different Objects")


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

print("""
✔ Class is a blueprint.

✔ Object is an instance of a class.

✔ One class can create many objects.

✔ Every object has its own memory location.

✔ type() tells the object's class.

✔ id() returns the memory address.

✔ 'is' compares object identity.

✔ Class names follow PascalCase naming convention.
""")

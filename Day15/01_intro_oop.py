# ==========================================================
#      Introduction to Object-Oriented Programming (OOP)
#                      Day 15
# ==========================================================

print("=" * 70)
print("      INTRODUCTION TO OBJECT-ORIENTED PROGRAMMING")
print("=" * 70)

# ==========================================================
# WHAT IS OOP?
# ==========================================================

print("\nWHAT IS OOP?")
print("-" * 70)

print("OOP stands for Object-Oriented Programming.")
print("It is a programming paradigm that organizes")
print("code into classes and objects.")
print("OOP helps us write reusable, organized,")
print("and maintainable programs.")

# ==========================================================
# WHY DO WE USE OOP?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE OOP?")
print("=" * 70)

print("1. Code Reusability")
print("2. Better Organization")
print("3. Easy Maintenance")
print("4. Real-World Modeling")
print("5. Improved Scalability")
print("6. Reduced Code Duplication")
print("7. Easy Team Collaboration")

# ==========================================================
# PROCEDURAL PROGRAMMING vs OOP
# ==========================================================

print("\n" + "=" * 70)
print("PROCEDURAL PROGRAMMING vs OOP")
print("=" * 70)

print("\nProcedural Programming")
print("----------------------")
print("• Focuses on functions.")
print("• Data and functions are separate.")
print("• Difficult for large projects.")
print("• Less reusable.")

print("\nObject-Oriented Programming")
print("---------------------------")
print("• Focuses on objects.")
print("• Data and methods stay together.")
print("• Easy to maintain.")
print("• Highly reusable.")

# ==========================================================
# REAL LIFE EXAMPLES
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE EXAMPLES OF OOP")
print("=" * 70)

examples = [

    "Car",
    "Mobile Phone",
    "Laptop",
    "Bank Account",
    "Student",
    "Employee",
    "Book",
    "Hospital",
    "ATM Machine",
    "Shopping Cart"

]

for example in examples:

    print("✔", example)

# ==========================================================
# CLASS vs OBJECT
# ==========================================================

print("\n" + "=" * 70)
print("CLASS vs OBJECT")
print("=" * 70)

print("Class")
print("-----")
print("Blueprint or template.")
print("Example: Car")

print()

print("Object")
print("------")
print("Real instance created from a class.")
print("Example: BMW Car")

# ==========================================================
# SIMPLE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("SIMPLE CLASS EXAMPLE")
print("=" * 70)


class Student:

    pass


student1 = Student()
student2 = Student()

print("Student1 :", student1)
print("Student2 :", student2)

# ==========================================================
# ANOTHER EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("ANIMAL CLASS")
print("=" * 70)


class Animal:

    pass


dog = Animal()
cat = Animal()

print("Dog Object :", dog)
print("Cat Object :", cat)

# ==========================================================
# OBJECT ID
# ==========================================================

print("\n" + "=" * 70)
print("OBJECT ID")
print("=" * 70)

print("Student1 ID :", id(student1))
print("Student2 ID :", id(student2))

# ==========================================================
# TYPE OF OBJECT
# ==========================================================

print("\n" + "=" * 70)
print("TYPE OF OBJECT")
print("=" * 70)

print(type(student1))
print(type(dog))

# ==========================================================
# isinstance()
# ==========================================================

print("\n" + "=" * 70)
print("isinstance()")
print("=" * 70)

print(isinstance(student1, Student))
print(isinstance(dog, Animal))

# ==========================================================
# MULTIPLE OBJECTS
# ==========================================================

print("\n" + "=" * 70)
print("MULTIPLE OBJECTS")
print("=" * 70)


class Car:

    pass


car1 = Car()
car2 = Car()
car3 = Car()

print("Created 3 Car Objects Successfully.")

# ==========================================================
# ADVANTAGES OF OOP
# ==========================================================

print("\n" + "=" * 70)
print("ADVANTAGES OF OOP")
print("=" * 70)

advantages = [

    "Reusable Code",

    "Easy Maintenance",

    "Better Security",

    "Scalable Applications",

    "Real World Modeling",

    "Readable Code",

    "Less Duplication",

    "Professional Development"

]

for item in advantages:

    print("✔", item)

# ==========================================================
# WHERE IS OOP USED?
# ==========================================================

print("\n" + "=" * 70)
print("WHERE IS OOP USED?")
print("=" * 70)

applications = [

    "Python Applications",

    "Django",

    "Flask",

    "Game Development",

    "Desktop Software",

    "AI & Machine Learning",

    "Mobile Applications",

    "Banking Systems",

    "Hospital Software",

    "E-Commerce"

]

for app in applications:

    print("✔", app)

# ==========================================================
# COMMON OOP TERMINOLOGY
# ==========================================================

print("\n" + "=" * 70)
print("COMMON OOP TERMS")
print("=" * 70)

print("Class")
print("Object")
print("Attribute")
print("Method")
print("Constructor")
print("Inheritance")
print("Polymorphism")
print("Encapsulation")
print("Abstraction")

# ==========================================================
# FOUR PILLARS OF OOP
# ==========================================================

print("\n" + "=" * 70)
print("FOUR PILLARS OF OOP")
print("=" * 70)

print("1. Encapsulation")
print("2. Inheritance")
print("3. Polymorphism")
print("4. Abstraction")

print("\nWe'll learn the last four in upcoming days.")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Thinking class and object are the same.")
print("❌ Creating unnecessary classes.")
print("❌ Forgetting to create objects.")
print("❌ Mixing procedural and OOP concepts.")
print("❌ Not understanding real-world modeling.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use meaningful class names.")
print("✔ One class should represent one concept.")
print("✔ Keep code organized.")
print("✔ Think in terms of real-world objects.")
print("✔ Follow naming conventions.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ OOP stands for Object-Oriented Programming.")
print("✔ OOP uses Classes and Objects.")
print("✔ A Class is a blueprint.")
print("✔ An Object is an instance of a class.")
print("✔ OOP makes programs reusable.")
print("✔ OOP is used in almost every modern software.")
print("✔ Python fully supports Object-Oriented Programming.")

print("=" * 70)
print("End of 01_intro_oop.py")
print("=" * 70)
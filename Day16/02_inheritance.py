print("=" * 70)
print("              INHERITANCE IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS INHERITANCE?
# ==========================================================

# Inheritance allows one class to acquire
# the properties and methods of another class.
#
# Existing Class  -> Parent / Base Class
# New Class       -> Child / Derived Class

print("\nWHAT IS INHERITANCE?")
print("-" * 70)

print("Inheritance allows one class to reuse")
print("the properties and methods of another class.")
print("It promotes code reusability and reduces duplication.")

# ==========================================================
# WHY USE INHERITANCE?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE INHERITANCE?")
print("=" * 70)

print("1. Code Reusability")
print("2. Less Code Duplication")
print("3. Easy Maintenance")
print("4. Better Organization")
print("5. Extensibility")

# ==========================================================
# BASIC INHERITANCE
# ==========================================================

print("\n" + "=" * 70)
print("1. BASIC INHERITANCE")
print("=" * 70)


class Animal:

    def speak(self):

        print("Animals can make sounds.")


class Dog(Animal):

    pass


dog = Dog()

dog.speak()

# ==========================================================
# SINGLE INHERITANCE
# ==========================================================

print("\n" + "=" * 70)
print("2. SINGLE INHERITANCE")
print("=" * 70)


class Person:

    def show_name(self):

        print("Name : Bhomdev")


class Student(Person):

    def show_course(self):

        print("Course : Python")


student = Student()

student.show_name()
student.show_course()

# ==========================================================
# MULTILEVEL INHERITANCE
# ==========================================================

print("\n" + "=" * 70)
print("3. MULTILEVEL INHERITANCE")
print("=" * 70)


class Grandfather:

    def grandfather_property(self):

        print("Grandfather's House")


class Father(Grandfather):

    def father_property(self):

        print("Father's Car")


class Son(Father):

    def son_property(self):

        print("Son's Laptop")


son = Son()

son.grandfather_property()
son.father_property()
son.son_property()

# ==========================================================
# MULTIPLE INHERITANCE
# ==========================================================

print("\n" + "=" * 70)
print("4. MULTIPLE INHERITANCE")
print("=" * 70)


class Father:

    def father_skill(self):

        print("Driving")


class Mother:

    def mother_skill(self):

        print("Cooking")


class Child(Father, Mother):

    def child_skill(self):

        print("Programming")


child = Child()

child.father_skill()
child.mother_skill()
child.child_skill()

# ==========================================================
# HIERARCHICAL INHERITANCE
# ==========================================================

print("\n" + "=" * 70)
print("5. HIERARCHICAL INHERITANCE")
print("=" * 70)


class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    pass


class Bike(Vehicle):

    pass


car = Car()
bike = Bike()

car.start()
bike.start()

# ==========================================================
# HYBRID INHERITANCE (Concept)
# ==========================================================

print("\n" + "=" * 70)
print("6. HYBRID INHERITANCE")
print("=" * 70)

print("Hybrid inheritance is a combination")
print("of two or more inheritance types.")
print("Python supports hybrid inheritance.")

# ==========================================================
# METHOD INHERITANCE
# ==========================================================

print("\n" + "=" * 70)
print("7. METHOD INHERITANCE")
print("=" * 70)


class Employee:

    def login(self):

        print("Employee Logged In")


class Manager(Employee):

    pass


manager = Manager()

manager.login()

# ==========================================================
# INHERITING ATTRIBUTES
# ==========================================================

print("\n" + "=" * 70)
print("8. INHERITING ATTRIBUTES")
print("=" * 70)


class Animal:

    kingdom = "Animalia"


class Lion(Animal):

    pass


lion = Lion()

print("Kingdom :", lion.kingdom)

# ==========================================================
# isinstance()
# ==========================================================

print("\n" + "=" * 70)
print("9. isinstance()")
print("=" * 70)

print(isinstance(lion, Lion))
print(isinstance(lion, Animal))

# ==========================================================
# issubclass()
# ==========================================================

print("\n" + "=" * 70)
print("10. issubclass()")
print("=" * 70)

print(issubclass(Lion, Animal))
print(issubclass(Car, Vehicle))

# ==========================================================
# REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("11. REAL-LIFE EXAMPLE")
print("=" * 70)


class BankAccount:

    def account_type(self):

        print("Savings Account")


class PremiumAccount(BankAccount):

    def premium_benefits(self):

        print("Free Insurance")
        print("Cashback")
        print("Priority Support")


premium = PremiumAccount()

premium.account_type()
premium.premium_benefits()

# ==========================================================
# TYPES OF INHERITANCE SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("TYPES OF INHERITANCE")
print("=" * 70)

print("1. Single")
print("2. Multiple")
print("3. Multilevel")
print("4. Hierarchical")
print("5. Hybrid")

# ==========================================================
# BENEFITS
# ==========================================================

print("\n" + "=" * 70)
print("BENEFITS OF INHERITANCE")
print("=" * 70)

benefits = [

    "Code Reusability",

    "Easy Maintenance",

    "Less Duplication",

    "Improved Readability",

    "Easy Extension",

    "Professional Design"

]

for item in benefits:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting parent class name.")
print("❌ Creating unnecessary inheritance.")
print("❌ Confusing inheritance with composition.")
print("❌ Using inheritance where it isn't needed.")
print("❌ Forgetting indentation.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Inherit only when there is an 'is-a' relationship.")
print("✔ Keep parent classes generic.")
print("✔ Avoid deep inheritance chains.")
print("✔ Write meaningful class names.")
print("✔ Reuse code whenever possible.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Banking Systems",

    "Hospital Management",

    "School Management",

    "Employee Management",

    "Vehicle Management",

    "Game Development",

    "E-commerce",

    "Library Systems"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Inheritance allows code reuse.")
print("✔ Child class inherits parent properties.")
print("✔ Parent is also called Base Class.")
print("✔ Child is also called Derived Class.")
print("✔ Python supports five inheritance types.")
print("✔ isinstance() checks object type.")
print("✔ issubclass() checks inheritance relationship.")

print("=" * 70)
print("End of 02_inheritance.py")
print("=" * 70)
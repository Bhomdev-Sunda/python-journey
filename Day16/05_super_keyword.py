print("=" * 70)
print("             super() KEYWORD IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS super()?
# ==========================================================

# super() is used to access the parent class.
#
# It allows us to call:
# ✔ Parent Constructor (__init__)
# ✔ Parent Methods
# ✔ Parent Attributes (indirectly)

print("\nWHAT IS super()?")
print("-" * 70)

print("super() is a built-in Python function.")
print("It gives access to the parent class.")
print("It helps reuse parent class code.")

# ==========================================================
# WHY DO WE USE super()?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE super()?")
print("=" * 70)

print("1. Reuse Parent Code")
print("2. Avoid Code Duplication")
print("3. Call Parent Constructor")
print("4. Call Parent Methods")
print("5. Better Readability")

# ==========================================================
# BASIC EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("1. BASIC EXAMPLE")
print("=" * 70)


class Parent:

    def show(self):

        print("This is Parent Class.")


class Child(Parent):

    def display(self):

        print("This is Child Class.")


child = Child()

child.show()
child.display()

# ==========================================================
# CALLING PARENT METHOD USING super()
# ==========================================================

print("\n" + "=" * 70)
print("2. CALLING PARENT METHOD")
print("=" * 70)


class Animal:

    def speak(self):

        print("Animals make sounds.")


class Dog(Animal):

    def speak(self):

        super().speak()

        print("Dog Barks.")


dog = Dog()

dog.speak()

# ==========================================================
# CALLING PARENT CONSTRUCTOR
# ==========================================================

print("\n" + "=" * 70)
print("3. CALLING PARENT CONSTRUCTOR")
print("=" * 70)


class Person:

    def __init__(self, name):

        self.name = name

        print("Parent Constructor Executed")


class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course

        print("Child Constructor Executed")


student = Student("Bhomdev", "Python")

print("Name   :", student.name)
print("Course :", student.course)

# ==========================================================
# ACCESSING PARENT ATTRIBUTES
# ==========================================================

print("\n" + "=" * 70)
print("4. ACCESSING PARENT ATTRIBUTES")
print("=" * 70)


class Employee:

    def __init__(self, name):

        self.name = name


class Manager(Employee):

    def __init__(self, name, department):

        super().__init__(name)

        self.department = department


manager = Manager("Rahul", "IT")

print("Name       :", manager.name)
print("Department :", manager.department)

# ==========================================================
# METHOD OVERRIDING WITH super()
# ==========================================================

print("\n" + "=" * 70)
print("5. METHOD OVERRIDING")
print("=" * 70)


class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    def start(self):

        super().start()

        print("Car is Ready to Drive")


car = Car()

car.start()

# ==========================================================
# MULTILEVEL INHERITANCE
# ==========================================================

print("\n" + "=" * 70)
print("6. MULTILEVEL INHERITANCE")
print("=" * 70)


class Grandfather:

    def show(self):

        print("Grandfather")


class Father(Grandfather):

    def show(self):

        super().show()

        print("Father")


class Son(Father):

    def show(self):

        super().show()

        print("Son")


son = Son()

son.show()

# ==========================================================
# BANK ACCOUNT EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("7. BANK ACCOUNT")
print("=" * 70)


class BankAccount:

    def __init__(self, holder):

        self.holder = holder

        print("Bank Account Created")


class SavingsAccount(BankAccount):

    def __init__(self, holder, balance):

        super().__init__(holder)

        self.balance = balance


account = SavingsAccount("Bhomdev", 50000)

print("Holder  :", account.holder)
print("Balance :", account.balance)

# ==========================================================
# EMPLOYEE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("8. EMPLOYEE EXAMPLE")
print("=" * 70)


class Employee:

    def work(self):

        print("Employee Working")


class Developer(Employee):

    def work(self):

        super().work()

        print("Writing Python Code")


developer = Developer()

developer.work()

# ==========================================================
# isinstance() AND issubclass()
# ==========================================================

print("\n" + "=" * 70)
print("9. TYPE CHECKING")
print("=" * 70)

print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))
print(issubclass(Car, Vehicle))

# ==========================================================
# BENEFITS OF super()
# ==========================================================

print("\n" + "=" * 70)
print("BENEFITS OF super()")
print("=" * 70)

benefits = [

    "Code Reusability",

    "Cleaner Code",

    "Easy Maintenance",

    "Less Duplication",

    "Professional OOP",

    "Supports Inheritance"

]

for item in benefits:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting parentheses after super().")
print("❌ Calling parent constructor manually.")
print("❌ Using super() without inheritance.")
print("❌ Forgetting to call super().__init__().")
print("❌ Creating duplicate initialization code.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Prefer super() over parent class name.")
print("✔ Call parent constructor first.")
print("✔ Avoid duplicate code.")
print("✔ Use meaningful class names.")
print("✔ Use super() when overriding methods.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Employee Management",

    "Banking Software",

    "Hospital Management",

    "Vehicle Systems",

    "School Management",

    "Game Development",

    "E-commerce",

    "Desktop Applications"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ super() accesses the parent class.")
print("✔ It can call parent constructors.")
print("✔ It can call parent methods.")
print("✔ It reduces code duplication.")
print("✔ It makes inheritance cleaner.")
print("✔ It is widely used in professional Python projects.")

print("=" * 70)
print("End of 05_super_keyword.py")
print("=" * 70)
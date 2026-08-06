print("=" * 60)
print("PYTHON CONSTRUCTOR (__init__)")
print("=" * 60)

# ==================================================
# What is a Constructor?
# ==================================================

print("\n1. Basic Constructor Example")


class Student:

    def __init__(self):
        print("Constructor Called!")
        print("Student Object Created Successfully.")


student1 = Student()
student2 = Student()


# ==================================================
# Constructor with Parameters
# ==================================================

print("\n2. Constructor with Parameters")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name :", self.name)
        print("Salary        :", self.salary)


emp1 = Employee("Bhomdev", 80000)
emp2 = Employee("Rahul", 50000)

emp1.display()
print()
emp2.display()


# ==================================================
# Multiple Objects
# ==================================================

print("\n3. Multiple Objects")


class Car:

    def __init__(self, brand, model, color):

        self.brand = brand
        self.model = model
        self.color = color

    def show(self):

        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Color :", self.color)


car1 = Car("Toyota", "Fortuner", "Black")
car2 = Car("Hyundai", "Creta", "White")

print("\nCar 1")
car1.show()

print("\nCar 2")
car2.show()


# ==================================================
# Default Parameter Values
# ==================================================

print("\n4. Constructor with Default Values")


class Mobile:

    def __init__(self, company="Unknown", price=0):

        self.company = company
        self.price = price

    def display(self):

        print(self.company, "-", self.price)


mobile1 = Mobile()

mobile2 = Mobile("Samsung", 45000)

mobile3 = Mobile("Apple", 95000)

mobile1.display()
mobile2.display()
mobile3.display()


# ==================================================
# Student Result Example
# ==================================================

print("\n5. Student Result")


class StudentResult:

    def __init__(self, name, maths, science, english):

        self.name = name
        self.maths = maths
        self.science = science
        self.english = english

    def percentage(self):

        total = self.maths + self.science + self.english
        percentage = total / 3

        print("Student :", self.name)
        print("Percentage :", percentage)


student = StudentResult("Bhomdev", 95, 92, 98)

student.percentage()


# ==================================================
# Bank Account Example
# ==================================================

print("\n6. Bank Account")


class BankAccount:

    def __init__(self, holder, balance):

        self.holder = holder
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
        print("Deposited :", amount)

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount
            print("Withdrawn :", amount)

        else:

            print("Insufficient Balance")

    def show_balance(self):

        print("Account Holder :", self.holder)
        print("Current Balance :", self.balance)


account = BankAccount("Bhomdev", 10000)

account.show_balance()

account.deposit(3000)

account.withdraw(2500)

account.show_balance()


# ==================================================
# Constructor Executes Automatically
# ==================================================

print("\n7. Constructor Runs Automatically")


class Demo:

    def __init__(self):

        print("I run automatically whenever an object is created.")


demo = Demo()


# ==================================================
# Constructor with Different Objects
# ==================================================

print("\n8. Every Object Has Different Data")


class Laptop:

    def __init__(self, brand, ram):

        self.brand = brand
        self.ram = ram

    def details(self):

        print(self.brand, "-", self.ram, "GB RAM")


lap1 = Laptop("ASUS", 16)
lap2 = Laptop("Dell", 8)
lap3 = Laptop("HP", 32)

lap1.details()
lap2.details()
lap3.details()


# ==================================================
# Printing Object Dictionary
# ==================================================

print("\n9. Object Dictionary")


print(account.__dict__)

print(student.__dict__)


# ==================================================
# Object Identity
# ==================================================

print("\n10. Different Objects")

print(id(emp1))
print(id(emp2))

print(emp1 is emp2)


# ==================================================
# Common Mistakes
# ==================================================

print("\n11. Common Mistakes")

print("""
Wrong:

def init():

Correct:

def __init__(self):

------------------------------------

Wrong:

name = name

Correct:

self.name = name

------------------------------------

The constructor is called automatically.
Never call __init__() directly in normal code.
""")


# ==================================================
# Constructor vs Normal Method
# ==================================================

print("\n12. Constructor vs Normal Method")

print("""
Constructor

✔ Automatically called
✔ Used for initialization
✔ Name is __init__

Normal Method

✔ Called manually
✔ Performs operations
✔ Can have any valid name
""")


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ __init__() is called a constructor.

✔ It executes automatically when an object is created.

✔ Constructors initialize object data.

✔ self refers to the current object.

✔ Every object receives its own values.

✔ Constructors make object creation simple.

✔ Constructors are widely used in real-world projects.

✔ Most Python classes use constructors.
""")

print("=" * 60)
print("End of Day15 - Constructor")
print("=" * 60)
print("=" * 60)
print("PYTHON SELF KEYWORD")
print("=" * 60)

# ==================================================
# What is self?
# ==================================================

print("\n1. Basic Example")


class Student:

    def greet(self):
        print("Hello Student!")
        print("self =", self)


student1 = Student()
student2 = Student()

student1.greet()
student2.greet()

print("\nMemory Address of student1 :", id(student1))
print("Memory Address of student2 :", id(student2))

print("\nNotice that self is the object that calls the method.")


# ==================================================
# self Refers to Current Object
# ==================================================

print("\n2. self Refers to Current Object")


class Employee:

    def show(self):
        print("Name :", self.name)
        print("Salary :", self.salary)


emp1 = Employee()
emp1.name = "Bhomdev"
emp1.salary = 80000

emp2 = Employee()
emp2.name = "Rahul"
emp2.salary = 55000

emp1.show()
print()
emp2.show()


# ==================================================
# Using self to Store Data
# ==================================================

print("\n3. Using self to Store Instance Variables")


class Car:

    def set_details(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)


car1 = Car()
car1.set_details("Toyota", "Fortuner")
car1.display()

print()

car2 = Car()
car2.set_details("Hyundai", "Creta")
car2.display()


# ==================================================
# Multiple Objects
# ==================================================

print("\n4. Every Object Has Its Own Data")


class Mobile:

    def set_mobile(self, company, price):
        self.company = company
        self.price = price

    def show_mobile(self):
        print(self.company, "-", self.price)


mobile1 = Mobile()
mobile1.set_mobile("Samsung", 45000)

mobile2 = Mobile()
mobile2.set_mobile("Apple", 90000)

mobile3 = Mobile()
mobile3.set_mobile("OnePlus", 38000)

mobile1.show_mobile()
mobile2.show_mobile()
mobile3.show_mobile()


# ==================================================
# self Can Call Another Method
# ==================================================

print("\n5. Calling One Method from Another")


class Demo:

    def first(self):
        print("Inside First Method")
        self.second()

    def second(self):
        print("Inside Second Method")


demo = Demo()

demo.first()


# ==================================================
# Printing self
# ==================================================

print("\n6. Printing self")


class Laptop:

    def who_am_i(self):
        print(self)


laptop = Laptop()

laptop.who_am_i()

print("Object Address :", laptop)


# ==================================================
# Python Internally Passes self
# ==================================================

print("\n7. Python Automatically Passes self")


class Test:

    def display(self):
        print("Hello Python")


obj = Test()

obj.display()

print("""
Internally Python does this:

Test.display(obj)

Python automatically sends the object
as the first argument (self).
""")


# ==================================================
# self vs Normal Variable
# ==================================================

print("\n8. self vs Local Variable")


class Person:

    def set_data(self, name):

        self.name = name

        local_variable = "Temporary Variable"

        print("Local Variable :", local_variable)

    def display(self):
        print("Name :", self.name)


person = Person()

person.set_data("Bhomdev")

person.display()


# ==================================================
# Another Example
# ==================================================

print("\n9. Bank Account Example")


class BankAccount:

    def create_account(self, holder, balance):

        self.holder = holder
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):

        print("Account Holder :", self.holder)
        print("Balance :", self.balance)


account = BankAccount()

account.create_account("Bhomdev", 10000)

account.deposit(5000)

account.withdraw(3000)

account.show_balance()


# ==================================================
# Common Mistake
# ==================================================

print("\n10. Common Mistake")

print("""
Wrong:

name = name

Correct:

self.name = name

Without self,
the value is NOT stored inside the object.
""")


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ self refers to the current object.

✔ Every instance method must have self
as its first parameter.

✔ Python automatically passes the object
to self when a method is called.

✔ self is used to create and access
instance variables.

✔ Every object has its own copy of
instance variables.

✔ self allows one method to call
another method inside the same class.

✔ Without self, data is not stored
inside the object.
""")

print("=" * 60)
print("End of Day15 - Self Keyword")
print("=" * 60)
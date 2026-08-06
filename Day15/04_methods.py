print("=" * 60)
print("PYTHON METHODS")
print("=" * 60)


# ==================================================
# What is a Method?
# ==================================================

print("\n1. Creating Our First Method")


class Student:

    def greet(self):
        print("Hello! Welcome to Python OOP.")


student = Student()

student.greet()


# ==================================================
# Method with Attributes
# ==================================================

print("\n2. Method Using Attributes")


class Employee:

    def show_details(self):
        print("Employee Name :", self.name)
        print("Department    :", self.department)
        print("Salary        :", self.salary)


emp = Employee()

emp.name = "Bhomdev"
emp.department = "AI Engineer"
emp.salary = 80000

emp.show_details()


# ==================================================
# Multiple Objects Using Same Method
# ==================================================

print("\n3. Multiple Objects")


class Car:

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Color :", self.color)


car1 = Car()

car1.brand = "Toyota"
car1.model = "Fortuner"
car1.color = "Black"

car2 = Car()

car2.brand = "Hyundai"
car2.model = "Creta"
car2.color = "White"

print("\nCar 1")
car1.display()

print("\nCar 2")
car2.display()


# ==================================================
# Method with Parameters
# ==================================================

print("\n4. Method with Parameters")


class Calculator:

    def add(self, a, b):
        print("Addition =", a + b)

    def multiply(self, a, b):
        print("Multiplication =", a * b)


calc = Calculator()

calc.add(10, 20)
calc.multiply(5, 6)


# ==================================================
# Returning Values
# ==================================================

print("\n5. Returning Values")


class Rectangle:

    def area(self, length, width):
        return length * width


rect = Rectangle()

result = rect.area(10, 5)

print("Area =", result)


# ==================================================
# Bank Account Example
# ==================================================

print("\n6. Bank Account")


class BankAccount:

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
        print("Current Balance :", self.balance)


account = BankAccount()

account.balance = 5000

account.show_balance()

account.deposit(2000)

account.withdraw(1500)

account.withdraw(10000)

account.show_balance()


# ==================================================
# Student Example
# ==================================================

print("\n7. Student Example")


class StudentResult:

    def calculate_percentage(self):
        total = self.maths + self.science + self.english
        percentage = total / 3
        print("Percentage =", percentage)


student = StudentResult()

student.maths = 90
student.science = 85
student.english = 95

student.calculate_percentage()


# ==================================================
# Shopping Cart
# ==================================================

print("\n8. Shopping Cart")


class ShoppingCart:

    def total_bill(self):
        total = self.price1 + self.price2 + self.price3
        print("Total Bill =", total)


cart = ShoppingCart()

cart.price1 = 450
cart.price2 = 850
cart.price3 = 300

cart.total_bill()


# ==================================================
# Movie Example
# ==================================================

print("\n9. Movie Example")


class Movie:

    def movie_info(self):
        print("Movie :", self.name)
        print("Rating :", self.rating)
        print("Language :", self.language)


movie = Movie()

movie.name = "The Social Network"
movie.rating = 8.5
movie.language = "English"

movie.movie_info()


# ==================================================
# Method Calling Another Method
# ==================================================

print("\n10. One Method Calling Another")


class Demo:

    def first(self):
        print("First Method")
        self.second()

    def second(self):
        print("Second Method")


demo = Demo()

demo.first()


# ==================================================
# Built-in Methods
# ==================================================

print("\n11. Built-in Methods")

numbers = [5, 2, 8, 1]

print("Original List :", numbers)

numbers.append(10)
numbers.sort()

print("Updated List :", numbers)

print("""
append() and sort() are also methods.
They belong to Python's list class.
""")


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ A method is a function inside a class.

✔ Methods define what an object can do.

✔ Methods always receive 'self' as the first parameter.

✔ Methods can access object attributes.

✔ Methods can take additional parameters.

✔ Methods can return values.

✔ One method can call another method.

✔ Built-in objects like list and string also have methods.
""")

print("=" * 60)
print("End of Day15 - Methods")
print("=" * 60)
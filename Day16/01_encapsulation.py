print("=" * 70)
print("             ENCAPSULATION IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS ENCAPSULATION?
# ==========================================================

# Encapsulation means wrapping data (variables)
# and methods (functions) into a single unit (class).
#
# It also helps protect data from direct access.

print("\nWHAT IS ENCAPSULATION?")
print("-" * 70)

print("Encapsulation combines data and methods into one class.")
print("It protects object data from unauthorized access.")
print("It improves security and code organization.")

# ==========================================================
# WHY DO WE USE ENCAPSULATION?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE ENCAPSULATION?")
print("=" * 70)

print("1. Data Security")
print("2. Better Code Organization")
print("3. Data Hiding")
print("4. Easy Maintenance")
print("5. Better Control Over Data")

# ==========================================================
# PUBLIC MEMBERS
# ==========================================================

print("\n" + "=" * 70)
print("1. PUBLIC MEMBERS")
print("=" * 70)


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student = Student("Bhomdev", 22)

print("Name :", student.name)
print("Age  :", student.age)

student.age = 23

print("Updated Age :", student.age)

# ==========================================================
# PROTECTED MEMBERS
# ==========================================================

print("\n" + "=" * 70)
print("2. PROTECTED MEMBERS")
print("=" * 70)


class Employee:

    def __init__(self, name, salary):

        self.name = name
        self._salary = salary


employee = Employee("Rahul", 50000)

print("Employee :", employee.name)
print("Salary :", employee._salary)

print("\nProtected members should not be accessed directly.")
print("The single underscore (_) is only a naming convention.")

# ==========================================================
# PRIVATE MEMBERS
# ==========================================================

print("\n" + "=" * 70)
print("3. PRIVATE MEMBERS")
print("=" * 70)


class BankAccount:

    def __init__(self, holder, balance):

        self.holder = holder
        self.__balance = balance


account = BankAccount("Bhomdev", 25000)

print("Account Holder :", account.holder)

try:

    print(account.__balance)

except AttributeError as error:

    print(error)

# ==========================================================
# NAME MANGLING
# ==========================================================

print("\n" + "=" * 70)
print("4. NAME MANGLING")
print("=" * 70)

print("Private variables are internally renamed.")

print("Accessing Private Variable Using Name Mangling:")

print(account._BankAccount__balance)

# ==========================================================
# GETTER METHOD
# ==========================================================

print("\n" + "=" * 70)
print("5. GETTER METHOD")
print("=" * 70)


class Account:

    def __init__(self, balance):

        self.__balance = balance

    def get_balance(self):

        return self.__balance


account1 = Account(10000)

print("Balance :", account1.get_balance())

# ==========================================================
# SETTER METHOD
# ==========================================================

print("\n" + "=" * 70)
print("6. SETTER METHOD")
print("=" * 70)


class Wallet:

    def __init__(self):

        self.__money = 0

    def set_money(self, amount):

        if amount >= 0:

            self.__money = amount

        else:

            print("Money cannot be negative.")

    def get_money(self):

        return self.__money


wallet = Wallet()

wallet.set_money(5000)

print("Money :", wallet.get_money())

wallet.set_money(-500)

# ==========================================================
# GETTER + SETTER
# ==========================================================

print("\n" + "=" * 70)
print("7. GETTER + SETTER")
print("=" * 70)


class Mobile:

    def __init__(self):

        self.__price = 0

    def set_price(self, price):

        if price > 0:

            self.__price = price

        else:

            print("Invalid Price.")

    def get_price(self):

        return self.__price


phone = Mobile()

phone.set_price(25000)

print("Mobile Price :", phone.get_price())

# ==========================================================
# REAL-LIFE ATM EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("8. ATM EXAMPLE")
print("=" * 70)


class ATM:

    def __init__(self, balance):

        self.__balance = balance

    def deposit(self, amount):

        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

        else:

            print("Insufficient Balance.")

    def show_balance(self):

        print("Balance :", self.__balance)


atm = ATM(10000)

atm.deposit(5000)

atm.withdraw(3000)

atm.show_balance()

# ==========================================================
# BENEFITS OF ENCAPSULATION
# ==========================================================

print("\n" + "=" * 70)
print("BENEFITS OF ENCAPSULATION")
print("=" * 70)

benefits = [

    "Data Hiding",

    "Better Security",

    "Easy Maintenance",

    "Code Reusability",

    "Controlled Access",

    "Cleaner Code"

]

for item in benefits:

    print("✔", item)

# ==========================================================
# ACCESS MODIFIERS SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("ACCESS MODIFIERS")
print("=" * 70)

print("Public    : variable")
print("Protected : _variable")
print("Private   : __variable")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Accessing private variables directly.")
print("❌ Confusing protected with private.")
print("❌ Ignoring getter/setter methods.")
print("❌ Using name mangling unnecessarily.")
print("❌ Exposing sensitive data.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Keep sensitive data private.")
print("✔ Use getter methods to read data.")
print("✔ Use setter methods to validate data.")
print("✔ Don't modify private data directly.")
print("✔ Write meaningful method names.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Machine",

    "Banking Software",

    "Hospital Management",

    "Student Management",

    "Employee Records",

    "Online Shopping",

    "Payment Systems",

    "Inventory Management"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Encapsulation combines data and methods.")
print("✔ Public members are accessible everywhere.")
print("✔ Protected members use a single underscore (_).")
print("✔ Private members use double underscores (__).")
print("✔ Getter methods read private data.")
print("✔ Setter methods update private data safely.")
print("✔ Encapsulation improves security and maintainability.")

print("=" * 70)
print("End of 01_encapsulation.py")
print("=" * 70)
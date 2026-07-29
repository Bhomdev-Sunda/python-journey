# ==========================================================
#        Python Custom Exceptions - Day 14
# ==========================================================

print("=" * 70)
print("           PYTHON CUSTOM EXCEPTIONS")
print("=" * 70)

# ==========================================================
# WHAT IS A CUSTOM EXCEPTION?
# ==========================================================

# A custom exception is a user-defined exception.
#
# We create our own exception class by inheriting
# from Python's built-in Exception class.
#
# Custom exceptions make our programs easier to
# understand and maintain.

print("\nA custom exception is created by the programmer.")

# ==========================================================
# WHY USE CUSTOM EXCEPTIONS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE CUSTOM EXCEPTIONS?")
print("=" * 70)

print("1. Improve code readability.")
print("2. Handle business rules.")
print("3. Display meaningful messages.")
print("4. Improve debugging.")
print("5. Professional programming practice.")

# ==========================================================
# SIMPLE CUSTOM EXCEPTION
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE CUSTOM EXCEPTION")
print("=" * 70)


class MyError(Exception):

    pass


try:

    raise MyError("This is my custom exception.")

except MyError as error:

    print(error)

# ==========================================================
# AGE VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("2. AGE VALIDATION")
print("=" * 70)


class InvalidAgeError(Exception):

    pass


try:

    age = int(input("Enter Your Age : "))

    if age < 18:

        raise InvalidAgeError("Age must be at least 18.")

    print("You are eligible.")

except InvalidAgeError as error:

    print(error)

# ==========================================================
# PASSWORD VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("3. PASSWORD VALIDATION")
print("=" * 70)


class WeakPasswordError(Exception):

    pass


try:

    password = input("Create Password : ")

    if len(password) < 8:

        raise WeakPasswordError(
            "Password must contain at least 8 characters."
        )

    print("Strong Password.")

except WeakPasswordError as error:

    print(error)

# ==========================================================
# BANK BALANCE
# ==========================================================

print("\n" + "=" * 70)
print("4. BANK WITHDRAWAL")
print("=" * 70)


class InsufficientBalanceError(Exception):

    pass


balance = 5000

try:

    amount = int(input("Enter Withdrawal Amount : "))

    if amount > balance:

        raise InsufficientBalanceError(
            "Insufficient Balance."
        )

    balance -= amount

    print("Remaining Balance :", balance)

except InsufficientBalanceError as error:

    print(error)

# ==========================================================
# STUDENT MARKS
# ==========================================================

print("\n" + "=" * 70)
print("5. STUDENT MARKS")
print("=" * 70)


class InvalidMarksError(Exception):

    pass


try:

    marks = int(input("Enter Marks : "))

    if marks < 0 or marks > 100:

        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

    print("Marks :", marks)

except InvalidMarksError as error:

    print(error)

# ==========================================================
# LOGIN VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("6. LOGIN VALIDATION")
print("=" * 70)


class LoginError(Exception):

    pass


correct_password = "python123"

try:

    password = input("Enter Password : ")

    if password != correct_password:

        raise LoginError("Incorrect Password.")

    print("Login Successful.")

except LoginError as error:

    print(error)

# ==========================================================
# FILE VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("7. FILE VALIDATION")
print("=" * 70)


class InvalidFileError(Exception):

    pass


try:

    filename = input("Enter File Name : ")

    if not filename.endswith(".txt"):

        raise InvalidFileError(
            "Only .txt files are allowed."
        )

    print("Valid File.")

except InvalidFileError as error:

    print(error)

# ==========================================================
# PRODUCT PRICE
# ==========================================================

print("\n" + "=" * 70)
print("8. PRODUCT PRICE")
print("=" * 70)


class InvalidPriceError(Exception):

    pass


try:

    price = float(input("Enter Product Price : "))

    if price <= 0:

        raise InvalidPriceError(
            "Price must be greater than zero."
        )

    print("Price :", price)

except InvalidPriceError as error:

    print(error)

# ==========================================================
# USERNAME VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("9. USERNAME VALIDATION")
print("=" * 70)


class UsernameError(Exception):

    pass


try:

    username = input("Enter Username : ")

    if username.strip() == "":

        raise UsernameError(
            "Username cannot be empty."
        )

    print("Username Accepted.")

except UsernameError as error:

    print(error)

# ==========================================================
# MULTIPLE CUSTOM EXCEPTIONS
# ==========================================================

print("\n" + "=" * 70)
print("10. MULTIPLE CUSTOM EXCEPTIONS")
print("=" * 70)


class EmptyNameError(Exception):

    pass


class InvalidSalaryError(Exception):

    pass


try:

    name = input("Employee Name : ")
    salary = float(input("Salary : "))

    if name.strip() == "":

        raise EmptyNameError(
            "Name cannot be empty."
        )

    if salary <= 0:

        raise InvalidSalaryError(
            "Salary must be positive."
        )

    print("Employee Added Successfully.")

except EmptyNameError as error:

    print(error)

except InvalidSalaryError as error:

    print(error)

# ==========================================================
# CUSTOM EXCEPTION WITH __init__
# ==========================================================

print("\n" + "=" * 70)
print("11. CUSTOM MESSAGE")
print("=" * 70)


class VotingError(Exception):

    def __init__(self, age):

        self.age = age

        super().__init__(
            f"Age {age} is not eligible for voting."
        )


try:

    age = int(input("Enter Age : "))

    if age < 18:

        raise VotingError(age)

    print("Eligible to Vote.")

except VotingError as error:

    print(error)

# ==========================================================
# INHERITANCE CHECK
# ==========================================================

print("\n" + "=" * 70)
print("12. INHERITANCE CHECK")
print("=" * 70)

print(
    "Is InvalidAgeError a subclass of Exception ?",
    issubclass(InvalidAgeError, Exception)
)

print(
    "Is WeakPasswordError a subclass of Exception ?",
    issubclass(WeakPasswordError, Exception)
)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to inherit from Exception.")
print("❌ Using unclear exception names.")
print("❌ Raising custom exceptions unnecessarily.")
print("❌ Ignoring exception messages.")
print("❌ Not handling raised exceptions.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Inherit from Exception.")
print("✔ Give meaningful class names.")
print("✔ Write clear error messages.")
print("✔ Raise exceptions only when needed.")
print("✔ Handle custom exceptions properly.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Machine",

    "Online Banking",

    "Hospital Management",

    "Student Portal",

    "Login System",

    "Shopping Website",

    "Payment Gateway",

    "Employee Management"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Custom exceptions are user-defined.")
print("✔ They inherit from Exception.")
print("✔ Used for business rule validation.")
print("✔ Make code easier to understand.")
print("✔ Improve debugging.")
print("✔ Common in professional applications.")

print("=" * 70)
print("End of 05_custom_exception.py")
print("=" * 70)
# ==========================================================
#          Python raise Keyword - Day 14
# ==========================================================

print("=" * 70)
print("              PYTHON RAISE KEYWORD")
print("=" * 70)

# ==========================================================
# WHAT IS raise?
# ==========================================================

# The raise keyword is used to manually generate
# an exception.
#
# It is commonly used to validate data and stop
# the program when invalid conditions occur.

print("\nThe 'raise' keyword allows us to create exceptions manually.")

# ==========================================================
# WHY DO WE USE raise?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE raise?")
print("=" * 70)

print("1. Validate user input.")
print("2. Prevent invalid data.")
print("3. Stop incorrect program execution.")
print("4. Improve program reliability.")
print("5. Create meaningful error messages.")

# ==========================================================
# BASIC raise EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("1. BASIC raise")
print("=" * 70)

try:

    raise Exception("This is a manually raised exception.")

except Exception as error:

    print(error)

# ==========================================================
# VALUE ERROR
# ==========================================================

print("\n" + "=" * 70)
print("2. VALUE ERROR")
print("=" * 70)

try:

    age = int(input("Enter Your Age : "))

    if age < 0:

        raise ValueError("Age cannot be negative.")

    print("Age :", age)

except ValueError as error:

    print(error)

# ==========================================================
# ZERO DIVISION CHECK
# ==========================================================

print("\n" + "=" * 70)
print("3. DIVISION VALIDATION")
print("=" * 70)

try:

    number = int(input("Enter Number : "))

    if number == 0:

        raise ZeroDivisionError("Division by zero is not allowed.")

    print("100 /", number, "=", 100 / number)

except ZeroDivisionError as error:

    print(error)

# ==========================================================
# PASSWORD VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("4. PASSWORD VALIDATION")
print("=" * 70)

try:

    password = input("Create Password : ")

    if len(password) < 8:

        raise ValueError("Password must contain at least 8 characters.")

    print("Password Accepted.")

except ValueError as error:

    print(error)

# ==========================================================
# MARKS VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("5. MARKS VALIDATION")
print("=" * 70)

try:

    marks = int(input("Enter Marks : "))

    if marks < 0 or marks > 100:

        raise ValueError("Marks should be between 0 and 100.")

    print("Marks :", marks)

except ValueError as error:

    print(error)

# ==========================================================
# VOTING ELIGIBILITY
# ==========================================================

print("\n" + "=" * 70)
print("6. VOTING ELIGIBILITY")
print("=" * 70)

try:

    age = int(input("Enter Age : "))

    if age < 18:

        raise PermissionError("You are not eligible to vote.")

    print("You can vote.")

except PermissionError as error:

    print(error)

# ==========================================================
# ATM WITHDRAWAL
# ==========================================================

print("\n" + "=" * 70)
print("7. ATM WITHDRAWAL")
print("=" * 70)

balance = 5000

try:

    amount = int(input("Enter Withdrawal Amount : "))

    if amount > balance:

        raise ValueError("Insufficient Balance.")

    balance -= amount

    print("Remaining Balance :", balance)

except ValueError as error:

    print(error)

# ==========================================================
# FILE VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("8. FILE VALIDATION")
print("=" * 70)

filename = "Day13/data.txt"

try:

    if not filename.endswith(".txt"):

        raise TypeError("Only .txt files are allowed.")

    print("Valid File :", filename)

except TypeError as error:

    print(error)

# ==========================================================
# LOGIN VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("9. LOGIN VALIDATION")
print("=" * 70)

correct_username = "admin"

try:

    username = input("Username : ")

    if username != correct_username:

        raise ValueError("Invalid Username.")

    print("Login Successful.")

except ValueError as error:

    print(error)

# ==========================================================
# PRODUCT PRICE VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("10. PRODUCT PRICE")
print("=" * 70)

try:

    price = float(input("Enter Product Price : "))

    if price <= 0:

        raise ValueError("Price must be greater than zero.")

    print("Price :", price)

except ValueError as error:

    print(error)

# ==========================================================
# MULTIPLE VALIDATIONS
# ==========================================================

print("\n" + "=" * 70)
print("11. MULTIPLE VALIDATIONS")
print("=" * 70)

try:

    username = input("Username : ")
    password = input("Password : ")

    if username == "":

        raise ValueError("Username cannot be empty.")

    if password == "":

        raise ValueError("Password cannot be empty.")

    if len(password) < 8:

        raise ValueError("Password must contain at least 8 characters.")

    print("Login Details Accepted.")

except ValueError as error:

    print(error)

# ==========================================================
# raise WITHOUT MESSAGE
# ==========================================================

print("\n" + "=" * 70)
print("12. raise WITHOUT MESSAGE")
print("=" * 70)

try:

    raise RuntimeError

except RuntimeError:

    print("RuntimeError Raised Successfully.")

# ==========================================================
# COMMON EXCEPTIONS USED WITH raise
# ==========================================================

print("\n" + "=" * 70)
print("COMMON EXCEPTIONS")
print("=" * 70)

exceptions = [

    "ValueError",

    "TypeError",

    "RuntimeError",

    "PermissionError",

    "ZeroDivisionError",

    "FileNotFoundError",

    "KeyError",

    "IndexError"

]

for item in exceptions:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Raising the wrong exception type.")
print("❌ Forgetting to handle raised exceptions.")
print("❌ Using raise unnecessarily.")
print("❌ Poor error messages.")
print("❌ Validating data after using it.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Raise meaningful exceptions.")
print("✔ Validate input before processing.")
print("✔ Write clear error messages.")
print("✔ Catch only expected exceptions.")
print("✔ Use raise for business rules.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Machines",

    "Online Banking",

    "Student Management",

    "Hospital Systems",

    "Login Authentication",

    "E-Commerce Websites",

    "Payment Validation",

    "Age Verification"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ raise creates exceptions manually.")
print("✔ Used for input validation.")
print("✔ Prevents invalid program execution.")
print("✔ Can raise built-in exceptions.")
print("✔ Always provide meaningful messages.")
print("✔ Makes programs safer and more reliable.")

print("=" * 70)
print("End of 04_raise.py")
print("=" * 70)
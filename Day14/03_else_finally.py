# ==========================================================
#       Python else & finally Blocks - Day 14
# ==========================================================

print("=" * 70)
print("          PYTHON ELSE & FINALLY")
print("=" * 70)

# ==========================================================
# WHAT IS ELSE?
# ==========================================================

# The else block executes only if NO exception occurs
# inside the try block.

print("\nThe else block runs only when the try block succeeds.")

# ==========================================================
# WHAT IS FINALLY?
# ==========================================================

# The finally block always executes whether an
# exception occurs or not.

print("The finally block always executes.")

# ==========================================================
# WHY USE ELSE AND FINALLY?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE ELSE & FINALLY?")
print("=" * 70)

print("1. else executes when there is no exception.")
print("2. finally always executes.")
print("3. Useful for cleaning resources.")
print("4. Makes programs more reliable.")
print("5. Professional coding practice.")

# ==========================================================
# BASIC ELSE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("1. BASIC ELSE EXAMPLE")
print("=" * 70)

try:

    number = 100 / 5

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Division Successful :", number)

# ==========================================================
# ELSE WITH USER INPUT
# ==========================================================

print("\n" + "=" * 70)
print("2. ELSE WITH USER INPUT")
print("=" * 70)

try:

    age = int(input("Enter Your Age : "))

except ValueError:

    print("Please enter numbers only.")

else:

    print("Your Age :", age)

# ==========================================================
# BASIC FINALLY
# ==========================================================

print("\n" + "=" * 70)
print("3. BASIC FINALLY")
print("=" * 70)

try:

    number = 10 / 2

    print("Answer :", number)

except ZeroDivisionError:

    print("Division by zero.")

finally:

    print("Finally block executed.")

# ==========================================================
# FINALLY AFTER EXCEPTION
# ==========================================================

print("\n" + "=" * 70)
print("4. FINALLY AFTER EXCEPTION")
print("=" * 70)

try:

    result = 20 / 0

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("Program continues...")

# ==========================================================
# ELSE + FINALLY TOGETHER
# ==========================================================

print("\n" + "=" * 70)
print("5. ELSE + FINALLY")
print("=" * 70)

try:

    number = int(input("Enter Number : "))

    answer = 100 / number

except ValueError:

    print("Invalid Number.")

except ZeroDivisionError:

    print("Division by zero is not allowed.")

else:

    print("Answer :", answer)

finally:

    print("Calculation Finished.")

# ==========================================================
# FILE HANDLING EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("6. FILE HANDLING")
print("=" * 70)

try:

    file = open("Day13/data.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("File not found.")

else:

    print("File Read Successfully.")

finally:

    try:

        file.close()

        print("File Closed.")

    except NameError:

        print("No file to close.")

# ==========================================================
# LOGIN EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("7. LOGIN EXAMPLE")
print("=" * 70)

correct_password = "python123"

try:

    password = input("Enter Password : ")

    if password != correct_password:

        raise ValueError("Incorrect Password")

except ValueError as error:

    print(error)

else:

    print("Login Successful!")

finally:

    print("Login Attempt Completed.")

# ==========================================================
# CALCULATOR EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("8. CALCULATOR")
print("=" * 70)

try:

    first = float(input("First Number : "))
    second = float(input("Second Number : "))

    result = first / second

except ValueError:

    print("Enter valid numbers.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Result :", result)

finally:

    print("Calculator Closed.")

# ==========================================================
# MULTIPLE OPERATIONS
# ==========================================================

print("\n" + "=" * 70)
print("9. MULTIPLE OPERATIONS")
print("=" * 70)

try:

    numbers = [10, 20, 30]

    print(numbers[1])

except IndexError:

    print("Index Error.")

else:

    print("List accessed successfully.")

finally:

    print("List operation completed.")

# ==========================================================
# EXCEPTION OBJECT
# ==========================================================

print("\n" + "=" * 70)
print("10. EXCEPTION OBJECT")
print("=" * 70)

try:

    value = int("Python")

except ValueError as error:

    print("Error :", error)

else:

    print("Conversion Successful.")

finally:

    print("Conversion Finished.")

# ==========================================================
# ELSE vs FINALLY
# ==========================================================

print("\n" + "=" * 70)
print("11. ELSE vs FINALLY")
print("=" * 70)

print("ELSE")
print("✔ Executes only when NO exception occurs.")
print("✔ Optional block.")

print()

print("FINALLY")
print("✔ Always executes.")
print("✔ Used for cleanup tasks.")
print("✔ Optional block.")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Writing else without try.")
print("❌ Expecting finally to skip execution.")
print("❌ Forgetting resource cleanup.")
print("❌ Using finally for normal program logic.")
print("❌ Ignoring specific exceptions.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use else for successful execution.")
print("✔ Use finally to release resources.")
print("✔ Close files in finally (or use with).")
print("✔ Keep try blocks small.")
print("✔ Handle only expected exceptions.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Transactions",

    "Database Connections",

    "File Handling",

    "Online Banking",

    "Hospital Software",

    "Web Applications",

    "Game Development",

    "API Requests"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ else executes only if no exception occurs.")
print("✔ finally always executes.")
print("✔ finally is mainly used for cleanup.")
print("✔ else keeps success code separate.")
print("✔ Use both for cleaner and safer programs.")
print("✔ Makes applications more reliable.")

print("=" * 70)
print("End of 03_else_finally.py")
print("=" * 70)
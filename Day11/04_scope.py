# ==========================================================
#           Python Variable Scope - Day 11
# ==========================================================

print("=" * 70)
print("              PYTHON VARIABLE SCOPE")
print("=" * 70)

# ==========================================================
# WHAT IS VARIABLE SCOPE?
# ==========================================================

# Scope means the area where a variable can be accessed.
#
# There are mainly two types:
# 1. Local Variable
# 2. Global Variable

# ==========================================================
# EXAMPLE 1 - LOCAL VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("1. LOCAL VARIABLE")
print("=" * 70)

def student():

    name = "Bhomdev"      # Local Variable

    print("Inside Function :", name)

student()

# print(name)   # Error (Outside Function)

# ==========================================================
# EXAMPLE 2 - GLOBAL VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("2. GLOBAL VARIABLE")
print("=" * 70)

college = "ABC College"

def show_college():

    print("Inside Function :", college)

show_college()

print("Outside Function :", college)

# ==========================================================
# EXAMPLE 3 - LOCAL AND GLOBAL SAME NAME
# ==========================================================

print("\n" + "=" * 70)
print("3. LOCAL VS GLOBAL")
print("=" * 70)

city = "Delhi"

def location():

    city = "Patiala"

    print("Inside Function :", city)

location()

print("Outside Function :", city)

# ==========================================================
# EXAMPLE 4 - USING GLOBAL KEYWORD
# ==========================================================

print("\n" + "=" * 70)
print("4. global KEYWORD")
print("=" * 70)

count = 10

def increase():

    global count

    count += 5

    print("Inside Function :", count)

increase()

print("Outside Function :", count)

# ==========================================================
# EXAMPLE 5 - ACCESS GLOBAL VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("5. ACCESS GLOBAL VARIABLE")
print("=" * 70)

language = "Python"

def course():

    print("Learning", language)

course()

# ==========================================================
# EXAMPLE 6 - LOCAL VARIABLES IN DIFFERENT FUNCTIONS
# ==========================================================

print("\n" + "=" * 70)
print("6. DIFFERENT LOCAL VARIABLES")
print("=" * 70)

def student1():

    name = "Rahul"

    print(name)

def student2():

    name = "Aman"

    print(name)

student1()

student2()

# ==========================================================
# EXAMPLE 7 - GLOBAL VARIABLE IN MULTIPLE FUNCTIONS
# ==========================================================

print("\n" + "=" * 70)
print("7. GLOBAL IN MULTIPLE FUNCTIONS")
print("=" * 70)

company = "OpenAI"

def employee1():

    print(company)

def employee2():

    print(company)

employee1()

employee2()

# ==========================================================
# EXAMPLE 8 - LOCAL VARIABLE DOES NOT AFFECT GLOBAL
# ==========================================================

print("\n" + "=" * 70)
print("8. LOCAL DOES NOT CHANGE GLOBAL")
print("=" * 70)

marks = 80

def exam():

    marks = 95

    print("Inside :", marks)

exam()

print("Outside :", marks)

# ==========================================================
# EXAMPLE 9 - MODIFY GLOBAL VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("9. MODIFY GLOBAL VARIABLE")
print("=" * 70)

balance = 5000

def deposit():

    global balance

    balance += 2000

deposit()

print("Updated Balance :", balance)

# ==========================================================
# EXAMPLE 10 - SHOP EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("10. SHOP EXAMPLE")
print("=" * 70)

shop_name = "Bhomdev Store"

def bill():

    customer = "Rahul"

    amount = 2500

    print("Shop     :", shop_name)

    print("Customer :", customer)

    print("Amount   :", amount)

bill()

# ==========================================================
# EXAMPLE 11 - COUNTER
# ==========================================================

print("\n" + "=" * 70)
print("11. VISITOR COUNTER")
print("=" * 70)

visitors = 0

def new_visitor():

    global visitors

    visitors += 1

    print("Visitors :", visitors)

new_visitor()

new_visitor()

new_visitor()

# ==========================================================
# EXAMPLE 12 - NESTED FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("12. NESTED FUNCTION")
print("=" * 70)

def outer():

    message = "Hello"

    def inner():

        print(message)

    inner()

outer()

# ==========================================================
# EXAMPLE 13 - GLOBAL() FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("13. globals()")
print("=" * 70)

country = "India"

print(globals()["country"])

# ==========================================================
# EXAMPLE 14 - LOCAL VARIABLES
# ==========================================================

print("\n" + "=" * 70)
print("14. locals()")
print("=" * 70)

def information():

    name = "Bhomdev"

    age = 22

    print(locals())

information()

# ==========================================================
# EXAMPLE 15 - BEST PRACTICE
# ==========================================================

print("\n" + "=" * 70)
print("15. BEST PRACTICE")
print("=" * 70)

print("✔ Use local variables whenever possible.")
print("✔ Use global variables only when necessary.")
print("✔ Avoid modifying global variables frequently.")
print("✔ Keep functions independent and reusable.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Scope defines where a variable can be used.")
print("✔ Local variables exist only inside functions.")
print("✔ Global variables exist throughout the program.")
print("✔ global keyword modifies a global variable.")
print("✔ Local variables do not affect global variables.")
print("✔ globals() returns all global variables.")
print("✔ locals() returns local variables of a function.")
print("✔ Prefer local variables for better code quality.")

print("=" * 70)
print("End of scope.py")
print("=" * 70)
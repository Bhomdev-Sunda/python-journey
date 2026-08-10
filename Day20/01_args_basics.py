# ==========================================================
#              *args Basics - Day 20
# ==========================================================

"""
Day 20 - *args Basics

Topics Covered:
1. Positional arguments
2. Problem with fixed arguments
3. What is *args?
4. args is a tuple
5. Looping through args
6. Using built-in functions with args
7. Normal parameters with *args
8. Practical examples
9. Common mistakes
10. Interview questions
"""

print("=" * 70)
print("                 *args BASICS")
print("=" * 70)


# ==========================================================
# 1. NORMAL POSITIONAL ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("1. NORMAL POSITIONAL ARGUMENTS")
print("=" * 70)


def add(a, b):
    return a + b


print("Result:", add(10, 20))


# ==========================================================
# 2. PROBLEM WITH FIXED ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("2. PROBLEM WITH FIXED ARGUMENTS")
print("=" * 70)


def add_three(a, b, c):
    return a + b + c


print("Result:", add_three(10, 20, 30))

print("\nThe function above accepts exactly 3 arguments.")
print("If we want to add 4, 5, or 10 numbers,")
print("we would need to keep changing the function.")


# ==========================================================
# 3. WHAT IS *args?
# ==========================================================

print("\n" + "=" * 70)
print("3. WHAT IS *args?")
print("=" * 70)

"""
*args allows a function to accept
any number of positional arguments.

Inside the function, args is stored as a tuple.
"""


def add_numbers(*args):

    print("args:", args)

    print("Type:", type(args))


add_numbers(10, 20, 30, 40)


# ==========================================================
# 4. ADD MULTIPLE NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("4. ADD MULTIPLE NUMBERS")
print("=" * 70)


def total(*args):

    result = 0

    for number in args:

        result += number

    return result


print("Total:", total(10, 20))

print("Total:", total(10, 20, 30))

print("Total:", total(10, 20, 30, 40, 50))


# ==========================================================
# 5. LOOP THROUGH *args
# ==========================================================

print("\n" + "=" * 70)
print("5. LOOP THROUGH *args")
print("=" * 70)


def show_numbers(*args):

    for number in args:

        print("Number:", number)


show_numbers(5, 10, 15, 20, 25)


# ==========================================================
# 6. *args IS A TUPLE
# ==========================================================

print("\n" + "=" * 70)
print("6. *args IS A TUPLE")
print("=" * 70)


def check_args(*args):

    print("Value:", args)

    print("Type:", type(args))

    print("Length:", len(args))


check_args("Python", "Java", "C++")


# ==========================================================
# 7. ACCESSING VALUES USING INDEX
# ==========================================================

print("\n" + "=" * 70)
print("7. ACCESSING *args VALUES")
print("=" * 70)


def first_and_last(*args):

    if len(args) == 0:

        print("No arguments provided.")

        return

    print("First:", args[0])

    print("Last:", args[-1])


first_and_last(10, 20, 30, 40)


# ==========================================================
# 8. BUILT-IN FUNCTIONS WITH *args
# ==========================================================

print("\n" + "=" * 70)
print("8. BUILT-IN FUNCTIONS")
print("=" * 70)


def statistics(*numbers):

    if not numbers:

        print("No numbers provided.")

        return

    print("Numbers:", numbers)

    print("Minimum:", min(numbers))

    print("Maximum:", max(numbers))

    print("Sum:", sum(numbers))

    print("Count:", len(numbers))


statistics(10, 25, 5, 40, 15)


# ==========================================================
# 9. NORMAL PARAMETER + *args
# ==========================================================

print("\n" + "=" * 70)
print("9. NORMAL PARAMETER + *args")
print("=" * 70)


def introduce(name, *skills):

    print("Name:", name)

    print("Skills:")

    for skill in skills:

        print("-", skill)


introduce(
    "Bhomdev",
    "Python",
    "SQL",
    "FastAPI",
    "Machine Learning"
)


# ==========================================================
# 10. *args WITH CALCULATOR
# ==========================================================

print("\n" + "=" * 70)
print("10. CALCULATOR USING *args")
print("=" * 70)


def addition(*numbers):

    return sum(numbers)


print("Addition:", addition(10, 20, 30, 40))


# ==========================================================
# 11. MULTIPLICATION USING *args
# ==========================================================

print("\n" + "=" * 70)
print("11. MULTIPLICATION USING *args")
print("=" * 70)


def multiply(*numbers):

    result = 1

    for number in numbers:

        result *= number

    return result


print("Result:", multiply(2, 3, 4))

print("Result:", multiply(5, 10))


# ==========================================================
# 12. FIND AVERAGE USING *args
# ==========================================================

print("\n" + "=" * 70)
print("12. AVERAGE USING *args")
print("=" * 70)


def average(*numbers):

    if not numbers:

        return 0

    return sum(numbers) / len(numbers)


print("Average:", average(10, 20, 30, 40, 50))


# ==========================================================
# 13. FIND EVEN NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("13. FIND EVEN NUMBERS")
print("=" * 70)


def even_numbers(*numbers):

    result = []

    for number in numbers:

        if number % 2 == 0:

            result.append(number)

    return result


print(even_numbers(1, 2, 3, 4, 5, 6, 7, 8))


# ==========================================================
# 14. FIND ODD NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("14. FIND ODD NUMBERS")
print("=" * 70)


def odd_numbers(*numbers):

    result = []

    for number in numbers:

        if number % 2 != 0:

            result.append(number)

    return result


print(odd_numbers(1, 2, 3, 4, 5, 6, 7, 8))


# ==========================================================
# 15. *args WITH STRINGS
# ==========================================================

print("\n" + "=" * 70)
print("15. *args WITH STRINGS")
print("=" * 70)


def print_names(*names):

    for name in names:

        print("Name:", name)


print_names(
    "Bhomdev",
    "Rahul",
    "Amit",
    "Priya"
)


# ==========================================================
# 16. JOIN STRINGS
# ==========================================================

print("\n" + "=" * 70)
print("16. JOIN STRINGS")
print("=" * 70)


def join_words(*words):

    return " ".join(words)


sentence = join_words(
    "Python",
    "is",
    "easy",
    "to",
    "learn"
)

print(sentence)


# ==========================================================
# 17. *args WITH CONDITIONS
# ==========================================================

print("\n" + "=" * 70)
print("17. *args WITH CONDITIONS")
print("=" * 70)


def check_numbers(*numbers):

    for number in numbers:

        if number > 50:

            print(number, "is greater than 50.")

        else:

            print(number, "is 50 or less.")


check_numbers(20, 60, 45, 90)


# ==========================================================
# 18. PASSING A LIST TO *args
# ==========================================================

print("\n" + "=" * 70)
print("18. PASSING A LIST")
print("=" * 70)


numbers = [10, 20, 30, 40]

print("Without unpacking:")


def display(*args):

    print(args)


display(numbers)

print("\nWith unpacking:")

display(*numbers)


# ==========================================================
# 19. *args AND FUNCTION REUSABILITY
# ==========================================================

print("\n" + "=" * 70)
print("19. FUNCTION REUSABILITY")
print("=" * 70)


def calculate_total(*prices):

    return sum(prices)


print("Cart 1:", calculate_total(100, 200))

print("Cart 2:", calculate_total(100, 200, 300, 400))

print("Cart 3:", calculate_total(50, 75, 125, 250, 500))


# ==========================================================
# 20. REAL-LIFE APPLICATION
# ==========================================================

print("\n" + "=" * 70)
print("20. REAL-LIFE APPLICATION")
print("=" * 70)


def shopping_cart(*prices):

    total_price = sum(prices)

    print("Items:", len(prices))

    print("Total Price:", total_price)


shopping_cart(499, 799, 299, 999)


# ==========================================================
# IMPORTANT RULE
# ==========================================================

print("\n" + "=" * 70)
print("IMPORTANT RULE")
print("=" * 70)

print("""
*args collects EXTRA POSITIONAL arguments.

Example:

def function(a, b, *args):
    pass

a -> first positional argument
b -> second positional argument
args -> remaining positional arguments
""")


# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Thinking args is a list.")
print("❌ Forgetting that args is a tuple.")
print("❌ Using *args when fixed arguments are enough.")
print("❌ Confusing *args with unpacking.")
print("❌ Forgetting that *args handles positional arguments.")


# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use *args when the number of positional arguments is unknown.")
print("✔ Remember that args is a tuple.")
print("✔ Give meaningful names to normal parameters.")
print("✔ Don't use *args unnecessarily.")
print("✔ Use *args with flexible utility functions.")


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)


questions = [

    "What is *args?",

    "What type of object is args?",

    "Why do we use *args?",

    "Can *args accept zero arguments?",

    "Can normal parameters be used with *args?",

    "What is the difference between *args and unpacking?",

    "Can we modify args directly?",

    "When should *args be used?"

]


for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")


# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ *args accepts variable positional arguments.")

print("✔ args is stored as a tuple.")

print("✔ *args can accept zero or many arguments.")

print("✔ Normal parameters can come before *args.")

print("✔ *args is useful for flexible functions.")

print("✔ *args can also be used for argument unpacking.")

print("✔ *args is commonly used in decorators.")


print("\n" + "=" * 70)
print("       End of 01_args_basics.py")
print("=" * 70)
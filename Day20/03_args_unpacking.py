# ==========================================================
#             *args Unpacking - Day 20
# ==========================================================

"""
Day 20 - *args Unpacking

Topics Covered:
1. What is unpacking?
2. * with lists
3. * with tuples
4. * with sets
5. Unpacking into function arguments
6. Unpacking with normal arguments
7. Combining multiple iterables
8. Star unpacking in assignments
9. Nested unpacking
10. Practical examples
11. Difference between *args and * unpacking
12. Common mistakes
13. Interview questions
"""

print("=" * 70)
print("                 *args UNPACKING")
print("=" * 70)


# ==========================================================
# 1. WHAT IS UNPACKING?
# ==========================================================

print("\n" + "=" * 70)
print("1. WHAT IS UNPACKING?")
print("=" * 70)

"""
Unpacking means taking elements from an iterable
and passing them individually.

The * operator is used for positional unpacking.
"""

numbers = [10, 20, 30]

print("List:", numbers)

print("Unpacked values:", *numbers)


# ==========================================================
# 2. LIST UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("2. LIST UNPACKING")
print("=" * 70)


numbers = [10, 20, 30, 40]

print("Original list:", numbers)

print("Values:")

print(*numbers)


# ==========================================================
# 3. TUPLE UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("3. TUPLE UNPACKING")
print("=" * 70)


numbers = (100, 200, 300)

print("Original tuple:", numbers)

print("Unpacked values:")

print(*numbers)


# ==========================================================
# 4. SET UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("4. SET UNPACKING")
print("=" * 70)


numbers = {1, 2, 3, 4}

print("Original set:", numbers)

print("Unpacked values:")

print(*numbers)


# ==========================================================
# 5. PASS LIST TO FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("5. PASS LIST TO FUNCTION")
print("=" * 70)


def add(a, b, c):

    return a + b + c


numbers = [10, 20, 30]

print("List:", numbers)

print("Result:", add(*numbers))


# ==========================================================
# 6. WITHOUT UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("6. WITHOUT UNPACKING")
print("=" * 70)


def display(a, b, c):

    print("a:", a)

    print("b:", b)

    print("c:", c)


numbers = [10, 20, 30]

print("Using unpacking:")

display(*numbers)


# ==========================================================
# 7. FUNCTION WITH *args
# ==========================================================

print("\n" + "=" * 70)
print("7. FUNCTION WITH *args")
print("=" * 70)


def show_numbers(*args):

    print("args:", args)


numbers = [10, 20, 30, 40]

show_numbers(*numbers)


# ==========================================================
# 8. COLLECTING vs UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("8. COLLECTING vs UNPACKING")
print("=" * 70)


def collect(*args):

    print("Collected:", args)


numbers = [10, 20, 30]

print("Using *args to collect:")

collect(10, 20, 30)

print("\nUsing * to unpack:")

collect(*numbers)


# ==========================================================
# 9. UNPACKING WITH NORMAL ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("9. UNPACKING WITH NORMAL ARGUMENTS")
print("=" * 70)


def introduce(name, age, city):

    print("Name:", name)

    print("Age:", age)

    print("City:", city)


data = ["Bhomdev", 22, "Punjab"]

introduce(*data)


# ==========================================================
# 10. MULTIPLE ITERABLES
# ==========================================================

print("\n" + "=" * 70)
print("10. MULTIPLE ITERABLES")
print("=" * 70)


first = [1, 2, 3]

second = [4, 5, 6]

combined = [*first, *second]

print("First:", first)

print("Second:", second)

print("Combined:", combined)


# ==========================================================
# 11. COMBINE TUPLES
# ==========================================================

print("\n" + "=" * 70)
print("11. COMBINE TUPLES")
print("=" * 70)


first = (10, 20)

second = (30, 40)

combined = (*first, *second)

print("First:", first)

print("Second:", second)

print("Combined:", combined)


# ==========================================================
# 12. COMBINE SETS
# ==========================================================

print("\n" + "=" * 70)
print("12. COMBINE SETS")
print("=" * 70)


first = {1, 2, 3}

second = {3, 4, 5}

combined = {*first, *second}

print("First:", first)

print("Second:", second)

print("Combined:", combined)


# ==========================================================
# 13. STAR UNPACKING IN LISTS
# ==========================================================

print("\n" + "=" * 70)
print("13. STAR UNPACKING IN LISTS")
print("=" * 70)


numbers = [1, 2, 3]

new_numbers = [0, *numbers, 4, 5]

print("Original:", numbers)

print("New list:", new_numbers)


# ==========================================================
# 14. STAR UNPACKING IN TUPLES
# ==========================================================

print("\n" + "=" * 70)
print("14. STAR UNPACKING IN TUPLES")
print("=" * 70)


numbers = (2, 3, 4)

new_numbers = (1, *numbers, 5)

print("Original:", numbers)

print("New tuple:", new_numbers)


# ==========================================================
# 15. STAR UNPACKING IN FUNCTION CALLS
# ==========================================================

print("\n" + "=" * 70)
print("15. STAR UNPACKING IN FUNCTION CALLS")
print("=" * 70)


def multiply(a, b, c):

    return a * b * c


numbers = [2, 3, 4]

result = multiply(*numbers)

print("Numbers:", numbers)

print("Result:", result)


# ==========================================================
# 16. FIRST AND REST UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("16. FIRST AND REST UNPACKING")
print("=" * 70)


numbers = [10, 20, 30, 40, 50]

first, *rest = numbers

print("First:", first)

print("Rest:", rest)


# ==========================================================
# 17. REST AND LAST UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("17. REST AND LAST UNPACKING")
print("=" * 70)


numbers = [10, 20, 30, 40, 50]

*rest, last = numbers

print("Rest:", rest)

print("Last:", last)


# ==========================================================
# 18. FIRST, MIDDLE AND LAST
# ==========================================================

print("\n" + "=" * 70)
print("18. FIRST, MIDDLE AND LAST")
print("=" * 70)


numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First:", first)

print("Middle:", middle)

print("Last:", last)


# ==========================================================
# 19. STRING UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("19. STRING UNPACKING")
print("=" * 70)


name = "Python"

letters = [*name]

print("String:", name)

print("Letters:", letters)


# ==========================================================
# 20. STRING FUNCTION ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("20. STRING FUNCTION ARGUMENTS")
print("=" * 70)


def show_letters(a, b, c, d, e, f):

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)


word = "Python"

show_letters(*word)


# ==========================================================
# 21. RANGE UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("21. RANGE UNPACKING")
print("=" * 70)


numbers = range(1, 6)

print("Range values:")

print(*numbers)


# ==========================================================
# 22. RANGE WITH FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("22. RANGE WITH FUNCTION")
print("=" * 70)


def calculate(a, b, c, d, e):

    return a + b + c + d + e


numbers = range(1, 6)

print("Result:", calculate(*numbers))


# ==========================================================
# 23. PRACTICAL STUDENT EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("23. PRACTICAL STUDENT EXAMPLE")
print("=" * 70)


def student(name, age, course, city):

    print("Name:", name)

    print("Age:", age)

    print("Course:", course)

    print("City:", city)


student_data = [
    "Bhomdev",
    22,
    "BCA",
    "Punjab"
]

student(*student_data)


# ==========================================================
# 24. PRACTICAL SHOPPING EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("24. PRACTICAL SHOPPING EXAMPLE")
print("=" * 70)


def calculate_total(*prices):

    return sum(prices)


prices = [499, 799, 299, 999]

total = calculate_total(*prices)

print("Prices:", prices)

print("Total:", total)


# ==========================================================
# 25. PRACTICAL API EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("25. PRACTICAL API EXAMPLE")
print("=" * 70)


def request_data(method, endpoint, timeout):

    print("Method:", method)

    print("Endpoint:", endpoint)

    print("Timeout:", timeout)


request = [
    "GET",
    "/users",
    30
]

request_data(*request)


# ==========================================================
# 26. NESTED UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("26. NESTED UNPACKING")
print("=" * 70)


data = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flattened = [
    *data[0],
    *data[1],
    *data[2]
]

print("Original:", data)

print("Flattened:", flattened)


# ==========================================================
# 27. COPYING A LIST USING *
# ==========================================================

print("\n" + "=" * 70)
print("27. COPYING A LIST")
print("=" * 70)


original = [10, 20, 30]

copy = [*original]

print("Original:", original)

print("Copy:", copy)

print("Same object:", original is copy)


# ==========================================================
# 28. ADD ELEMENTS WHILE UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("28. ADD ELEMENTS WHILE UNPACKING")
print("=" * 70)


numbers = [20, 30, 40]

result = [10, *numbers, 50]

print("Original:", numbers)

print("Result:", result)


# ==========================================================
# 29. IMPORTANT DIFFERENCE
# ==========================================================

print("\n" + "=" * 70)
print("29. IMPORTANT DIFFERENCE")
print("=" * 70)

print("""
*args:

def function(*args):
    pass

Here *args COLLECTS positional arguments.

Example:
function(10, 20, 30)

args = (10, 20, 30)


* Unpacking:

numbers = [10, 20, 30]

function(*numbers)

Here * UNPACKS the iterable.

It becomes:

function(10, 20, 30)
""")


# ==========================================================
# 30. COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("30. COMMON MISTAKES")
print("=" * 70)

print("❌ Confusing *args with * unpacking.")

print("❌ Trying to unpack a non-iterable object.")

print("❌ Passing the wrong number of values to a function.")

print("❌ Forgetting that * performs positional unpacking.")

print("❌ Using * on a dictionary when ** is required.")


# ==========================================================
# 31. BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("31. BEST PRACTICES")
print("=" * 70)

print("✔ Use * when unpacking positional arguments.")

print("✔ Use ** when unpacking keyword arguments.")

print("✔ Make sure the number of unpacked values matches the function.")

print("✔ Use star unpacking to combine iterables cleanly.")

print("✔ Use starred assignment when you need the remaining values.")


# ==========================================================
# 32. INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("32. INTERVIEW QUESTIONS")
print("=" * 70)


questions = [

    "What is argument unpacking?",

    "What does * do in a function call?",

    "What is the difference between *args and * unpacking?",

    "Can a list be unpacked using *?",

    "Can a tuple be unpacked using *?",

    "Can a string be unpacked using *?",

    "What is starred assignment?",

    "What does first, *rest = values mean?",

    "What does *rest, last = values mean?",

    "What is the difference between * and **?"

]


for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")


# ==========================================================
# 33. SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("33. SUMMARY")
print("=" * 70)

print("✔ * is used for positional unpacking.")

print("✔ Lists, tuples, sets, strings and ranges can be unpacked.")

print("✔ *args collects positional arguments.")

print("✔ *numbers expands an iterable into separate values.")

print("✔ Starred assignment can capture remaining values.")

print("✔ * can combine multiple iterables.")

print("✔ ** is used for dictionary/keyword unpacking.")


print("\n" + "=" * 70)
print("       End of 03_args_unpacking.py")
print("=" * 70)
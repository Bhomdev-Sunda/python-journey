#        Python Dictionary Comprehension 

print("=" * 65)
print("         PYTHON DICTIONARY COMPREHENSION")
print("=" * 65)

# ==========================================================
# WHAT IS DICTIONARY COMPREHENSION?
# ==========================================================

# Dictionary comprehension is a short and clean way
# to create dictionaries using a single line of code.

# Syntax:
# {key: value for item in iterable}

# ==========================================================
# EXAMPLE 1 - SQUARE OF NUMBERS
# ==========================================================

print("\n1. Square Dictionary")

square = {num: num ** 2 for num in range(1, 6)}

print(square)

# ==========================================================
# EXAMPLE 2 - CUBE OF NUMBERS
# ==========================================================

print("\n2. Cube Dictionary")

cube = {num: num ** 3 for num in range(1, 6)}

print(cube)

# ==========================================================
# EXAMPLE 3 - NUMBER : EVEN / ODD
# ==========================================================

print("\n3. Even or Odd Dictionary")

numbers = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in range(1, 11)
}

print(numbers)

# ==========================================================
# EXAMPLE 4 - WORD LENGTH
# ==========================================================

print("\n4. Word Length")

words = ["Python", "Java", "SQL", "HTML", "CSS"]

length = {word: len(word) for word in words}

print(length)

# ==========================================================
# EXAMPLE 5 - STUDENT MARKS
# ==========================================================

print("\n5. Student Marks")

students = ["Rahul", "Aman", "Bhomdev", "Priya"]

marks = {student: 80 for student in students}

print(marks)

# ==========================================================
# EXAMPLE 6 - MULTIPLICATION TABLE
# ==========================================================

print("\n6. Table of 5")

table = {num: 5 * num for num in range(1, 11)}

print(table)

# ==========================================================
# EXAMPLE 7 - CONVERT LIST TO DICTIONARY
# ==========================================================

print("\n7. Convert List to Dictionary")

fruits = ["Apple", "Banana", "Mango"]

fruit_dict = {fruit: len(fruit) for fruit in fruits}

print(fruit_dict)

# ==========================================================
# EXAMPLE 8 - FILTER EVEN NUMBERS
# ==========================================================

print("\n8. Even Numbers Only")

even = {
    num: num
    for num in range(1, 21)
    if num % 2 == 0
}

print(even)

# ==========================================================
# EXAMPLE 9 - FILTER ODD NUMBERS
# ==========================================================

print("\n9. Odd Numbers Only")

odd = {
    num: num
    for num in range(1, 21)
    if num % 2 != 0
}

print(odd)

# ==========================================================
# EXAMPLE 10 - UPPERCASE WORDS
# ==========================================================

print("\n10. Uppercase Words")

languages = ["python", "java", "c++", "sql"]

upper = {
    lang: lang.upper()
    for lang in languages
}

print(upper)

# ==========================================================
# EXAMPLE 11 - LOWERCASE WORDS
# ==========================================================

print("\n11. Lowercase Words")

names = ["RAHUL", "AMAN", "BHOMDEV", "PRIYA"]

lower = {
    name: name.lower()
    for name in names
}

print(lower)

# ==========================================================
# EXAMPLE 12 - PRICE WITH GST
# ==========================================================

print("\n12. Product Price With GST")

products = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500
}

gst_price = {
    item: price * 1.18
    for item, price in products.items()
}

print(gst_price)

# ==========================================================
# EXAMPLE 13 - DISCOUNT PRICE
# ==========================================================

print("\n13. Discount Price")

discount = {
    item: price * 0.90
    for item, price in products.items()
}

print(discount)

# ==========================================================
# EXAMPLE 14 - CHARACTER FREQUENCY
# ==========================================================

print("\n14. Character Frequency")

text = "python"

frequency = {
    char: text.count(char)
    for char in text
}

print(frequency)

# ==========================================================
# EXAMPLE 15 - SQUARE ROOT STYLE DATA
# ==========================================================

print("\n15. Number and Square")

result = {
    num: {
        "Square": num ** 2,
        "Cube": num ** 3
    }
    for num in range(1, 6)
}

print(result)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)

print("✔ Dictionary comprehension creates dictionaries quickly.")
print("✔ Uses a single line of code.")
print("✔ Can use conditions.")
print("✔ Can use if-else expressions.")
print("✔ Can iterate through lists, ranges and dictionaries.")
print("✔ Makes code cleaner and more readable.")

print("=" * 65)
print("End of dictionary_comprehension.py")
print("=" * 65)
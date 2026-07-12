# Creating Strings in Python
print("========== CREATING STRINGS ==========\n")

# 1. Using Single Quotes
name = 'Bhomdev'
print("Single Quotes :", name)

# 2. Using Double Quotes
city = "Patiala"
print("Double Quotes :", city)

# 3. Using Triple Single Quotes
message1 = '''Welcome to
Python Programming'''
print("\nTriple Single Quotes")
print(message1)

# 4. Using Triple Double Quotes
message2 = """Learning Python
is fun."""
print("\nTriple Double Quotes")
print(message2)

# 5. Empty String
empty = ""
print("\nEmpty String")
print(empty)

# 6. String with Numbers
number = "12345"
print("\nString with Numbers")
print(number)

# 7. String with Special Characters
symbols = "@#$%^&*!"
print("\nSpecial Characters")
print(symbols)

# 8. String with Spaces
sentence = "Python is easy to learn."
print("\nSentence")
print(sentence)

# 9. Multi-line String
paragraph = """
Python is one of the most
popular programming languages.

It is easy to learn,
powerful,
and widely used.
"""
print("\nMulti-line String")
print(paragraph)

# 10. Escape Characters
print("Escape Characters")
print("Hello\nWorld")
print("Python\tProgramming")
print("He said, \"Welcome!\"")
print('It\'s a beautiful day.')
print("C:\\Users\\Bhomdev")

# 11. String using str()
age = 22
age_string = str(age)
print("\nUsing str()")
print(age_string)
print(type(age_string))

# 12. User Input (Always Returns String)
user_name = input("\nEnter your name: ")
print("Hello,", user_name)

# 13. String Concatenation
first_name = "Bhom"
last_name = "Dev"
full_name = first_name + " " + last_name
print("\nConcatenation")
print(full_name)

# 14. String Repetition
print("\nString Repetition")
print("=" * 40)
print("*" * 20)

# 15. f-Strings
course = "Python"
print("\nf-String")
print(f"My name is {user_name}.")
print(f"I am learning {course}.")
print(f"My age is {age}.")

print("\n========== END ==========")
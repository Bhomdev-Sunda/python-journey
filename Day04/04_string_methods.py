# String Methods in Python
print("========== STRING METHODS ==========\n")
text = "  Python Programming  "
print("Original String :", text)

# case conversion methods
print("\nCase Conversion")
print("upper()      :", text.upper())
print("lower()      :", text.lower())
print("title()      :", text.title())
print("capitalize() :", text.capitalize())
print("swapcase()   :", text.swapcase())

# remove spaces
print("\nRemoving Spaces")
print("strip()      :", text.strip())
print("lstrip()     :", text.lstrip())
print("rstrip()     :", text.rstrip())

# searching methods
sentence = "Python Programming"
print("\nSearching")
print("find('Pro')      :", sentence.find("Pro"))
print("find('Java')     :", sentence.find("Java"))
print("index('Python')  :", sentence.index("Python"))
print("count('m')       :", sentence.count("m"))

# replace method
print("\nReplace")
print(sentence.replace("Python", "Java"))

# startswith() and endswith()
print("\nStartswith / Endswith")
print(sentence.startswith("Python"))
print(sentence.endswith("Programming"))

# split()
print("\nSplit")
words = sentence.split()
print(words)

# join()
print("\nJoin")
language = ["Python", "Java", "C++"]
print(", ".join(language))
print(" - ".join(language))

# checking methods
print("\nChecking Methods")
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print("Python Programming".istitle())
print(" ".isspace())

# length
print("\nLength")
print(len(sentence))

# user input example
name = input("\nEnter your name : ")
print("\nUpper Case :", name.upper())
print("Lower Case :", name.lower())
print("Title Case :", name.title())
print("Length     :", len(name))
print("\n========== END ==========")
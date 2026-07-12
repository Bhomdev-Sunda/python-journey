# String Indexing in Python
print("========== STRING INDEXING ==========\n")

# Creating a String
text = "Python"
print("String :", text)

# Positive Indexing
print("\nPositive Indexing")
print("text[0] =", text[0])
print("text[1] =", text[1])
print("text[2] =", text[2])
print("text[3] =", text[3])
print("text[4] =", text[4])
print("text[5] =", text[5])

# Negative Indexing
print("\nNegative Indexing")
print("text[-1] =", text[-1])
print("text[-2] =", text[-2])
print("text[-3] =", text[-3])
print("text[-4] =", text[-4])
print("text[-5] =", text[-5])
print("text[-6] =", text[-6])

# Accessing First Character
print("\nFirst Character")
print(text[0])

# Accessing Last Character
print("\nLast Character")
print(text[-1])

# User Input Example
name = input("\nEnter your name: ")
print("First Character :", name[0])
print("Last Character  :", name[-1])

# Indexing with Numbers
number = "123456789"
print("\nString :", number)
print("First Digit :", number[0])
print("Last Digit  :", number[-1])

# IndexError Example
print("\nIndexError Example")
word = "Cat"
print("word =", word)
print("word[0] =", word[0])
print("word[1] =", word[1])
print("word[2] =", word[2])
# Uncomment the line below to see IndexError
# print(word[3])

# Length of String
print("\nLength of String")
print("Length of text :", len(text))
print("Length of word :", len(word))
print("Length of name :", len(name))
print("\n========== END ==========")
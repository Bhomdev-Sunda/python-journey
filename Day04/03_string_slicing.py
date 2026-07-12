# String Slicing in Python
print("========== STRING SLICING ==========\n")

# Creating a String
text = "Python Programming"
print("Original String :", text)

# Basic Slicing
print("\nBasic Slicing")
print("text[0:6]   =", text[0:6])
print("text[7:18]  =", text[7:18])
print("text[0:10]  =", text[0:10])

# Omitting Start Index
print("\nOmitting Start Index")
print("text[:6]    =", text[:6])
print("text[:10]   =", text[:10])

# Omitting End Index
print("\nOmitting End Index")
print("text[7:]    =", text[7:])
print("text[10:]   =", text[10:])

# Entire String
print("\nEntire String")
print("text[:]     =", text[:])

# Negative Slicing
print("\nNegative Slicing")
print("text[-11:]  =", text[-11:])
print("text[:-12]  =", text[:-12])
print("text[-18:-12] =", text[-18:-12])

# Step Value
print("\nStep Value")
print("text[::2]   =", text[::2])
print("text[::3]   =", text[::3])
print("text[1::2]  =", text[1::2])

# Reverse String
print("\nReverse String")
print("text[::-1]  =", text[::-1])

# Reverse with Step
print("\nReverse with Step")
print("text[::-2]  =", text[::-2])

# User Input Example
name = input("\nEnter your name: ")
print("\nFirst 3 Characters :", name[:3])
print("Last 3 Characters  :", name[-3:])
print("Without First Char :", name[1:])
print("Without Last Char  :", name[:-1])
print("Reverse Name       :", name[::-1])

# Length of String
print("\nLength of String")
print("Length =", len(text))

print("\n========== END ==========")
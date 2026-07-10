# Type Conversion

# "100" -> integer
value1 = "100"
print("Before:", value1, type(value1))
value1 = int(value1)
print("After :", value1, type(value1))

print()

# 50 -> string
value2 = 50
print("Before:", value2, type(value2))
value2 = str(value2)
print("After :", value2, type(value2))

print()

# "25.5" -> float
value3 = "25.5"
print("Before:", value3, type(value3))
value3 = float(value3)
print("After :", value3, type(value3))

print()

# 1 -> bool
value4 = 1
print("Before:", value4, type(value4))
value4 = bool(value4)
print("After :", value4, type(value4))
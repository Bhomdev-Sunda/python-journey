# ============================================
# Identity Operators Practice
# ============================================

print("========== IDENTITY OPERATORS ==========\n")

# Variables
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]
e = c

# is Operator
print("Using 'is' Operator\n")

print("a is b :", a is b)
print("c is d :", c is d)
print("c is e :", c is e)

print("\n------------------------------\n")

# is not Operator
print("Using 'is not' Operator\n")

print("a is not b :", a is not b)
print("c is not d :", c is not d)
print("c is not e :", c is not e)

print("\n------------------------------\n")

# Value Comparison vs Identity Comparison
print("Value Comparison (==)")
print("c == d :", c == d)
print("c == e :", c == e)

print("\nIdentity Comparison (is)")
print("c is d :", c is d)
print("c is e :", c is e)

print("\n------------------------------\n")

# Memory Addresses
print("Memory Addresses")

print("id(a) =", id(a))
print("id(b) =", id(b))
print("id(c) =", id(c))
print("id(d) =", id(d))
print("id(e) =", id(e))
# ============================================
# Operator Precedence Practice
# ============================================

print("========== OPERATOR PRECEDENCE ==========\n")

# Example 1: Multiplication before Addition
result1 = 10 + 5 * 2
print("10 + 5 * 2 =", result1)

# Example 2: Parentheses have Higher Precedence
result2 = (10 + 5) * 2
print("(10 + 5) * 2 =", result2)

# Example 3: Division before Addition
result3 = 20 + 10 / 2
print("20 + 10 / 2 =", result3)

# Example 4: Parentheses First
result4 = (20 + 10) / 2
print("(20 + 10) / 2 =", result4)

# Example 5: Exponent before Multiplication
result5 = 2 + 3 * 2 ** 3
print("2 + 3 * 2 ** 3 =", result5)

# Example 6: Parentheses + Exponent
result6 = (2 + 3) * 2 ** 3
print("(2 + 3) * 2 ** 3 =", result6)

# Example 7: Modulus
result7 = 15 + 10 % 4
print("15 + 10 % 4 =", result7)

# Example 8: Comparison Operators
result8 = 10 + 5 > 12
print("10 + 5 > 12 =", result8)

# Example 9: Logical Operators
result9 = 10 > 5 and 8 < 10
print("10 > 5 and 8 < 10 =", result9)

# Example 10: not Operator
result10 = not (10 > 5)
print("not (10 > 5) =", result10)

print("\n========== END ==========")
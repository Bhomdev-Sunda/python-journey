# Logical Operators Practice

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nLogical Operator Results")

# AND Operator
print("\nAND Operator")
print("num1 > 0 and num2 > 0 :", num1 > 0 and num2 > 0)

# OR Operator
print("\nOR Operator")
print("num1 > 0 or num2 > 0 :", num1 > 0 or num2 > 0)

# NOT Operator
print("\nNOT Operator")
print("not(num1 > num2) :", not (num1 > num2))
print("not(num1 < num2) :", not (num1 < num2))


# ============================================
# Logical Operators & Membership Operators
# ============================================

# ---------- User Input ----------
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

print("\n========== LOGICAL OPERATORS ==========\n")

# AND Operator
print("Eligible for Loan (Age >= 21 AND Salary >= 30000)")
print(age >= 21 and salary >= 30000)

# OR Operator
print("\nEligible for Vote (Age >= 18 OR Special Permission)")
# Assuming no special permission
special_permission = False
print(age >= 18 or special_permission)

# NOT Operator
print("\nEligible for Student Discount (NOT Age >= 60)")
print(not (age >= 60))

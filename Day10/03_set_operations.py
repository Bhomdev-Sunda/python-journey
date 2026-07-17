#           Python Set Operations 
print("=" * 70)
print("              PYTHON SET OPERATIONS")
print("=" * 70)

# ==========================================================
# SAMPLE SETS
# ==========================================================

set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print("\nSet 1 :", set1)
print("Set 2 :", set2)

# ==========================================================
# UNION
# ==========================================================

print("\n" + "=" * 70)
print("1. UNION")
print("=" * 70)

# Combines all unique elements

union_set = set1.union(set2)

print("Union :", union_set)

# Using | operator

print("Using | Operator")

print(set1 | set2)

# ==========================================================
# INTERSECTION
# ==========================================================

print("\n" + "=" * 70)
print("2. INTERSECTION")
print("=" * 70)

# Common elements

intersection_set = set1.intersection(set2)

print("Intersection :", intersection_set)

# Using & operator

print("Using & Operator")

print(set1 & set2)

# ==========================================================
# DIFFERENCE
# ==========================================================

print("\n" + "=" * 70)
print("3. DIFFERENCE")
print("=" * 70)

print("Set1 - Set2")

difference1 = set1.difference(set2)

print(difference1)

print("\nSet2 - Set1")

difference2 = set2.difference(set1)

print(difference2)

# Using - operator

print("\nUsing - Operator")

print(set1 - set2)

# ==========================================================
# SYMMETRIC DIFFERENCE
# ==========================================================

print("\n" + "=" * 70)
print("4. SYMMETRIC DIFFERENCE")
print("=" * 70)

# Elements present in either set but not both

sym_diff = set1.symmetric_difference(set2)

print(sym_diff)

# Using ^ operator

print("\nUsing ^ Operator")

print(set1 ^ set2)

# ==========================================================
# issubset()
# ==========================================================

print("\n" + "=" * 70)
print("5. issubset()")
print("=" * 70)

A = {1, 2}

B = {1, 2, 3, 4, 5}

print("A :", A)
print("B :", B)

print("\nIs A subset of B?")

print(A.issubset(B))

print("\nIs B subset of A?")

print(B.issubset(A))

# ==========================================================
# issuperset()
# ==========================================================

print("\n" + "=" * 70)
print("6. issuperset()")
print("=" * 70)

print("Is B superset of A?")

print(B.issuperset(A))

print("Is A superset of B?")

print(A.issuperset(B))

# ==========================================================
# isdisjoint()
# ==========================================================

print("\n" + "=" * 70)
print("7. isdisjoint()")
print("=" * 70)

x = {1, 2, 3}

y = {4, 5, 6}

z = {3, 4, 5}

print("X :", x)
print("Y :", y)
print("Z :", z)

print("\nX and Y are disjoint")

print(x.isdisjoint(y))

print("\nX and Z are disjoint")

print(x.isdisjoint(z))

# ==========================================================
# intersection_update()
# ==========================================================

print("\n" + "=" * 70)
print("8. intersection_update()")
print("=" * 70)

a = {1, 2, 3, 4}

b = {3, 4, 5, 6}

print("Before")

print("A :", a)

a.intersection_update(b)

print("\nAfter")

print("A :", a)

# ==========================================================
# difference_update()
# ==========================================================

print("\n" + "=" * 70)
print("9. difference_update()")
print("=" * 70)

a = {1, 2, 3, 4}

b = {3, 4, 5, 6}

print("Before")

print("A :", a)

a.difference_update(b)

print("\nAfter")

print("A :", a)

# ==========================================================
# symmetric_difference_update()
# ==========================================================

print("\n" + "=" * 70)
print("10. symmetric_difference_update()")
print("=" * 70)

a = {1, 2, 3}

b = {3, 4, 5}

print("Before")

print("A :", a)

a.symmetric_difference_update(b)

print("\nAfter")

print("A :", a)

# ==========================================================
# REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("11. STUDENT SPORTS CLUB")
print("=" * 70)

cricket = {"Rahul", "Aman", "Bhomdev", "Neha"}

football = {"Aman", "Neha", "Riya", "Karan"}

print("Cricket Team")
print(cricket)

print("\nFootball Team")
print(football)

print("\nStudents Playing Both Sports")

print(cricket.intersection(football))

print("\nStudents Playing At Least One Sport")

print(cricket.union(football))

print("\nOnly Cricket Players")

print(cricket.difference(football))

print("\nOnly Football Players")

print(football.difference(cricket))

print("\nStudents Playing Only One Sport")

print(cricket.symmetric_difference(football))

# ==========================================================
# REMOVE DUPLICATES FROM TWO LISTS
# ==========================================================

print("\n" + "=" * 70)
print("12. REMOVE DUPLICATES")
print("=" * 70)

list1 = [10, 20, 30, 20, 40]

list2 = [30, 40, 50, 60, 50]

unique = set(list1).union(set(list2))

print("Unique Values")

print(unique)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("union()                       -> Combines two sets")
print("intersection()                -> Common elements")
print("difference()                  -> Elements in first set only")
print("symmetric_difference()        -> Elements not common")
print("issubset()                    -> Checks subset")
print("issuperset()                  -> Checks superset")
print("isdisjoint()                  -> Checks no common elements")
print("intersection_update()         -> Updates with common elements")
print("difference_update()           -> Removes common elements")
print("symmetric_difference_update() -> Updates with non-common elements")

print("=" * 70)
print("End of set_operations.py")
print("=" * 70)
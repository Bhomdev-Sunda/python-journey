#              Python Set Methods 
print("=" * 65)
print("               PYTHON SET METHODS")
print("=" * 65)

# ==========================================================
# SAMPLE SET
# ==========================================================

numbers = {10, 20, 30, 40, 50}

print("\nOriginal Set")
print(numbers)

# ==========================================================
# add()
# ==========================================================

print("\n" + "=" * 65)
print("1. add() Method")
print("=" * 65)

numbers.add(60)

print("After Adding 60")
print(numbers)

# ==========================================================
# update()
# ==========================================================

print("\n" + "=" * 65)
print("2. update() Method")
print("=" * 65)

numbers.update([70, 80])

print("After Updating")
print(numbers)

# ==========================================================
# remove()
# ==========================================================

print("\n" + "=" * 65)
print("3. remove() Method")
print("=" * 65)

numbers.remove(20)

print("After Removing 20")
print(numbers)

# ==========================================================
# discard()
# ==========================================================

print("\n" + "=" * 65)
print("4. discard() Method")
print("=" * 65)

numbers.discard(30)

print("After Discarding 30")
print(numbers)

# discard() does not raise an error if the item doesn't exist
numbers.discard(500)

print("Discarding Non-Existing Element (500)")
print(numbers)

# ==========================================================
# pop()
# ==========================================================

print("\n" + "=" * 65)
print("5. pop() Method")
print("=" * 65)

removed = numbers.pop()

print("Removed Element :", removed)

print("Remaining Set")
print(numbers)

# ==========================================================
# copy()
# ==========================================================

print("\n" + "=" * 65)
print("6. copy() Method")
print("=" * 65)

copy_set = numbers.copy()

print("Copied Set")
print(copy_set)

# ==========================================================
# clear()
# ==========================================================

print("\n" + "=" * 65)
print("7. clear() Method")
print("=" * 65)

temp = {1, 2, 3, 4}

print("Before Clear")
print(temp)

temp.clear()

print("After Clear")
print(temp)

# ==========================================================
# len()
# ==========================================================

print("\n" + "=" * 65)
print("8. len() Function")
print("=" * 65)

print("Length :", len(numbers))

# ==========================================================
# in / not in
# ==========================================================

print("\n" + "=" * 65)
print("9. Membership Operators")
print("=" * 65)

print("40 in numbers :", 40 in numbers)

print("100 in numbers :", 100 in numbers)

print("50 not in numbers :", 50 not in numbers)

# ==========================================================
# LOOPING THROUGH SET
# ==========================================================

print("\n" + "=" * 65)
print("10. Loop Through Set")
print("=" * 65)

for value in numbers:
    print(value)

# ==========================================================
# UPDATE USING ANOTHER SET
# ==========================================================

print("\n" + "=" * 65)
print("11. update() With Another Set")
print("=" * 65)

set1 = {1, 2, 3}

set2 = {4, 5, 6}

print("Before Update")

print("Set1 :", set1)

print("Set2 :", set2)

set1.update(set2)

print("\nAfter Update")

print(set1)

# ==========================================================
# UPDATE USING TUPLE
# ==========================================================

print("\n" + "=" * 65)
print("12. update() With Tuple")
print("=" * 65)

fruits = {"Apple", "Mango"}

fruits.update(("Banana", "Orange"))

print(fruits)

# ==========================================================
# UPDATE USING LIST
# ==========================================================

print("\n" + "=" * 65)
print("13. update() With List")
print("=" * 65)

colors = {"Red", "Blue"}

colors.update(["Green", "Yellow"])

print(colors)

# ==========================================================
# REMOVE DUPLICATES USING SET
# ==========================================================

print("\n" + "=" * 65)
print("14. Remove Duplicates")
print("=" * 65)

data = [10, 20, 20, 30, 40, 30, 50]

unique = set(data)

print("Original List")
print(data)

print("Unique Values")
print(unique)

# ==========================================================
# REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 65)
print("15. Student Club Members")
print("=" * 65)

members = {"Rahul", "Aman", "Priya"}

print("Original Members")

print(members)

members.add("Bhomdev")

members.update(["Neha", "Riya"])

members.remove("Rahul")

print("\nUpdated Members")

for student in members:
    print(student)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)

print("add()      -> Adds one element")
print("update()   -> Adds multiple elements")
print("remove()   -> Removes an element (Error if missing)")
print("discard()  -> Removes an element (No Error)")
print("pop()      -> Removes a random element")
print("copy()     -> Creates a copy")
print("clear()    -> Removes all elements")
print("len()      -> Returns total elements")
print("in         -> Checks membership")
print("not in     -> Checks absence")

print("=" * 65)
print("End of set_methods.py")
print("=" * 65)
# 📘 Day 07 Notes – Python Lists

# 📌 What is a List?

A **list** is one of Python's most commonly used built-in data structures. It is used to store **multiple values in a single variable**.

Lists are **ordered**, **mutable (changeable)**, and can store **different data types** together.

A list is created using **square brackets `[]`**, with elements separated by commas.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]
```

A list can contain:

* Integers
* Floats
* Strings
* Boolean values
* Other lists (Nested Lists)
* Mixed data types

Example:

```python
data = [101, "Bhomdev", 95.5, True]
```

---

# ⭐ Characteristics of Lists

Python lists have several important characteristics.

### 1. Ordered

Items maintain their insertion order.

```python
colors = ["Red", "Green", "Blue"]
```

Output:

```
Red
Green
Blue
```

---

### 2. Mutable

Lists can be modified after creation.

```python
numbers = [10, 20, 30]

numbers[1] = 100

print(numbers)
```

Output

```
[10, 100, 30]
```

---

### 3. Allows Duplicate Values

```python
marks = [90, 90, 85, 90]
```

Duplicates are allowed.

---

### 4. Can Store Different Data Types

```python
student = [101, "Bhomdev", 92.5, True]
```

---

### 5. Dynamic Size

Lists automatically grow or shrink.

```python
numbers.append(40)
numbers.remove(20)
```

---

### 6. Supports Indexing and Slicing

Lists allow quick access to elements.

```python
numbers[0]
numbers[-1]
numbers[1:4]
```

---

# 🎯 Why Do We Use Lists?

Without lists, if you wanted to store 100 student names, you would need 100 variables.

```python
student1
student2
student3
...
student100
```

This is inefficient.

Using a list:

```python
students = []
```

Now all student names are stored in one variable.

Lists help us:

* Store large collections of data
* Manage records easily
* Process data using loops
* Build real-world applications

---

# 📌 Creating Lists

### Empty List

```python
numbers = []
```

---

### Integer List

```python
numbers = [10, 20, 30, 40]
```

---

### String List

```python
fruits = ["Apple", "Banana", "Orange"]
```

---

### Mixed List

```python
data = [101, "Bhomdev", 95.5, True]
```

---

### Nested List

```python
students = [
    [101, "Bhomdev"],
    [102, "Rahul"]
]
```

---

# 📌 List Indexing

Indexing means accessing elements using their position.

Positive Index

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])
```

Output

```
Apple
```

Negative Index

```python
print(fruits[-1])
```

Output

```
Orange
```

---

# 📌 List Slicing

Slicing extracts a portion of a list.

Syntax

```python
list[start:stop:step]
```

Examples

```python
numbers = [10,20,30,40,50]

numbers[:3]
numbers[2:]
numbers[1:4]
numbers[::-1]
numbers[::2]
```

---

# 📌 Updating Elements

Lists are mutable.

```python
students = ["Rahul", "Aman", "Priya"]

students[1] = "Bhomdev"

print(students)
```

Output

```
['Rahul', 'Bhomdev', 'Priya']
```

---

# 📌 Deleting Elements

Using remove()

```python
students.remove("Rahul")
```

Using pop()

```python
students.pop()
```

Using del

```python
del students[0]
```

Delete Entire List

```python
del students
```

---

# 📌 List Methods

## append()

Adds one element.

```python
numbers.append(100)
```

---

## extend()

Adds multiple elements.

```python
numbers.extend([200,300])
```

---

## insert()

Insert at specific position.

```python
numbers.insert(1,50)
```

---

## remove()

Removes first matching value.

```python
numbers.remove(50)
```

---

## pop()

Removes using index.

```python
numbers.pop()
numbers.pop(2)
```

---

## clear()

Removes all elements.

```python
numbers.clear()
```

---

## copy()

Creates a shallow copy.

```python
copy_list = numbers.copy()
```

---

## sort()

Sorts ascending.

```python
numbers.sort()
```

Descending

```python
numbers.sort(reverse=True)
```

---

## reverse()

Reverses order.

```python
numbers.reverse()
```

---

## count()

Counts occurrences.

```python
numbers.count(20)
```

---

## index()

Returns index.

```python
numbers.index(30)
```

---

# 📌 Looping Through Lists

Using for loop

```python
for item in fruits:
    print(item)
```

Using range()

```python
for i in range(len(fruits)):
    print(fruits[i])
```

Using while loop

```python
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

# 📌 Nested Lists

A nested list is a list inside another list.

Example

```python
students = [
    [101,"Bhomdev",90],
    [102,"Rahul",85],
    [103,"Priya",92]
]
```

Accessing data

```python
students[0][1]
students[2][2]
```

Looping

```python
for student in students:
    print(student)
```

---

# 🌍 Real-Life Applications

Lists are widely used in software development.

Examples

* Student Management System
* Employee Database
* Shopping Cart
* Hospital Records
* Library Management
* Hotel Management
* Contact Book
* Banking Applications
* Inventory Management
* E-Commerce Websites
* Social Media Applications
* Game Scoreboards

---

# ⚠️ Common Mistakes

### Forgetting Square Brackets

```python
numbers = 10,20,30
```

Wrong.

---

### Index Out of Range

```python
numbers[100]
```

Raises IndexError.

---

### Confusing append() with extend()

```python
numbers.append([1,2])
```

Produces

```
[10,20,[1,2]]
```

Whereas

```python
numbers.extend([1,2])
```

Produces

```
[10,20,1,2]
```

---

### Using remove() for Missing Values

```python
numbers.remove(500)
```

Raises ValueError.

---

### Forgetting Lists are Mutable

Changing one copied reference affects both variables unless you use `copy()`.

---

# 🔄 Difference Between List and String

| List                  | String                   |
| --------------------- | ------------------------ |
| Mutable               | Immutable                |
| Uses []               | Uses quotes              |
| Stores any data type  | Stores only characters   |
| Elements can change   | Characters cannot change |
| Supports list methods | Supports string methods  |

---

# 🔄 Difference Between append() and extend()

| append()                 | extend()                       |
| ------------------------ | ------------------------------ |
| Adds one object          | Adds multiple elements         |
| Keeps nested list intact | Adds each element individually |
| Returns None             | Returns None                   |

Example

```python
numbers.append([4,5])
```

Output

```
[1,2,3,[4,5]]
```

Example

```python
numbers.extend([4,5])
```

Output

```
[1,2,3,4,5]
```

---

# 🔄 Difference Between remove(), pop(), and del

| remove()                           | pop()                              | del                             |
| ---------------------------------- | ---------------------------------- | ------------------------------- |
| Removes by value                   | Removes by index                   | Deletes by index or entire list |
| Returns nothing                    | Returns removed value              | Returns nothing                 |
| Raises ValueError if value missing | Raises IndexError if invalid index | Deletes objects                 |

---

# 🎤 Interview Questions (Detailed Answers)

## 1. What is a list?

A list is an ordered, mutable collection in Python that stores multiple values in a single variable. It can contain duplicate values and mixed data types.

---

## 2. Why are lists called mutable?

Lists are called mutable because their contents can be modified after creation. You can add, update, remove, or rearrange elements without creating a new list.

---

## 3. Difference between a list and a tuple?

Lists are mutable and use square brackets `[]`, while tuples are immutable and use parentheses `()`. Lists are preferred when data changes frequently; tuples are better for fixed data.

---

## 4. Difference between append() and extend()?

`append()` adds a single object to the end of the list. `extend()` adds each element from another iterable individually.

---

## 5. Difference between remove(), pop(), and del?

* `remove()` deletes the first matching value.
* `pop()` removes an element by index and returns it.
* `del` deletes an element, a slice, or the entire list.

---

## 6. What is list slicing?

List slicing extracts a portion of a list using the syntax:

```python
list[start:stop:step]
```

It is useful for copying lists, reversing lists, and extracting subsets.

---

## 7. What is a nested list?

A nested list is a list that contains one or more lists as its elements. It is commonly used to represent tables, matrices, and structured records.

---

## 8. How do you copy a list?

You can copy a list using:

```python
copy_list = original.copy()
```

or

```python
copy_list = original[:]
```

Both create a shallow copy.

---

# ⭐ Key Takeaways

* Lists store multiple values in one variable.
* Lists are ordered and mutable.
* Indexing starts at 0.
* Negative indexing starts from the end.
* Slicing extracts parts of a list.
* Lists support many useful built-in methods.
* Lists work efficiently with loops.
* Nested lists store structured data.
* Lists are one of the most important Python data structures used in real-world applications.

---

# 📖 Revision Summary

✔ Learned what a list is.

✔ Learned characteristics of lists.

✔ Created different types of lists.

✔ Used positive and negative indexing.

✔ Used list slicing.

✔ Updated and deleted elements.

✔ Practiced all common list methods.

✔ Used loops with lists.

✔ Worked with nested lists.

✔ Compared lists with strings and tuples.

✔ Learned common mistakes.

✔ Answered important interview questions.

---

# 🎯 Today's Goal (Completed)

By the end of Day 7, you should now be able to:

✅ Create and modify lists.

✅ Use common list methods confidently.

✅ Access data using indexing and slicing.

✅ Process lists using `for` and `while` loops.

✅ Build small real-world projects using lists.

✅ Explain Python lists clearly and confidently in technical interviews.

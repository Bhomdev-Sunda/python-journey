# 📘 Day 15 Notes – Object-Oriented Programming (OOP)

# What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **objects** instead of only functions.

An object represents a real-world entity that contains:

- **Attributes (Data)**
- **Methods (Behavior)**

OOP helps make programs:

- Modular
- Reusable
- Easy to maintain
- Easy to extend
- Closer to real-world modeling

Python is a fully object-oriented programming language.

---

# Why Do We Use OOP?

Without OOP, programs become difficult to manage as they grow.

OOP helps developers:

- Organize code efficiently
- Reuse existing code
- Reduce duplication
- Improve readability
- Simplify debugging
- Build scalable applications

Real-world examples:

- Banking Systems
- Hospital Management Systems
- Student Management Systems
- E-commerce Websites
- Social Media Platforms
- AI & ML Applications
- Game Development

---

# What is a Class?

A **class** is a blueprint or template used to create objects.

It defines:

- Data (Attributes)
- Functions (Methods)

A class itself does not store actual data.

It simply defines how objects should look and behave.

Example:

A class "Car" defines:

- Brand
- Model
- Color

Every actual car created from this blueprint becomes an object.

---

# What is an Object?

An object is an **instance of a class**.

Objects contain actual values.

Example:

Class:

Car

Objects:

- Toyota Fortuner
- Hyundai Creta
- Honda City

Each object has different data but follows the same blueprint.

---

# Relationship Between Class and Object

Think of it like this:

Blueprint → House

Class → Object

Recipe → Dish

Cookie Cutter → Cookie

Template → Document

One class can create multiple objects.

Each object has its own data.

---

# What are Attributes?

Attributes are variables that belong to an object.

They store information about that object.

Examples:

Student

- Name
- Age
- Marks
- Course

Car

- Brand
- Model
- Price
- Color

Employee

- Name
- Department
- Salary

Each object stores its own attribute values.

---

# Instance Attributes

Instance attributes belong to individual objects.

Each object has its own copy.

Example:

Student 1

Name = Bhomdev

Marks = 95

Student 2

Name = Rahul

Marks = 82

Although both belong to the same class, their data is different.

---

# What is a Method?

A method is a **function defined inside a class**.

Methods describe what an object can do.

Examples:

Student

- study()
- attend_class()

Bank Account

- deposit()
- withdraw()

Car

- start()
- stop()

Employee

- work()

Methods operate on object data.

---

# self Keyword

The **self** keyword refers to the current object.

Python automatically passes the object as the first argument whenever an instance method is called.

Example:

```python
student.display()
```

Internally Python executes:

```python
Student.display(student)
```

The variable `self` points to the object that called the method.

---

# Why Do We Use self?

self allows methods to:

- Access object attributes
- Modify object data
- Call other methods

Without self, object data cannot be stored properly.

Correct:

```python
self.name = name
```

Wrong:

```python
name = name
```

The second statement creates only a local variable.

---

# Constructor (__init__)

A constructor is a special method named:

```python
__init__()
```

It executes automatically whenever an object is created.

Example:

```python
class Student:

    def __init__(self):
        print("Object Created")
```

Whenever:

```python
student = Student()
```

Python automatically calls:

```python
__init__()
```

---

# Why Do We Use Constructors?

Constructors initialize object data automatically.

Instead of:

```python
student.name = "Bhomdev"
student.age = 22
```

We can simply write:

```python
student = Student("Bhomdev", 22)
```

This makes object creation easier and cleaner.

---

# Constructor with Parameters

Constructors can accept values.

Example:

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

Creating objects:

```python
student = Student("Bhomdev", 22)
```

Each object receives different values.

---

# Constructor vs Normal Method

| Constructor | Normal Method |
|------------|---------------|
| Automatically called | Called manually |
| Name is __init__() | Any valid name |
| Initializes object | Performs operations |
| Executes once during object creation | Can execute many times |

---

# Dynamic Attributes

Python allows attributes to be added even after object creation.

Example:

```python
student.city = "Delhi"
```

This creates a new attribute instantly.

---

# Built-in Attribute Functions

## hasattr()

Checks whether an attribute exists.

Example:

```python
hasattr(student, "name")
```

Returns:

```python
True
```

---

## getattr()

Gets an attribute safely.

Example:

```python
getattr(student, "name")
```

Default value:

```python
getattr(student, "salary", "Not Found")
```

---

## setattr()

Creates or updates an attribute.

Example:

```python
setattr(student, "college", "ABC College")
```

---

## delattr()

Deletes an attribute.

Example:

```python
delattr(student, "city")
```

---

# __dict__

Every object stores its attributes in a dictionary.

Example:

```python
print(student.__dict__)
```

Output:

```python
{
'name': 'Bhomdev',
'age': 22,
'course': 'Python'
}
```

Useful for debugging.

---

# id()

Returns the memory address of an object.

Example:

```python
id(student)
```

Useful for checking whether two variables refer to the same object.

---

# is vs ==

## ==

Compares values.

Example:

```python
5 == 5
```

Returns:

```python
True
```

---

## is

Compares object identity (memory location).

Example:

```python
obj1 is obj2
```

Returns:

True only if both variables refer to the exact same object.

---

# Real-Life Uses of OOP

OOP is used almost everywhere:

- Banking Applications
- Hospital Management
- Student Management
- Employee Management
- Inventory Systems
- Hotel Booking
- E-commerce Websites
- Chat Applications
- Social Media
- Games
- Robotics
- Artificial Intelligence
- Machine Learning
- Backend APIs

---

# Advantages of OOP

- Code Reusability
- Easy Maintenance
- Better Security
- Better Organization
- Easy Debugging
- Scalable Applications
- Real-world Modeling
- Team Collaboration

---

# Common Beginner Mistakes

❌ Forgetting `self`

Wrong:

```python
name = name
```

Correct:

```python
self.name = name
```

---

❌ Writing `init()` instead of `__init__()`

Correct:

```python
def __init__(self):
```

---

❌ Calling methods without creating objects

Wrong:

```python
Student.display()
```

Correct:

```python
student = Student()
student.display()
```

---

❌ Forgetting parentheses while creating an object

Wrong:

```python
student = Student
```

Correct:

```python
student = Student()
```

---

# Interview Questions

## 1. What is OOP?

Object-Oriented Programming is a programming paradigm that organizes programs using classes and objects.

---

## 2. What is a class?

A class is a blueprint used to create objects.

---

## 3. What is an object?

An object is an instance of a class containing actual data.

---

## 4. What are attributes?

Attributes are variables that store object data.

---

## 5. What are methods?

Methods are functions defined inside a class that describe object behavior.

---

## 6. What is self?

self is a reference to the current object.

Python automatically passes it as the first argument of every instance method.

---

## 7. What is a constructor?

A constructor is the special `__init__()` method that runs automatically when an object is created.

---

## 8. Why do we use constructors?

To initialize object data automatically.

---

## 9. Difference between Class and Object?

Class is a blueprint.

Object is an actual instance created from that blueprint.

---

## 10. Difference between Attribute and Method?

Attributes store data.

Methods perform actions.

---

## 11. Difference between == and is?

`==` compares values.

`is` compares object identity (memory location).

---

## 12. What does __dict__ do?

It returns all instance attributes as a dictionary.

---

# Key Takeaways

- OOP organizes code using classes and objects.
- A class is a blueprint, while an object is its instance.
- Attributes store data, and methods define behavior.
- `self` refers to the current object.
- `__init__()` is a constructor that initializes object data automatically.
- Every object has its own instance attributes.
- Python provides `hasattr()`, `getattr()`, `setattr()`, and `delattr()` to manage attributes.
- `__dict__` displays an object's stored attributes.
- OOP makes programs reusable, organized, maintainable, and scalable.
- OOP is widely used in backend development, AI/ML, automation, APIs, and enterprise software.
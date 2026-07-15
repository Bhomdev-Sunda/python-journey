
# 📘 Day 08 Notes – Python Tuples

## What is a Tuple?
A tuple is an **ordered, immutable** collection of values. Once created, its contents cannot be changed.

### Syntax
```python
student = ("Bhomdev", 22, "Python")
```

## Characteristics
- Ordered
- Immutable
- Allows duplicate values
- Stores multiple data types
- Supports indexing and slicing
- Faster and more memory-efficient than lists

## Why Tuples are Used
- Fixed data (days, months, coordinates)
- Better performance
- Data safety
- Hashable (when elements are immutable)

## Creating Tuples
```python
t1 = (1,2,3)
t2 = "A","B","C"
t3 = tuple([10,20,30])
empty = ()
```

## Single-Element Tuples
```python
a = (10,)   # Correct
b = (10)    # int
```
Python recognizes the comma, not the parentheses.

## Indexing
```python
colors=("Red","Green","Blue")
print(colors[0])
print(colors[-1])
```

## Slicing
```python
nums=(10,20,30,40,50)
print(nums[1:4])
print(nums[:3])
print(nums[-2:])
print(nums[::-1])
```

## Tuple Packing
```python
employee = 101, "Rahul", "IT"
```

## Tuple Unpacking
```python
emp_id, name, dept = employee
```

## Tuple Methods
Only two methods exist:
```python
data=(1,2,2,3,2)
print(data.count(2))
print(data.index(3))
```

## Membership Operators
```python
fruits=("Apple","Mango","Orange")
print("Apple" in fruits)
print("Banana" not in fruits)
```

## Nested Tuples
```python
students=(
 (101,"Rahul",90),
 (102,"Aman",85),
 (103,"Bhomdev",98)
)
print(students[2][1])
```

## Looping Through Tuples
```python
for value in ("A","B","C"):
    print(value)

for roll,name,marks in students:
    print(roll,name,marks)
```

## List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | [] | () |
| Mutable | Yes | No |
| Speed | Slower | Faster |
| Methods | Many | count(), index() |
| Memory | More | Less |

## Real-Life Applications
- Employee records
- Student records
- GPS coordinates
- RGB colors
- Days of week
- Months of year
- Database rows
- Flight information

## Common Mistakes
1. Forgetting comma in single-element tuple.
2. Trying to modify tuple values.
3. Using append() or remove() on tuples.
4. Confusing list [] with tuple ().

# 🎤 Interview Questions

### What is a tuple?
An ordered and immutable collection.

### Why are tuples immutable?
To protect data and improve performance.

### Difference between list and tuple?
Lists are mutable; tuples are immutable.

### Why is a comma required in a single-element tuple?
Python identifies tuples using the comma.

### What are tuple packing and unpacking?
Packing combines values into one tuple. Unpacking assigns tuple values to variables.

### Which methods are available for tuples?
count() and index().

### Can a tuple contain a list?
Yes.
```python
data=(1,[10,20],3)
```
The tuple cannot change, but the list inside it can.

### Can a tuple be a dictionary key? Why?
Yes, if every element is immutable (hashable).
```python
marks={
 ("Bhomdev",101):95
}
```

## Key Takeaways
- Tuples are immutable.
- Faster than lists.
- Only two built-in methods.
- Support indexing, slicing, nesting, packing and unpacking.
- Best for fixed/read-only data.

## Revision Summary
- ✅ What is a tuple
- ✅ Characteristics
- ✅ Why tuples are used
- ✅ Creating tuples
- ✅ Single-element tuples
- ✅ Indexing
- ✅ Slicing
- ✅ Packing
- ✅ Unpacking
- ✅ Tuple methods
- ✅ Membership operators
- ✅ Nested tuples
- ✅ Looping
- ✅ List vs Tuple
- ✅ Real-life applications
- ✅ Common mistakes
- ✅ Interview questions & answers

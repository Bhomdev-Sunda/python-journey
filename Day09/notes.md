# 📘 Day 09 Notes – Python Dictionaries


# What is a Dictionary?
A dictionary is an ordered, mutable collection that stores data as key-value pairs. Each key is unique and is used to access its corresponding value.

```python
student={'name':'Bhomdev','age':22}
```


# Characteristics
- Ordered (Python 3.7+)
- Mutable
- Unique keys
- Duplicate values allowed
- Fast lookup using keys
- Can store any data type


# Why Dictionaries are Used
Used for structured data such as student records, employee details, product catalogs, JSON responses, configuration settings and APIs because values can be accessed quickly using keys.


# Creating Dictionaries
```python
d={}
d={'a':1,'b':2}
d2=dict(name='Rahul',age=20)
```


# Accessing Values
```python
print(d['a'])
print(d.get('a'))
print(d.get('x','Not Found'))
```
`[]` raises `KeyError` if the key is missing, while `get()` safely returns `None` or a default value.


# Updating Values
```python
d['a']=100
d.update({'city':'Patiala'})
```


# Adding and Deleting
```python
d['course']='Python'
d.pop('course')
del d['a']
d.clear()
```


# Dictionary Methods

| Method | Description |
|---|---|
| get() | Safely returns value |
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| update() | Updates dictionary |
| pop() | Removes key and returns value |
| popitem() | Removes last pair |
| copy() | Creates shallow copy |
| setdefault() | Adds key if absent |
| fromkeys() | Creates dictionary from iterable |
| clear() | Removes all items |



# Looping
```python
for k,v in d.items():
    print(k,v)
```


# Nested Dictionaries
```python
students={101:{'name':'Rahul','marks':90},102:{'name':'Bhomdev','marks':95}}
```


# Dictionary Comprehension
```python
squares={x:x*x for x in range(1,6)}
even={x:x for x in range(10) if x%2==0}
```


# Real-life Applications
- Student Management
- Employee Database
- Shopping Cart
- Banking
- Hospital Records
- JSON/API data
- Inventory Systems
- User Profiles


# Common Mistakes
- Duplicate keys overwrite previous values.
- Using `[]` for missing keys.
- Trying to use a list as a dictionary key.
- Forgetting `.items()` when looping over key-value pairs.


# 📊 List vs Tuple vs Dictionary

| Feature | List | Tuple | Dictionary |
|---|---|---|---|
| Syntax | `[]` | `()` | `{}` |
| Stores | Values | Values | Key : Value |
| Mutable | ✅ Yes | ❌ No | ✅ Yes |
| Ordered | ✅ | ✅ | ✅ |
| Duplicate Values | ✅ | ✅ | ✅ |
| Duplicate Keys | N/A | N/A | ❌ |
| Access | Index | Index | Key |
| Slicing | ✅ | ✅ | ❌ |
| Comprehension | ✅ | ❌ | ✅ |
| Built-in Methods | Many | 2 | Many |
| Memory Usage | More | Less | Moderate |
| Speed | Good | Fastest | Fast lookup |
| Best For | Dynamic collections | Fixed data | Structured records |
| JSON Equivalent | Array | None | Object |
| Can Nest | ✅ | ✅ | ✅ |
| Hashable | ❌ | Sometimes | ❌ |
| Example | Shopping list | Coordinates | Student record |

# 🎤 Interview Questions

### 1. What is a dictionary?
A mutable collection of unique keys mapped to values.

### 2. Why are dictionary keys unique?
Because each key identifies exactly one value. If a duplicate key is inserted, the old value is replaced.

### 3. Difference between `get()` and `[]`?
- `get()` safely returns `None` or a default.
- `[]` raises `KeyError` if the key doesn't exist.

### 4. Difference between `keys()`, `values()`, and `items()`?
- `keys()` → keys only
- `values()` → values only
- `items()` → key-value pairs

### 5. Difference between `pop()` and `del`?
`pop()` returns the removed value; `del` simply deletes.

### 6. What is a nested dictionary?
A dictionary containing another dictionary as a value.

### 7. Can dictionary keys be lists?
No. Lists are mutable and unhashable. Keys must be immutable and hashable.

### 8. What is dictionary comprehension?
A concise way to build dictionaries from iterables.

# Key Takeaways
- Dictionaries use key-value pairs.
- Keys must be unique.
- Values can repeat.
- Dictionaries are mutable.
- `items()` is the best way to loop through key-value pairs.
- Dictionary comprehension makes code concise.

# Revision Summary
✅ Basics
✅ Creating dictionaries
✅ Accessing values
✅ Updating
✅ Adding & deleting
✅ Methods
✅ Looping
✅ Nested dictionaries
✅ Dictionary comprehension
✅ Comparison table
✅ Interview questions



# 📘 Day 10 Notes - Python Sets

# What is a Set?
A **set** is an unordered, mutable collection of **unique** elements. Duplicate values are removed automatically.

```python
numbers={10,20,30}
```

## Characteristics
- Unordered
- Mutable
- Unique elements only
- No indexing or slicing
- Fast membership testing
- Can store immutable data types

## Why Sets are Used
- Remove duplicates
- Fast searching
- Mathematical operations
- Compare collections
- Data cleaning

## Creating Sets

```python
a={1,2,3}
b=set([1,2,2,3])
c=set("python")
d=set((1,2,3))
```

## Empty Set vs Dictionary

| Code | Result |
|---|---|
| `{}` | Empty Dictionary |
| `set()` | Empty Set |

## Adding Elements

```python
s={1,2}
s.add(3)
s.update([4,5])
```

## Removing Elements

```python
s.remove(2)
s.discard(10)
x=s.pop()
s.clear()
```

## Membership Testing

```python
10 in s
20 not in s
```

## Set Operations

| Operation | Method | Operator |
|---|---|---|
| Union | union() | `|` |
| Intersection | intersection() | `&` |
| Difference | difference() | `-` |
| Symmetric Difference | symmetric_difference() | `^` |
| Subset | issubset() | - |
| Superset | issuperset() | - |
| Disjoint | isdisjoint() | - |

## Set Methods

| Method | Purpose |
|---|---|
| add() | Add one element |
| update() | Add multiple elements |
| remove() | Remove item (error if absent) |
| discard() | Remove item (no error) |
| pop() | Remove random element |
| clear() | Remove all |
| copy() | Copy set |

## Frozenset

A **frozenset** is an immutable set.

```python
rules=frozenset({"Read","Write"})
```

It supports reading and set operations but **not** add(), remove(), update(), pop() or clear().

## Real-life Applications
- Student attendance
- Unique visitors
- Tags/hashtags
- Product categories
- Database duplicate removal
- Permissions
- Recommendation systems

## Common Mistakes
- Using `{}` instead of `set()`
- Expecting order from a set
- Trying to index a set
- Using mutable objects like lists inside a set
- Using remove() without checking existence

# 📊 List vs Tuple vs Dictionary vs Set

| Feature | List | Tuple | Dictionary | Set |
|---|---|---|---|---|
| Syntax | [] | () | {} | {} / set() |
| Stores | Values | Values | Key:Value | Unique Values |
| Ordered | ✅ | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicate Values | ✅ | ✅ | Values ✅ | ❌ |
| Duplicate Keys | N/A | N/A | ❌ | N/A |
| Indexing | ✅ | ✅ | By key | ❌ |
| Slicing | ✅ | ✅ | ❌ | ❌ |
| Lookup Speed | Medium | Medium | Very Fast | Very Fast |
| Best Use | Dynamic list | Fixed data | Structured records | Unique data |

# 🎤 Interview Questions

### What is a set?
A mutable collection of unique elements.

### Why are duplicates not allowed in a set?
Sets are designed to store each value only once. Duplicate insertions are automatically ignored.

### Difference between remove() and discard()?

| remove() | discard() |
|---|---|
| Raises KeyError if missing | No error if missing |
| Use when item must exist | Use when unsure |

### Difference between pop() and remove()?

| pop() | remove() |
|---|---|
| Removes random element | Removes specified element |
| No argument | Requires element |

### Difference between set and list?

| Set | List |
|---|---|
| Unique values | Duplicates allowed |
| Unordered | Ordered |
| No indexing | Indexing supported |

### What is a frozenset?
An immutable version of a set.

### Can a set contain a list?
No. Lists are mutable and therefore unhashable.

### When would you use a set instead of a list?
When uniqueness and fast membership testing are more important than preserving order.

# Key Takeaways
- Sets remove duplicates automatically.
- Use `set()` for an empty set.
- `discard()` is safer than `remove()`.
- Set operations are efficient.
- Frozensets are immutable.

# Revision Summary
✅ Set basics
✅ Creating sets
✅ Empty set vs dictionary
✅ Adding & removing
✅ Membership testing
✅ Set operations
✅ Set methods
✅ Frozenset
✅ Applications
✅ Comparison table
✅ Interview questions

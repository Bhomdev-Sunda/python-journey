# 📘 Day 17 Notes – Iterables & Iterators in Python

## What is an Iterable?
An iterable is an object whose elements can be traversed one by one.

Examples:
- List
- Tuple
- String
- Dictionary
- Set
- Range
- File object

## What is an Iterator?
An iterator returns one value at a time and remembers its current position.

## Iterable vs Iterator

| Feature | Iterable | Iterator |
|---|---|---|
| Stores data | Yes | No |
| Supports for-loop | Yes | Yes |
| next() directly | No | Yes |

## iter()

```python
numbers=[1,2,3]
it=iter(numbers)
```

## next()

```python
print(next(it))
```

## StopIteration
Raised when an iterator has no remaining values.

## Iterator Protocol
- __iter__()
- __next__()

## Custom Iterator Example

```python
class Counter:
    def __init__(self,limit):
        self.current=1
        self.limit=limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.limit:
            v=self.current
            self.current+=1
            return v
        raise StopIteration
```

## Advantages
- Memory efficient
- Lazy evaluation
- Great for large datasets

## Common Mistakes
- Calling next() on a list
- Forgetting iter()
- Ignoring StopIteration

## Interview Questions
1. What is an iterable?
2. What is an iterator?
3. Difference between iterable and iterator?
4. What does iter() do?
5. What does next() do?
6. What is StopIteration?
7. What methods are required for a custom iterator?
8. How do for-loops use iterators?

## Revision Summary
- Iterable
- Iterator
- iter()
- next()
- StopIteration
- Custom Iterator

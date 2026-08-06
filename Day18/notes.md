# 📘 Day 18 Notes – Generators in Python

## What is a Generator?
A generator is a special function that uses `yield` to produce values one at a time.

## Why Generators?
- Memory efficient
- Lazy evaluation
- Ideal for large datasets

## yield vs return
- `yield` pauses execution.
- `return` ends execution.

## Generator Expression
```python
(x*x for x in range(5))
```
Uses `()` instead of `[]`.

## Infinite Generator
```python
def counter():
    n=1
    while True:
        yield n
        n+=1
```

## Real-life Applications
- File processing
- APIs
- Data pipelines
- ML
- Web scraping

## Common Mistakes
- Using return instead of yield
- Reusing exhausted generators
- Converting infinite generators to list

## Interview Questions
1. What is a generator?
2. What is yield?
3. Difference between yield and return?
4. What is lazy evaluation?
5. What is a generator expression?
6. What is an infinite generator?
7. Why are generators memory efficient?
8. What exception is raised when a generator ends?

## Revision Summary
- Generator
- yield
- next()
- StopIteration
- Generator Expression
- Infinite Generator
- Lazy Evaluation

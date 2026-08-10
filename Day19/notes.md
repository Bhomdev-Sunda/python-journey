# 📘 Day 19 Notes – First-Class Functions, Closures & Decorators

## What are First-Class Functions?
Functions are objects in Python. They can be assigned to variables, passed as arguments, returned from functions, and stored in collections.

## Nested Functions
A nested function is a function defined inside another function. They help organize code and are the basis of closures.

## Closures
A closure is a nested function that remembers variables from its enclosing scope even after the outer function finishes. Use `nonlocal` to modify outer local variables.

## Decorators
Decorators add extra functionality to existing functions without modifying their source code.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Built-in Decorators

### @property
Creates attribute-like getter/setter methods.

### @staticmethod
Utility method that does not use `self` or `cls`.

### @classmethod
Works with the class using `cls`; useful for alternative constructors.

## Comparison

| Decorator | Purpose |
|-----------|---------|
| @property | Computed/read-only attributes |
| @staticmethod | Utility/helper methods |
| @classmethod | Class-level operations |

## Real-world Applications
- Flask/FastAPI route decorators
- Authentication
- Authorization
- Logging
- Timing
- Caching
- Validation

## Common Mistakes
- Passing `func()` instead of `func`
- Forgetting to return the wrapper
- Forgetting `*args` and `**kwargs`
- Forgetting `nonlocal`
- Confusing `@staticmethod` and `@classmethod`

## Interview Questions
1. What are first-class functions?
2. What is a higher-order function?
3. What is a nested function?
4. What is a closure?
5. What does `nonlocal` do?
6. What is a decorator?
7. Difference between `@property`, `@staticmethod`, and `@classmethod`?
8. Why are decorators used in frameworks?

## Key Takeaways
- Functions are first-class objects.
- Closures preserve state.
- Decorators wrap functions.
- `@property`, `@staticmethod`, and `@classmethod` simplify OOP.

## Revision Summary
- First-Class Functions
- Higher-Order Functions
- Nested Functions
- Closures
- nonlocal
- Decorators
- Decorator Factory
- @property
- @staticmethod
- @classmethod

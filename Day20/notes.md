# 📘 Day 20 Notes – `*args`, `**kwargs`, and Argument Unpacking

## 1. What is `*args`?

`*args` allows a function to accept any number of positional arguments.

```python
def show_numbers(*args):
    print(args)

show_numbers(10, 20, 30)
```

Output:
```text
(10, 20, 30)
```

- `args` is a tuple.
- `*` collects extra positional arguments.
- `args` is a conventional name.

---

## 2. What is `**kwargs`?

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def show_details(**kwargs):
    print(kwargs)

show_details(name="Bhomdev", age=22)
```

Output:
```text
{'name': 'Bhomdev', 'age': 22}
```

- `kwargs` is a dictionary.
- `**` collects extra keyword arguments.
- `kwargs` is a conventional name.

---

## 3. `*args` vs `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Purpose | Extra positional arguments | Extra keyword arguments |
| Data type | Tuple | Dictionary |
| Example | `function(10, 20)` | `function(name="Bhomdev")` |
| Symbol | `*` | `**` |

---

## 4. Using `*args` and `**kwargs` Together

```python
def show_data(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show_data(10, 20, 30, name="Bhomdev", age=22)
```

Result:
```text
args: (10, 20, 30)
kwargs: {'name': 'Bhomdev', 'age': 22}
```

---

## 5. What is Argument Unpacking?

Unpacking takes values from a collection and passes them as individual function arguments.

```text
*  → positional unpacking
** → keyword/dictionary unpacking
```

### Positional unpacking

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]
print(add(*numbers))
```

### Dictionary unpacking

```python
def introduce(name, age, city):
    print(name, age, city)

data = {
    "name": "Bhomdev",
    "age": 22,
    "city": "Punjab"
}

introduce(**data)
```

Dictionary keys must match the function's parameter names.

---

## 6. Collecting vs Unpacking

### Collecting

```python
def function(*args):
    print(args)
```

`*args` collects positional arguments into a tuple.

### Unpacking

```python
numbers = [10, 20, 30]
function(*numbers)
```

`*numbers` unpacks the list.

The same distinction applies to `**kwargs` and `**dictionary`.

---

## 7. Merging Dictionaries with `**`

```python
personal = {
    "name": "Bhomdev",
    "age": 22
}

professional = {
    "role": "Python Developer",
    "skill": "Python"
}

combined = {
    **personal,
    **professional
}
```

If duplicate keys exist, the later value wins:

```python
first = {"role": "Student"}
second = {"role": "Developer"}

result = {**first, **second}
```

Result:
```python
{"role": "Developer"}
```

---

## 8. Argument Forwarding

Argument forwarding means passing arguments received by one function to another.

```python
def target(*args, **kwargs):
    print(args)
    print(kwargs)

def wrapper(*args, **kwargs):
    target(*args, **kwargs)
```

The important pattern is:

```python
function(*args, **kwargs)
```

---

## 9. Why `*args` and `**kwargs` Matter in Decorators

Decorators often need to work with functions having different parameters.

```python
def logger(function):

    def wrapper(*args, **kwargs):
        print("Function:", function.__name__)
        result = function(*args, **kwargs)
        return result

    return wrapper
```

This allows the decorator to preserve flexible positional and keyword arguments.

---

## 10. Flexible Functions

```python
def calculate_sum(*numbers):
    return sum(numbers)

print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40))
```

One function can accept different numbers of arguments.

---

## 11. Practical Student Example

```python
def student_profile(name, *skills, **details):

    print("Name:", name)

    for skill in skills:
        print("-", skill)

    for key, value in details.items():
        print(key, value)

student_profile(
    "Bhomdev",
    "Python",
    "SQL",
    "FastAPI",
    age=22,
    goal="AI Engineer"
)
```

---

## 12. Practical Shopping Cart Example

```python
def shopping_cart(*prices, **details):

    total = sum(prices)

    print("Prices:", prices)
    print("Total:", total)

    for key, value in details.items():
        print(key, value)

shopping_cart(
    499,
    799,
    299,
    customer="Bhomdev",
    payment="UPI"
)
```

---

## 13. Function Parameter Order

A useful structure is:

```python
def function(
    normal_parameter,
    *args,
    keyword_only_parameter="default",
    **kwargs
):
    pass
```

Example:

```python
def example(name, *skills, role="Developer", **details):
    pass
```

Remember: `*args` comes before `**kwargs`.

---

## 14. Starred Assignment

`*` can also collect multiple values during assignment.

```python
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:
```text
10
[20, 30, 40]
50
```

---

## 15. Common Mistakes

### Mistake 1 – Using `*` instead of `**`

For keyword arguments:

```python
function(**data)
```

not:

```python
function(*data)
```

### Mistake 2 – Dictionary keys don't match parameters

```python
def user(name, age):
    pass

data = {
    "username": "Bhomdev",
    "age": 22
}

user(**data)
```

This causes an error because `username` does not match `name`.

### Mistake 3 – Duplicate keyword arguments

Avoid passing the same keyword more than once.

### Mistake 4 – Assuming `args` is a list

`args` is a tuple.

```python
def test(*args):
    print(type(args))
```

### Mistake 5 – Assuming `kwargs` is a tuple

`kwargs` is a dictionary.

```python
def test(**kwargs):
    print(type(kwargs))
```

### Mistake 6 – Forgetting to unpack during forwarding

Correct:

```python
function(*args, **kwargs)
```

---

# 🎤 Interview Questions

### Q1. What is `*args`?

`*args` allows a function to accept a variable number of positional arguments. They are stored as a tuple.

### Q2. What is `**kwargs`?

`**kwargs` allows a function to accept a variable number of keyword arguments. They are stored as a dictionary.

### Q3. Difference between `*args` and `**kwargs`?

`*args` handles positional arguments and stores them in a tuple. `**kwargs` handles keyword arguments and stores them in a dictionary.

### Q4. What does `*` do in a function call?

It unpacks an iterable into positional arguments.

### Q5. What does `**` do in a function call?

It unpacks a dictionary into keyword arguments.

### Q6. Can `*args` and `**kwargs` be used together?

Yes:

```python
def function(*args, **kwargs):
    pass
```

### Q7. Why are they useful in decorators?

They allow wrappers to accept and forward different combinations of positional and keyword arguments.

### Q8. What type is `args`?

`tuple`

### Q9. What type is `kwargs`?

`dict`

### Q10. What is argument forwarding?

Passing arguments received by one function to another, commonly using:

```python
function(*args, **kwargs)
```

### Q11. What happens if `*args` receives no arguments?

It becomes:

```python
()
```

### Q12. What happens if `**kwargs` receives no arguments?

It becomes:

```python
{}
```

### Q13. What happens when duplicate keys are used while merging dictionaries?

The later value overrides the earlier value.

---

# 🔑 Key Takeaways

- `*args` collects variable positional arguments.
- `**kwargs` collects variable keyword arguments.
- `args` is a tuple.
- `kwargs` is a dictionary.
- `*` performs positional unpacking.
- `**` performs keyword/dictionary unpacking.
- `*args` and `**kwargs` can be used together.
- `**` can merge dictionaries.
- Later duplicate dictionary values override earlier values.
- Argument forwarding commonly uses `*args` and `**kwargs`.
- Decorators frequently use `*args` and `**kwargs`.
- Dictionary keys must match function parameter names when using `**`.

---

# 🔄 Revision Summary

```text
*args
  ↓
Extra positional arguments
  ↓
Tuple

**kwargs
  ↓
Extra keyword arguments
  ↓
Dictionary

*list / *tuple
  ↓
Positional unpacking

**dictionary
  ↓
Keyword unpacking

*args + **kwargs
  ↓
Flexible functions

*args + **kwargs in wrapper
  ↓
Argument forwarding
  ↓
Decorators
```

## ⭐ Most Important Pattern

```python
def wrapper(*args, **kwargs):
    result = function(*args, **kwargs)
    return result
```

Understand this pattern thoroughly before moving to advanced Python.

---

# 🎯 Day 20 Final Checklist

- [ ] Understand `*args`
- [ ] Understand `**kwargs`
- [ ] Know that `args` is a tuple
- [ ] Know that `kwargs` is a dictionary
- [ ] Understand positional unpacking
- [ ] Understand dictionary unpacking
- [ ] Know how to merge dictionaries with `**`
- [ ] Understand argument forwarding
- [ ] Understand `*args + **kwargs`
- [ ] Understand their role in decorators
- [ ] Complete `06_practice.py`
- [ ] Be able to explain the concepts in an interview

---

# 🚀 Day 20 Complete

```text
01_args_basics.py
02_kwargs_basics.py
03_args_unpacking.py
04_kwargs_unpacking.py
05_args_kwargs_together.py
06_practice.py
notes.md
```

### Connection to Previous Days

```text
Day 19
  ↓
First-class functions
Nested functions
Closures
Decorators

Day 20
  ↓
*args
**kwargs
Unpacking
Argument forwarding
Decorator arguments
```

These concepts form an important foundation for advanced Python, backend development, FastAPI, and framework code.
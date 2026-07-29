# 📘 Day 14 Notes – Exception Handling in Python

## What is Exception Handling?
Exception handling allows a program to handle runtime errors without crashing.

## Error vs Exception
- Error: Problem in code.
- Exception: Runtime issue that can be handled.

## Why Use Exception Handling?
- Prevent crashes
- Handle invalid input
- Improve reliability
- Better user experience

## Syntax

```python
try:
    pass
except ValueError:
    pass
else:
    pass
finally:
    pass
```

## Keywords
- try: risky code
- except: handles exceptions
- else: runs if no exception
- finally: always runs
- raise: manually raises an exception

## Custom Exception
```python
class MyError(Exception):
    pass
```

## Common Exceptions
- ZeroDivisionError
- ValueError
- TypeError
- NameError
- IndexError
- KeyError
- AttributeError
- FileNotFoundError
- ModuleNotFoundError
- ImportError
- AssertionError
- OverflowError

## Best Practices
- Catch specific exceptions.
- Keep try blocks small.
- Use finally for cleanup.
- Use meaningful error messages.

## Common Mistakes
- Using bare except
- Hiding all exceptions
- Ignoring error messages

## Interview Questions
1. What is exception handling?
2. Difference between error and exception?
3. What is try?
4. What is except?
5. What is else?
6. What is finally?
7. What is raise?
8. What is a custom exception?
9. Why use custom exceptions?
10. Difference between Exception and ValueError?

## Revision Summary
- try
- except
- else
- finally
- raise
- custom exceptions
- common exceptions

# 📘 Day 4 Notes – Python Strings

# What is a String?

A **string** is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

Strings are one of the most commonly used data types in Python. They are used to store and manipulate text such as names, addresses, emails, passwords, messages, file paths, and more.

Examples:

* `"Python"`
* `'Hello World'`
* `"12345"`
* `"Bhomdev"`

A string can contain:

* Letters
* Numbers
* Spaces
* Special characters
* Symbols

---

# Characteristics of Strings

* Strings are **ordered**, meaning each character has a fixed position (index).
* Strings are **immutable**, meaning you cannot change individual characters after the string is created.
* Strings support **indexing** and **slicing**.
* Strings can be concatenated using `+`.
* Strings can be repeated using `*`.
* Python provides many built-in methods to work with strings.

---

# Creating Strings

Python provides several ways to create strings.

## 1. Single Quotes

Used for simple strings.

Example:

`'Python'`

---

## 2. Double Quotes

Functionally the same as single quotes.

Example:

`"Python Programming"`

---

## 3. Triple Single Quotes

Used for multi-line text.

Example:

```text
'''Python
Programming'''
```

---

## 4. Triple Double Quotes

Also used for multi-line strings and documentation.

Example:

```text
"""Welcome
to Python"""
```

---

## 5. Empty String

A string with no characters.

Example:

`""`

---

## 6. Using str()

The `str()` function converts other data types into strings.

Examples:

* Integer → String
* Float → String
* Boolean → String

---

# String Indexing

Each character inside a string has an index.

Python uses **zero-based indexing**, meaning the first character is at index `0`.

Example:

```text
Python
```

| Character      | P  | y  | t  | h  | o  | n  |
| -------------- | -- | -- | -- | -- | -- | -- |
| Positive Index | 0  | 1  | 2  | 3  | 4  | 5  |
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

Positive indexing starts from the left.

Negative indexing starts from the right.

Examples of common access patterns:

* First character → index `0`
* Last character → index `-1`

Attempting to access an index outside the valid range raises an `IndexError`.

---

# String Slicing

Slicing extracts a portion (substring) of a string.

Syntax:

`string[start : stop : step]`

## Parameters

**start**

* Starting index (inclusive).

**stop**

* Ending index (exclusive).

**step**

* Number of positions to move each time.
* Default value is `1`.

---

## Common Slicing Patterns

| Slice        | Meaning                                    |
| ------------ | ------------------------------------------ |
| `text[:]`    | Entire string                              |
| `text[:5]`   | First five characters                      |
| `text[5:]`   | From index 5 to the end                    |
| `text[-5:]`  | Last five characters                       |
| `text[:-5]`  | Everything except the last five characters |
| `text[::2]`  | Every second character                     |
| `text[::3]`  | Every third character                      |
| `text[::-1]` | Reverse the string                         |
| `text[::-2]` | Reverse with a step of two                 |

---

# String Methods

String methods perform common operations on strings. They return a new string or a useful value without modifying the original string.

## Case Conversion

### `upper()`

Converts all letters to uppercase.

### `lower()`

Converts all letters to lowercase.

### `title()`

Capitalizes the first letter of every word.

### `capitalize()`

Capitalizes only the first letter of the string.

### `swapcase()`

Converts uppercase letters to lowercase and lowercase letters to uppercase.

---

## Removing Spaces

### `strip()`

Removes spaces from both ends of a string.

### `lstrip()`

Removes spaces from the left side.

### `rstrip()`

Removes spaces from the right side.

---

## Searching Methods

### `find()`

Returns the index of the first occurrence of a substring.

Returns `-1` if the substring is not found.

### `index()`

Works like `find()`, but raises an error if the substring is not found.

### `count()`

Returns how many times a substring appears.

---

## Replacing Text

### `replace()`

Replaces one substring with another.

---

## Checking Beginning and End

### `startswith()`

Checks whether a string starts with a specified value.

### `endswith()`

Checks whether a string ends with a specified value.

---

## Splitting and Joining

### `split()`

Splits a string into a list.

### `join()`

Joins list elements into a single string.

---

## Validation Methods

### `isalpha()`

Returns `True` if all characters are alphabetic.

### `isdigit()`

Returns `True` if all characters are digits.

### `isalnum()`

Returns `True` if all characters are alphabetic or numeric.

### `islower()`

Returns `True` if all letters are lowercase.

### `isupper()`

Returns `True` if all letters are uppercase.

### `istitle()`

Returns `True` if each word starts with a capital letter.

### `isspace()`

Returns `True` if the string contains only whitespace characters.

---

# Escape Sequences

Escape sequences are special character combinations that begin with a backslash (`\`). They allow you to format strings or include characters that would otherwise be difficult to type.

| Escape Sequence | Meaning           |
| --------------- | ----------------- |
| `\n`            | New line          |
| `\t`            | Horizontal tab    |
| `\\`            | Backslash         |
| `\'`            | Single quote      |
| `\"`            | Double quote      |
| `\b`            | Backspace         |
| `\r`            | Carriage return   |
| `\f`            | Form feed         |
| `\v`            | Vertical tab      |
| `\a`            | Alert/Bell        |
| `\uXXXX`        | Unicode character |
| `r"..."`        | Raw string        |

The most commonly used escape sequences are:

* `\n`
* `\t`
* `\\`
* `\"`
* `\'`
* `r"..."`

---

# f-Strings

An **f-string** (formatted string literal) is a string prefixed with `f` or `F` that allows variables and expressions to be embedded directly inside curly braces `{}`.

Examples of what you can include:

* Variables
* Mathematical expressions
* Function calls
* String methods

Benefits:

* Easy to read
* Easy to write
* Faster than older formatting methods
* Preferred in modern Python

Examples of formatting:

* Float with two decimal places: `.2f`
* Left, right, and center alignment using `<`, `>`, and `^`

---

# String Operators

## Concatenation (`+`)

Combines two or more strings into one.

Example:

* `"Hello" + " World"`

Result:

* `"Hello World"`

---

## Repetition (`*`)

Repeats a string multiple times.

Example:

* `"=" * 40`

Useful for creating separators and formatted output.

---

# Built-in Function

## `len()`

Returns the total number of characters in a string, including spaces and special characters.

---

# Real-Life Uses of Strings

Strings are used in almost every Python application, including:

* Login systems
* Registration forms
* Employee management systems
* Student management systems
* Banking applications
* Hospital management systems
* E-commerce websites
* Chat applications
* Email processing
* File handling
* Data analysis
* Web development
* APIs
* Automation scripts

---

# Interview Questions

## 1. What is a string?

A string is a sequence of characters enclosed in single, double, or triple quotes.

---

## 2. Are strings mutable?

No. Strings are **immutable**, which means individual characters cannot be changed after the string is created.

---

## 3. What is indexing?

Indexing is the process of accessing individual characters using their position (index).

---

## 4. What is slicing?

Slicing extracts a portion of a string using the syntax:

`string[start:stop:step]`

---

## 5. What is the difference between indexing and slicing?

* **Indexing** returns a single character.
* **Slicing** returns a substring.

---

## 6. What is the difference between `find()` and `index()`?

* `find()` returns `-1` if the substring is not found.
* `index()` raises an error if the substring is not found.

---

## 7. What is the difference between `strip()`, `lstrip()`, and `rstrip()`?

* `strip()` removes spaces from both ends.
* `lstrip()` removes spaces from the left.
* `rstrip()` removes spaces from the right.

---

## 8. What is an escape sequence?

An escape sequence is a special character combination beginning with a backslash (`\`) that performs formatting or represents special characters.

---

## 9. What is an f-string?

An f-string is a formatted string literal that allows variables and expressions to be embedded directly inside a string using `{}`.

---

## 10. What does `len()` do?

The `len()` function returns the number of characters in a string.

---

# Key Takeaways

* A string is a sequence of characters used to store text.
* Strings are ordered and immutable.
* Python supports indexing and slicing for accessing parts of a string.
* String methods simplify common text-processing tasks.
* Escape sequences help format output and include special characters.
* f-Strings are the preferred way to create readable and dynamic output.
* Concatenation and repetition are fundamental string operations.
* Strings are one of the most important data types in Python and are used in almost every real-world application.

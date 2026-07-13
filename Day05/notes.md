# 📘 Day 5 Notes – Conditional Statements in Python

# Introduction

In programming, we often need to make decisions. For example:

* Should a student pass or fail?
* Is a customer eligible for a discount?
* Can an employee access the company portal?
* Is a user allowed to log in?

Python provides **conditional statements** to make these decisions.

A conditional statement executes different blocks of code depending on whether a condition is **True** or **False**.

Conditional statements are one of the most important concepts in programming because they allow programs to become intelligent and interactive.

---

# What is a Condition?

A **condition** is an expression that evaluates to either:

* `True`
* `False`

Conditions are usually created using:

* Comparison Operators
* Logical Operators

Example:

* Age is greater than or equal to 18
* Salary is greater than 50,000
* Password is correct

---

# What are Conditional Statements?

A **conditional statement** is a statement that allows a program to make decisions based on one or more conditions.

Python supports the following conditional statements:

* `if`
* `if-else`
* `if-elif-else`
* Nested `if`
* `match-case`

---

# 1. if Statement

## Definition

The `if` statement executes a block of code **only if the condition is True**.

If the condition is False, the block is skipped.

---

## Syntax

```text
if condition:
    statement
```

---

## Flow

```text
Condition
    │
    ▼
 True ───► Execute Code
 False ──► Skip Code
```

---

## Example

Check if an employee is eligible to enter the office.

If age is greater than or equal to 18, allow entry.

---

## Real-Life Uses

* Login verification
* ATM withdrawal validation
* Age verification
* Product availability
* Employee access systems

---

# 2. if-else Statement

## Definition

The `if-else` statement provides two possible execution paths.

* If the condition is True, the `if` block runs.
* Otherwise, the `else` block runs.

---

## Syntax

```text
if condition:
    statement
else:
    statement
```

---

## Flow

```text
          Condition
          /      \
      True       False
       |            |
 Execute Code   Execute Else
```

---

## Example

Employee is allowed to enter the company only if age is at least 18.

Otherwise, access is denied.

---

## Real-Life Uses

* Login systems
* Student pass/fail
* Payment success/failure
* Scholarship eligibility
* Online booking

---

# 3. if-elif-else Statement

## Definition

The `if-elif-else` statement checks multiple conditions.

Python evaluates conditions from top to bottom.

As soon as one condition becomes True, the remaining conditions are skipped.

---

## Syntax

```text
if condition:
    statement

elif condition:
    statement

elif condition:
    statement

else:
    statement
```

---

## Flow

```text
Condition 1
     │
 True ─► Execute
 False
     │
Condition 2
     │
 True ─► Execute
 False
     │
Condition 3
     │
 True ─► Execute
 False
     │
Else Block
```

---

## Example

Employee performance evaluation:

* Excellent
* Good
* Average
* Poor

---

## Real-Life Uses

* Grade calculation
* Salary classification
* Tax calculation
* Performance review
* Hotel room categories

---

# 4. Nested if

## Definition

A **Nested if** means placing one `if` statement inside another `if` statement.

The inner condition is checked only if the outer condition is True.

---

## Syntax

```text
if condition:

    if another_condition:
        statement
```

---

## Flow

```text
First Condition
       │
     True
       │
Second Condition
       │
     True
       │
 Execute Code
```

---

## Example

Employee Login System

Step 1

Check employee age.

Step 2

If age is valid, verify employee ID.

---

## Real-Life Uses

* Banking systems
* Login verification
* Hospital management
* Online examinations
* Airport security

---

# 5. match-case Statement

## Definition

`match-case` is Python's version of a switch statement.

It compares one value against multiple cases.

Introduced in **Python 3.10**.

---

## Syntax

```text
match variable:

    case value:
        statement

    case value:
        statement

    case _:
        default statement
```

---

## Flow

```text
Value
  │
Match?
  │
Case 1
Case 2
Case 3
Default
```

---

## Example

Employee Department Portal

Department

* HR
* IT
* Finance
* Sales
* Marketing

Each department displays different information.

---

## Real-Life Uses

* ATM menu
* Restaurant menu
* Banking options
* Employee department selection
* Customer support menu

---

# Boolean Values

Python has only two Boolean values.

* `True`
* `False`

A Boolean value represents the result of a condition.

Examples:

* Age >= 18 → True
* Password Correct → False

Booleans are the foundation of all conditional statements.

---

# Indentation in Python

Python uses **indentation** (spaces at the beginning of a line) to define blocks of code.

Unlike many programming languages, Python does not use curly braces `{}`.

Example structure:

```text
if condition:
    statement
```

The indented statement belongs to the `if` block.

If indentation is incorrect, Python raises an `IndentationError`.

---

# Ternary Operator

The ternary operator is a shorthand way of writing an `if-else` statement in a single line.

## Syntax

```text
value_if_true if condition else value_if_false
```

## Example

Assigning "Pass" if marks are at least 33, otherwise "Fail".

---

## Benefits

* Shorter code
* Easy for simple conditions
* Improves readability when used appropriately

Avoid using ternary operators for complex logic.

---

# Real-Life Applications of Conditional Statements

Conditional statements are used in almost every software application.

Examples include:

* Login systems
* Banking software
* Hospital management
* Student management
* Employee management
* ATM machines
* Online shopping websites
* Food delivery applications
* Hotel booking systems
* Flight reservation systems
* Mobile applications
* Games
* AI chatbots
* E-commerce platforms

---

# Common Errors

* Missing colon (`:`)
* Incorrect indentation
* Using `=` instead of `==` for comparisons
* Forgetting the default `case _:` in `match-case`
* Incorrect logical conditions

---

# Best Practices

* Keep conditions simple.
* Use meaningful variable names.
* Maintain consistent indentation (4 spaces).
* Prefer `match-case` when comparing a single value against many fixed options.
* Use nested `if` only when necessary.
* Avoid deeply nested conditions as they reduce readability.

---

# Interview Questions and Answers

## 1. What is a conditional statement?

A conditional statement is a programming statement that executes different blocks of code depending on whether a condition evaluates to `True` or `False`.

---

## 2. Difference between if, if-else, and if-elif-else?

### if

Checks only one condition.

If the condition is False, nothing happens.

### if-else

Provides two execution paths.

One block runs if the condition is True, the other runs if it is False.

### if-elif-else

Used when multiple conditions need to be checked.

Python evaluates conditions from top to bottom and executes the first matching block.

---

## 3. What is a nested if?

A nested `if` is an `if` statement placed inside another `if` statement.

The inner condition is evaluated only after the outer condition is satisfied.

---

## 4. What is match-case?

`match-case` is Python's pattern matching statement introduced in Python 3.10.

It compares one value against multiple possible cases and executes the matching block.

---

## 5. Difference between match-case and if-elif?

### if-elif

* Can evaluate different expressions and ranges.
* Suitable for complex conditions.
* Uses Boolean expressions.

### match-case

* Compares a single value against fixed patterns.
* Cleaner when handling many fixed options.
* Similar to the switch statement in other programming languages.

---

## 6. Why is indentation important in Python?

Indentation defines code blocks in Python.

Without proper indentation, Python cannot determine which statements belong together, resulting in an `IndentationError`.

---

## 7. What is a Boolean value?

A Boolean value represents one of two logical states:

* `True`
* `False`

Conditional statements rely on Boolean values to decide which code to execute.

---

## 8. What is a ternary operator?

A ternary operator is a compact way to write a simple `if-else` statement in one line.

It returns one value if the condition is True and another if it is False.

---

# Key Takeaways

* Conditional statements help programs make decisions.
* Python supports `if`, `if-else`, `if-elif-else`, nested `if`, and `match-case`.
* Every condition evaluates to either `True` or `False`.
* Proper indentation is mandatory in Python.
* `match-case` is useful for comparing one value against multiple fixed choices.
* Nested `if` is used when one condition depends on another.
* The ternary operator provides a concise alternative for simple `if-else` expressions.
* Conditional statements are widely used in real-world software such as banking systems, login systems, and management applications.

---

# Revision Summary

✔ What is a condition

✔ Boolean values

✔ if statement

✔ if-else statement

✔ if-elif-else statement

✔ Nested if

✔ match-case

✔ Indentation

✔ Ternary operator

✔ Real-life uses

✔ Interview questions

✔ Best practices

✔ Common mistakes

---

# Today's Mini Project

**Smart Student Management System**

This project combined everything learned so far:

* Variables
* Data Types
* User Input
* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Strings
* Conditional Statements
* f-Strings
* Professional Output Formatting

It demonstrated how conditional statements are used in a real-world application to calculate:

* Total Marks
* Percentage
* Grade
* Pass/Fail Status
* Scholarship Eligibility

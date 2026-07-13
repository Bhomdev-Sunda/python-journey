# 📘 Day 6 Notes – Python Loops

# Introduction

In programming, we often need to perform the same task multiple times.

For example:

* Display employee records.
* Print invoices.
* Generate student IDs.
* Process customer orders.
* Send notifications to multiple users.

Writing the same code repeatedly is inefficient and makes programs difficult to maintain.

To solve this problem, Python provides **loops**.

A loop allows a block of code to execute repeatedly until a specified condition is met.

Loops are one of the fundamental building blocks of programming and are used in almost every real-world application.

---

# What is a Loop?

A **loop** is a control flow statement that repeatedly executes a block of code based on a condition or over a collection of data.

Instead of writing the same code multiple times, we write it once inside a loop.

The loop automatically repeats the execution.

---

# Why Do We Use Loops?

Loops help programmers:

* Reduce code duplication.
* Save development time.
* Improve code readability.
* Automate repetitive tasks.
* Process large amounts of data efficiently.
* Build scalable applications.

Without loops, even simple tasks would require writing many repeated statements.

---

# Types of Loops in Python

Python provides two primary loops:

1. **for Loop**
2. **while Loop**

Python also provides loop control statements:

* `break`
* `continue`
* `pass`

---

# 1. for Loop

## Definition

A **for loop** is used to iterate over a sequence such as:

* List
* Tuple
* String
* Dictionary
* Range
* Set

The loop executes once for every item in the sequence.

---

## Syntax

```text id="3fru4a"
for variable in sequence:
    statements
```

---

## Flow Diagram

```text id="e4v7sm"
Sequence
    │
    ▼
Next Item?
    │
   Yes
    │
Execute Code
    │
    ▼
Repeat
    │
   No
    ▼
End
```

---

## Example

Displaying employee names stored in a list.

The loop prints one employee name at a time.

---

## Real-Life Applications

* Employee attendance systems
* Student lists
* Product catalogs
* Email sending
* Report generation
* Processing orders
* Inventory systems

---

# 2. while Loop

## Definition

A **while loop** executes as long as a condition remains `True`.

Unlike the `for` loop, it is condition-based rather than sequence-based.

---

## Syntax

```text id="0d8vbw"
while condition:
    statements
```

---

## Flow Diagram

```text id="9vkpme"
Condition
   │
 True
   │
Execute Code
   │
Return to Condition
   │
False
   ▼
 End
```

---

## Example

Continuously asking a user to enter the correct employee ID until it matches the required value.

---

## Real-Life Applications

* Login systems
* Password verification
* ATM PIN verification
* Game menus
* Chat applications
* User input validation

---

# The range() Function

## Definition

The `range()` function generates a sequence of numbers.

It is most commonly used with the `for` loop.

Instead of writing numbers manually, Python generates them automatically.

---

## Syntax

### range(stop)

Starts from `0` and stops before `stop`.

---

### range(start, stop)

Starts from `start` and stops before `stop`.

---

### range(start, stop, step)

Moves according to the specified step value.

The step can be positive or negative.

---

## Real-Life Applications

* Employee ID generation
* Invoice numbers
* Roll numbers
* Ticket numbers
* Countdown timers
* Pagination

---

# Nested Loops

## Definition

A **nested loop** is a loop placed inside another loop.

The inner loop completes all its iterations before the outer loop moves to its next iteration.

---

## Syntax

```text id="hjbhhd"
for outer in sequence:

    for inner in sequence:
        statements
```

---

## Flow Diagram

```text id="wtvwmv"
Outer Loop

   │

Inner Loop

   │

Execute

   │

Repeat
```

---

## Real-Life Applications

* Seating arrangements
* Hotel room layouts
* School classroom layouts
* Parking systems
* Chess boards
* Calendar generation

---

# break Statement

## Definition

The `break` statement immediately terminates the nearest loop.

Control moves to the first statement after the loop.

---

## Syntax

```text id="6k1s5o"
if condition:
    break
```

---

## Real-Life Applications

* Stop searching after finding a record.
* Exit login attempts.
* Stop processing once a file is found.
* Exit menus.

---

# continue Statement

## Definition

The `continue` statement skips the current iteration and immediately moves to the next iteration of the loop.

The loop itself continues running.

---

## Syntax

```text id="vxig4j"
if condition:
    continue
```

---

## Real-Life Applications

* Skip unavailable products.
* Ignore cancelled orders.
* Skip invalid records.
* Ignore maintenance rooms.

---

# pass Statement

## Definition

The `pass` statement does nothing.

It acts as a placeholder where Python expects a statement.

---

## Syntax

```text id="6yqkpk"
if condition:
    pass
```

---

## Real-Life Applications

* Future feature development.
* Empty function definitions.
* Empty classes.
* Placeholder during project development.

---

# Loop else Block

Many programmers don't know that Python allows an `else` block with loops.

The `else` block executes only if the loop completes normally.

If the loop is terminated using `break`, the `else` block does not execute.

---

## Syntax

```text id="2w6jv7"
for item in sequence:
    statements
else:
    statements
```

The same applies to `while` loops.

---

# Common Mistakes

* Forgetting to update the condition in a `while` loop.
* Creating an infinite loop unintentionally.
* Incorrect indentation.
* Using `break` when `continue` is needed.
* Modifying loop variables incorrectly.
* Using the wrong range values.
* Forgetting that the stop value in `range()` is excluded.

---

# Difference Between for and while

| for Loop                           | while Loop                             |
| ---------------------------------- | -------------------------------------- |
| Used for sequences                 | Used for conditions                    |
| Number of iterations usually known | Number of iterations may be unknown    |
| Uses iterable objects              | Uses Boolean conditions                |
| Less chance of infinite loops      | Higher chance of infinite loops        |
| Commonly used with `range()`       | Commonly used for validation and menus |

---

# Difference Between break, continue, and pass

| break                        | continue                     | pass                    |
| ---------------------------- | ---------------------------- | ----------------------- |
| Stops the loop completely    | Skips current iteration      | Does nothing            |
| Exits the loop               | Continues the loop           | Placeholder only        |
| Used to terminate processing | Used to ignore one iteration | Used during development |

---

# Infinite Loop

## Definition

An **infinite loop** is a loop that never ends because its condition always remains `True`.

Example situations:

* Forgetting to update the loop variable.
* Using `while True` without a proper exit condition.

Infinite loops can cause programs to freeze or consume unnecessary system resources.

---

# Real-Life Applications of Loops

Loops are used in almost every software application.

Examples include:

* Banking software
* Employee management systems
* Hospital management systems
* Hotel booking systems
* Inventory management
* Student management
* ATM machines
* Mobile apps
* Games
* AI applications
* Data analysis
* Automation scripts

---

# Best Practices

* Choose the appropriate loop for the problem.
* Keep loop conditions simple.
* Avoid unnecessary nested loops.
* Use meaningful variable names.
* Prevent infinite loops by updating conditions correctly.
* Use `break`, `continue`, and `pass` only when they improve clarity.

---

# Interview Questions and Answers

## 1. What is a loop?

A loop is a control flow statement that repeatedly executes a block of code until a condition becomes False or all items in a sequence have been processed.

---

## 2. Why do we use loops?

Loops reduce code repetition, automate repetitive tasks, improve readability, and allow programs to process large amounts of data efficiently.

---

## 3. Difference between for and while loops?

A `for` loop is used to iterate over sequences such as lists, strings, or ranges when the number of iterations is usually known.

A `while` loop is condition-based and continues executing as long as the condition remains True. It is useful when the number of iterations is unknown.

---

## 4. What is range()?

`range()` is a built-in Python function that generates a sequence of numbers.

It is commonly used with `for` loops for counting and iteration.

---

## 5. Difference between break, continue, and pass?

* `break` exits the loop immediately.
* `continue` skips the current iteration and moves to the next.
* `pass` performs no action and acts as a placeholder.

---

## 6. What is an infinite loop?

An infinite loop is a loop that never terminates because its condition always evaluates to True or is never updated.

---

## 7. What is a nested loop?

A nested loop is a loop inside another loop.

The inner loop completes all its iterations for every iteration of the outer loop.

---

## 8. Can a loop have an else block?

Yes.

Both `for` and `while` loops can have an `else` block.

The `else` block executes only when the loop finishes normally.

If the loop exits using `break`, the `else` block is skipped.

---

# Key Takeaways

* Loops automate repetitive tasks.
* Python provides `for` and `while` loops.
* `range()` generates sequences of numbers.
* Nested loops allow working with multi-dimensional data.
* `break` terminates a loop.
* `continue` skips the current iteration.
* `pass` acts as a placeholder.
* Loops can include an `else` block.
* Infinite loops should be avoided unless intentionally controlled.
* Loops are essential in almost every real-world application.

---

# Revision Summary

✔ What is a loop

✔ Why loops are used

✔ Types of loops

✔ `for` loop

✔ `while` loop

✔ `range()` function

✔ Nested loops

✔ `break`

✔ `continue`

✔ `pass`

✔ Loop `else`

✔ Infinite loop

✔ Real-life applications

✔ Common mistakes

✔ Best practices

✔ Interview questions

# 📘 Day 3 Notes – Python Operators

## 1. What is an Operator?

An **operator** is a special symbol or keyword that tells Python to perform a specific operation on one or more values (called operands).

For example, operators can:

* Perform mathematical calculations
* Compare values
* Assign values to variables
* Combine multiple conditions
* Check membership in a collection
* Compare object identity

---

# 2. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Meaning             | Example        |
| -------- | ------------------- | -------------- |
| `+`      | Addition            | `10 + 5 = 15`  |
| `-`      | Subtraction         | `10 - 5 = 5`   |
| `*`      | Multiplication      | `10 * 5 = 50`  |
| `/`      | Division            | `10 / 5 = 2.0` |
| `//`     | Floor Division      | `10 // 3 = 3`  |
| `%`      | Modulus (Remainder) | `10 % 3 = 1`   |
| `**`     | Exponent (Power)    | `2 ** 3 = 8`   |

### Uses

* Billing systems
* Interest calculation
* Area and volume calculations
* Salary calculation
* Percentage calculation

---

# 3. Assignment Operators

Assignment operators assign values to variables.

| Operator | Equivalent To    |
| -------- | ---------------- |
| `=`      | Assign value     |
| `+=`     | `x = x + value`  |
| `-=`     | `x = x - value`  |
| `*=`     | `x = x * value`  |
| `/=`     | `x = x / value`  |
| `//=`    | `x = x // value` |
| `%=`     | `x = x % value`  |
| `**=`    | `x = x ** value` |

### Benefits

* Reduces code length
* Improves readability
* Makes updates easier

---

# 4. Comparison Operators

Comparison operators compare two values and always return a Boolean (`True` or `False`).

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Uses

* Age verification
* Login validation
* Result checking
* Eligibility checks

---

# 5. Logical Operators

Logical operators combine multiple conditions.

Python has only **three logical operators**.

## AND (`and`)

Returns `True` only if **all conditions are True**.

Example:

* Adult and salary above ₹30,000
* Username and password both correct

---

## OR (`or`)

Returns `True` if **at least one condition is True**.

Example:

* Eligible through marks OR sports quota
* Cash payment OR online payment

---

## NOT (`not`)

Reverses the Boolean value.

Example:

* `True` becomes `False`
* `False` becomes `True`

### Truth Table

**AND**

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | False  |
| False | True  | False  |
| False | False | False  |

**OR**

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

**NOT**

| A     | Result |
| ----- | ------ |
| True  | False  |
| False | True   |

---

# 6. Membership Operators

Membership operators check whether an element exists inside a collection such as a list, tuple, string, or set.

Python has two membership operators.

| Operator | Meaning                                   |
| -------- | ----------------------------------------- |
| `in`     | Returns `True` if the item exists         |
| `not in` | Returns `True` if the item does not exist |

### Uses

* Search operations
* Menu validation
* Checking available products
* User permissions

---

# 7. Identity Operators

Identity operators compare whether two variables refer to the **same object in memory**, not whether they contain the same value.

Python has two identity operators.

| Operator | Meaning                     |
| -------- | --------------------------- |
| `is`     | Same object in memory       |
| `is not` | Different objects in memory |

### Difference Between `==` and `is`

`==`

* Compares values
* Most commonly used

`is`

* Compares object identity (memory reference)
* Commonly used with `None` and object identity checks

---

# 8. Operator Precedence

Operator precedence determines the order in which Python evaluates an expression.

Python follows a predefined priority order.

Highest to Lowest:

1. Parentheses `()`
2. Exponent `**`
3. Unary `+`, `-`
4. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
5. Addition `+`, Subtraction `-`
6. Comparison Operators
7. `not`
8. `and`
9. `or`

### Example

Expression:

`10 + 5 * 2`

Python first performs multiplication.

Result:

`10 + 10 = 20`

If parentheses are used:

`(10 + 5) * 2`

Result:

`15 × 2 = 30`

### Memory Trick

**P E M A C N A O**

* **P** → Parentheses
* **E** → Exponent
* **M** → Multiplication / Division / Modulus
* **A** → Addition / Subtraction
* **C** → Comparison
* **N** → Not
* **A** → And
* **O** → Or

---

# 9. Real-Life Uses of Operators

### Arithmetic

* Restaurant billing
* Shopping carts
* Banking
* Salary systems

### Assignment

* Updating account balance
* Increasing scores
* Decreasing stock

### Comparison

* Login validation
* Age verification
* Pass or fail

### Logical

* Loan approval
* Admission eligibility
* Employee verification

### Membership

* Product search
* Language availability
* User role checking

### Identity

* Object comparison
* Checking `None`
* Memory reference validation

---

# Interview Questions

## What is an operator?

An operator is a symbol or keyword that performs an operation on one or more operands.

---

## How many arithmetic operators are there in Python?

Seven:

* Addition
* Subtraction
* Multiplication
* Division
* Floor Division
* Modulus
* Exponent

---

## What do comparison operators return?

Comparison operators always return a Boolean value (`True` or `False`).

---

## How many logical operators are there?

Three:

* `and`
* `or`
* `not`

---

## Difference between `==` and `is`

`==` compares values.

`is` compares whether two variables refer to the same object in memory.

---

## Difference between `=` and `==`

`=` assigns a value to a variable.

`==` compares two values.

---

## What is operator precedence?

Operator precedence is the order in which Python evaluates operators in an expression.

---

# Key Takeaways

* Operators perform operations on values.
* Arithmetic operators are used for calculations.
* Assignment operators update variable values.
* Comparison operators return Boolean results.
* Logical operators combine conditions.
* Membership operators check whether an item exists in a collection.
* Identity operators compare object identity, not just values.
* Parentheses have the highest precedence and should be used to make expressions clear.

# 📘 Day 12 Notes – Python Modules & Packages

## What is a Module?
A module is a Python (.py) file containing reusable code.

## Why Modules are Used
- Reusability
- Better organization
- Easy maintenance
- Readability

## Advantages
- Modular code
- Faster development
- Easy collaboration

## Import Methods
- import math
- import math as m
- from math import sqrt
- from math import * (generally avoid)

## math Module
sqrt(), pow(), factorial(), ceil(), floor(), gcd(), pi, e.

## random Module
randint(), random(), uniform(), choice(), sample(), shuffle().

## datetime Module
date.today(), datetime.now(), strftime(), timedelta().

## Custom Modules
Create your own .py file and import it.

## Packages
A package is a folder containing related modules.

## if __name__ == '__main__'
Runs code only when the file is executed directly.

## Common Mistakes
- Forgetting imports
- Naming files math.py/random.py
- Using wildcard imports

## Interview Questions
1. What is a module?
A reusable Python file.
2. What is a package?
A folder containing modules.
3. Module vs Package?
Module=file, Package=folder.
4. import math vs from math import sqrt?
First uses math.sqrt(); second uses sqrt().
5. Why avoid from module import *?
Namespace pollution.
6. What is __name__?
Special execution variable.
7. Purpose of if __name__ == '__main__'?
Run only when executed directly.
8. How create your own module?
Create a .py file and import it.

## Key Takeaways
- Use modules to organize code.
- Packages group modules.
- Prefer explicit imports.

## Revision Summary
Modules, Packages, Imports, math, random, datetime, custom modules, __main__.
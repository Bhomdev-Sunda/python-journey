# ==========================================================
#           **kwargs Unpacking - Day 20
# ==========================================================

"""
Day 20 - **kwargs Unpacking

Topics Covered:
1. What is dictionary unpacking?
2. ** with function calls
3. Passing dictionaries as keyword arguments
4. Combining dictionaries
5. Adding and overriding dictionary values
6. **kwargs collecting vs ** unpacking
7. Dictionary merging
8. Practical examples
9. Common mistakes
10. Interview questions
"""

print("=" * 70)
print("               **kwargs UNPACKING")
print("=" * 70)


# ==========================================================
# 1. WHAT IS ** UNPACKING?
# ==========================================================

print("\n" + "=" * 70)
print("1. WHAT IS ** UNPACKING?")
print("=" * 70)

"""
** is used to unpack a dictionary.

A dictionary stores data as:

{
    key: value
}

Using ** expands the dictionary into
separate keyword arguments.
"""

user = {
    "name": "Bhomdev",
    "age": 22,
    "city": "Punjab"
}

print("Dictionary:", user)


# ==========================================================
# 2. BASIC DICTIONARY UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("2. BASIC DICTIONARY UNPACKING")
print("=" * 70)


def introduce(name, age, city):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


user = {
    "name": "Bhomdev",
    "age": 22,
    "city": "Punjab"
}

introduce(**user)


# ==========================================================
# 3. WITHOUT ** UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("3. WITHOUT ** UNPACKING")
print("=" * 70)

print("""
If a function expects separate keyword arguments:

def introduce(name, age, city):
    pass

And we have:

user = {
    "name": "Bhomdev",
    "age": 22,
    "city": "Punjab"
}

We use:

introduce(**user)

Python converts it conceptually into:

introduce(
    name="Bhomdev",
    age=22,
    city="Punjab"
)
""")


# ==========================================================
# 4. **kwargs COLLECTING vs ** UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("4. **kwargs COLLECTING vs ** UNPACKING")
print("=" * 70)


def show_details(**kwargs):

    print("Collected kwargs:", kwargs)


print("Collecting keyword arguments:")

show_details(
    name="Bhomdev",
    role="Python Developer"
)

print("\nUnpacking a dictionary:")

data = {
    "name": "Bhomdev",
    "role": "Python Developer"
}

show_details(**data)


# ==========================================================
# 5. PASSING A DICTIONARY TO A FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("5. PASSING A DICTIONARY TO A FUNCTION")
print("=" * 70)


def student(name, age, course):

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_data = {
    "name": "Bhomdev",
    "age": 22,
    "course": "BCA"
}

student(**student_data)


# ==========================================================
# 6. ORDER DOES NOT MATTER
# ==========================================================

print("\n" + "=" * 70)
print("6. ORDER OF DICTIONARY KEYS")
print("=" * 70)


def profile(name, age, city):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


data = {
    "city": "Punjab",
    "name": "Bhomdev",
    "age": 22
}

profile(**data)


# ==========================================================
# 7. UNPACKING WITH NORMAL KEYWORD ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("7. UNPACKING WITH NORMAL KEYWORD ARGUMENTS")
print("=" * 70)


def employee(name, age, role, city):

    print("Name:", name)
    print("Age:", age)
    print("Role:", role)
    print("City:", city)


employee_data = {
    "age": 22,
    "role": "Python Developer"
}

employee(
    name="Bhomdev",
    city="Punjab",
    **employee_data
)


# ==========================================================
# 8. COMBINE TWO DICTIONARIES
# ==========================================================

print("\n" + "=" * 70)
print("8. COMBINE TWO DICTIONARIES")
print("=" * 70)


personal_info = {
    "name": "Bhomdev",
    "age": 22
}

professional_info = {
    "role": "Python Developer",
    "experience": "Fresher"
}

combined = {
    **personal_info,
    **professional_info
}

print("Personal:", personal_info)
print("Professional:", professional_info)
print("Combined:", combined)


# ==========================================================
# 9. COMBINE MULTIPLE DICTIONARIES
# ==========================================================

print("\n" + "=" * 70)
print("9. COMBINE MULTIPLE DICTIONARIES")
print("=" * 70)


basic_info = {
    "name": "Bhomdev"
}

education = {
    "degree": "BCA"
}

skills = {
    "skill": "Python"
}

profile_data = {
    **basic_info,
    **education,
    **skills
}

print(profile_data)


# ==========================================================
# 10. ADD NEW VALUES WHILE UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("10. ADD NEW VALUES")
print("=" * 70)


user = {
    "name": "Bhomdev",
    "age": 22
}

updated_user = {
    **user,
    "city": "Punjab",
    "role": "Developer"
}

print("Original:", user)
print("Updated:", updated_user)


# ==========================================================
# 11. OVERRIDE EXISTING VALUES
# ==========================================================

print("\n" + "=" * 70)
print("11. OVERRIDE EXISTING VALUES")
print("=" * 70)


user = {
    "name": "Bhomdev",
    "age": 22,
    "role": "Student"
}

updated_user = {
    **user,
    "role": "Python Developer"
}

print("Original:", user)
print("Updated:", updated_user)


# ==========================================================
# 12. DICTIONARY MERGE PRIORITY
# ==========================================================

print("\n" + "=" * 70)
print("12. DICTIONARY MERGE PRIORITY")
print("=" * 70)


first = {
    "name": "Bhomdev",
    "role": "Student"
}

second = {
    "role": "Developer",
    "city": "Punjab"
}

merged = {
    **first,
    **second
}

print("First:", first)
print("Second:", second)
print("Merged:", merged)

print("\nWhen duplicate keys exist, the later value wins.")


# ==========================================================
# 13. COPY A DICTIONARY USING **
# ==========================================================

print("\n" + "=" * 70)
print("13. COPY A DICTIONARY")
print("=" * 70)


original = {
    "name": "Bhomdev",
    "skill": "Python"
}

copy = {
    **original
}

print("Original:", original)
print("Copy:", copy)
print("Same object:", original is copy)


# ==========================================================
# 14. API CONFIGURATION EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("14. API CONFIGURATION")
print("=" * 70)


def api_request(method, url, timeout, authentication):

    print("Method:", method)
    print("URL:", url)
    print("Timeout:", timeout)
    print("Authentication:", authentication)


config = {
    "method": "GET",
    "url": "/users",
    "timeout": 30,
    "authentication": True
}

api_request(**config)


# ==========================================================
# 15. USER SETTINGS EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("15. USER SETTINGS")
print("=" * 70)


default_settings = {
    "theme": "light",
    "language": "English",
    "notifications": True
}

user_settings = {
    "theme": "dark",
    "notifications": False
}

final_settings = {
    **default_settings,
    **user_settings
}

print("Default Settings:", default_settings)
print("User Settings:", user_settings)
print("Final Settings:", final_settings)


# ==========================================================
# 16. DATABASE CONFIGURATION EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("16. DATABASE CONFIGURATION")
print("=" * 70)


database_config = {
    "host": "localhost",
    "port": 5432
}

credentials = {
    "username": "admin",
    "password": "password123"
}

config = {
    **database_config,
    **credentials
}

print("Database Configuration:")

for key, value in config.items():

    print(f"{key}: {value}")


# ==========================================================
# 17. FUNCTION WITH DEFAULT VALUES
# ==========================================================

print("\n" + "=" * 70)
print("17. FUNCTION WITH DEFAULT VALUES")
print("=" * 70)


def create_user(name, age=18, city="Unknown"):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


user_data = {
    "name": "Bhomdev",
    "city": "Punjab"
}

create_user(**user_data)


# ==========================================================
# 18. MIXED DATA + ** UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("18. MIXED DATA + ** UNPACKING")
print("=" * 70)


def show_product(name, price, category, stock):

    print("Name:", name)
    print("Price:", price)
    print("Category:", category)
    print("Stock:", stock)


product_data = {
    "category": "Electronics",
    "stock": 10
}

show_product(
    name="Keyboard",
    price=1500,
    **product_data
)


# ==========================================================
# 19. PRACTICAL STUDENT EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("19. PRACTICAL STUDENT EXAMPLE")
print("=" * 70)


def create_student(name, age, course, skill):

    print("\nStudent Information")
    print("-" * 30)

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("Skill:", skill)


student_data = {
    "name": "Bhomdev",
    "age": 22,
    "course": "BCA",
    "skill": "Python"
}

create_student(**student_data)


# ==========================================================
# 20. PRACTICAL CONFIGURATION MERGE
# ==========================================================

print("\n" + "=" * 70)
print("20. PRACTICAL CONFIGURATION MERGE")
print("=" * 70)


default_config = {
    "debug": False,
    "port": 8000,
    "host": "localhost"
}

production_config = {
    "debug": False,
    "port": 8080
}

final_config = {
    **default_config,
    **production_config
}

print("Final Configuration:")

for key, value in final_config.items():

    print(f"{key}: {value}")


# ==========================================================
# 21. UNPACKING MULTIPLE DICTIONARIES
# ==========================================================

print("\n" + "=" * 70)
print("21. UNPACKING MULTIPLE DICTIONARIES")
print("=" * 70)


dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4
}

dict3 = {
    "e": 5,
    "f": 6
}

combined = {
    **dict1,
    **dict2,
    **dict3
}

print(combined)


# ==========================================================
# 22. IMPORTANT DIFFERENCE
# ==========================================================

print("\n" + "=" * 70)
print("22. IMPORTANT DIFFERENCE")
print("=" * 70)

print("""
**kwargs:

def function(**kwargs):
    pass

Here **kwargs COLLECTS keyword arguments.

Example:

function(name="Bhomdev", age=22)

kwargs becomes:

{
    "name": "Bhomdev",
    "age": 22
}


** Unpacking:

data = {
    "name": "Bhomdev",
    "age": 22
}

function(**data)

Python conceptually converts it into:

function(
    name="Bhomdev",
    age=22
)
""")


# ==========================================================
# 23. * vs **
# ==========================================================

print("\n" + "=" * 70)
print("23. * vs **")
print("=" * 70)

print("""
*  -> Positional argument unpacking
** -> Keyword argument unpacking

Example:

numbers = [10, 20, 30]

function(*numbers)


data = {
    "name": "Bhomdev",
    "age": 22
}

function(**data)
""")


# ==========================================================
# 24. COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("24. COMMON MISTAKES")
print("=" * 70)

print("❌ Confusing **kwargs with ** unpacking.")
print("❌ Using * instead of ** for keyword arguments.")
print("❌ Dictionary keys not matching function parameter names.")
print("❌ Passing duplicate keyword arguments.")
print("❌ Forgetting that later dictionary values override earlier values.")
print("❌ Trying to unpack a non-dictionary using **.")


# ==========================================================
# 25. BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("25. BEST PRACTICES")
print("=" * 70)

print("✔ Use ** to unpack dictionaries into keyword arguments.")
print("✔ Ensure dictionary keys match parameter names.")
print("✔ Use ** for clean dictionary merging.")
print("✔ Be careful with duplicate keys.")
print("✔ Remember that later values override earlier values.")
print("✔ Use configuration dictionaries for flexible settings.")


# ==========================================================
# 26. INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("26. INTERVIEW QUESTIONS")
print("=" * 70)


questions = [

    "What is dictionary unpacking?",

    "What does ** do in a function call?",

    "What is the difference between **kwargs and ** unpacking?",

    "Can a dictionary be unpacked into a function?",

    "What happens if dictionary keys do not match parameter names?",

    "What happens when dictionaries have duplicate keys during merging?",

    "How can multiple dictionaries be combined using **?",

    "What is the difference between * and **?",

    "How do you override values while copying a dictionary?"

]


for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")


# ==========================================================
# 27. SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("27. SUMMARY")
print("=" * 70)

print("✔ ** is used for dictionary unpacking.")

print("✔ **kwargs collects keyword arguments.")

print("✔ **data expands dictionary values into keyword arguments.")

print("✔ Dictionary keys should match function parameter names.")

print("✔ ** can combine multiple dictionaries.")

print("✔ Later dictionary values override earlier duplicate keys.")

print("✔ ** is commonly used for configuration and API data.")


print("\n" + "=" * 70)
print("       End of 04_kwargs_unpacking.py")
print("=" * 70)
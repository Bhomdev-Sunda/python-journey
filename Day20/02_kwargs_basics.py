# ==========================================================
#              **kwargs Basics - Day 20
# ==========================================================

"""
Day 20 - **kwargs Basics

Topics Covered:
1. Positional vs keyword arguments
2. What is **kwargs?
3. kwargs is a dictionary
4. Accessing keys and values
5. Looping through kwargs
6. Using kwargs with normal parameters
7. Practical examples
8. **kwargs with dictionaries
9. Common mistakes
10. Interview questions
"""

print("=" * 70)
print("                **kwargs BASICS")
print("=" * 70)


# ==========================================================
# 1. NORMAL KEYWORD ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("1. NORMAL KEYWORD ARGUMENTS")
print("=" * 70)


def introduce(name, age, city):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


introduce(
    name="Bhomdev",
    age=22,
    city="Punjab"
)


# ==========================================================
# 2. WHAT IS **kwargs?
# ==========================================================

print("\n" + "=" * 70)
print("2. WHAT IS **kwargs?")
print("=" * 70)

"""
**kwargs allows a function to accept
any number of keyword arguments.

Inside the function, kwargs is stored
as a dictionary.
"""


def show_details(**kwargs):

    print("kwargs:", kwargs)

    print("Type:", type(kwargs))


show_details(
    name="Bhomdev",
    age=22,
    role="Python Developer"
)


# ==========================================================
# 3. kwargs IS A DICTIONARY
# ==========================================================

print("\n" + "=" * 70)
print("3. kwargs IS A DICTIONARY")
print("=" * 70)


def check_kwargs(**kwargs):

    print("Value:", kwargs)

    print("Type:", type(kwargs))

    print("Length:", len(kwargs))


check_kwargs(
    language="Python",
    database="PostgreSQL",
    framework="FastAPI"
)


# ==========================================================
# 4. ACCESSING VALUES USING KEYS
# ==========================================================

print("\n" + "=" * 70)
print("4. ACCESSING VALUES")
print("=" * 70)


def profile(**kwargs):

    print("Name:", kwargs["name"])

    print("Age:", kwargs["age"])

    print("Role:", kwargs["role"])


profile(
    name="Bhomdev",
    age=22,
    role="AI Engineer"
)


# ==========================================================
# 5. USING get()
# ==========================================================

print("\n" + "=" * 70)
print("5. USING get()")
print("=" * 70)


def user_profile(**kwargs):

    name = kwargs.get("name", "Unknown")

    city = kwargs.get("city", "Unknown")

    role = kwargs.get("role", "Not specified")

    print("Name:", name)

    print("City:", city)

    print("Role:", role)


user_profile(
    name="Bhomdev",
    city="Punjab"
)


# ==========================================================
# 6. LOOP THROUGH kwargs
# ==========================================================

print("\n" + "=" * 70)
print("6. LOOP THROUGH kwargs")
print("=" * 70)


def display_details(**kwargs):

    for key, value in kwargs.items():

        print(key, ":", value)


display_details(
    name="Bhomdev",
    age=22,
    language="Python",
    experience="Fresher"
)


# ==========================================================
# 7. LOOP THROUGH KEYS
# ==========================================================

print("\n" + "=" * 70)
print("7. LOOP THROUGH KEYS")
print("=" * 70)


def show_keys(**kwargs):

    for key in kwargs:

        print("Key:", key)


show_keys(
    name="Bhomdev",
    age=22,
    city="Punjab"
)


# ==========================================================
# 8. LOOP THROUGH VALUES
# ==========================================================

print("\n" + "=" * 70)
print("8. LOOP THROUGH VALUES")
print("=" * 70)


def show_values(**kwargs):

    for value in kwargs.values():

        print("Value:", value)


show_values(
    name="Bhomdev",
    age=22,
    city="Punjab"
)


# ==========================================================
# 9. NORMAL PARAMETER + **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("9. NORMAL PARAMETER + **kwargs")
print("=" * 70)


def employee(name, **details):

    print("Name:", name)

    print("Additional Details:")

    for key, value in details.items():

        print(f"{key}: {value}")


employee(
    "Bhomdev",
    age=22,
    role="Python Developer",
    skills="Python, SQL, FastAPI"
)


# ==========================================================
# 10. **kwargs WITH DEFAULT DATA
# ==========================================================

print("\n" + "=" * 70)
print("10. DEFAULT DATA")
print("=" * 70)


def settings(**kwargs):

    theme = kwargs.get("theme", "light")

    language = kwargs.get("language", "English")

    notifications = kwargs.get("notifications", True)

    print("Theme:", theme)

    print("Language:", language)

    print("Notifications:", notifications)


settings(
    theme="dark",
    language="English"
)


# ==========================================================
# 11. COUNT KEYWORD ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("11. COUNT KEYWORD ARGUMENTS")
print("=" * 70)


def count_details(**kwargs):

    print("Number of details:", len(kwargs))


count_details(
    name="Bhomdev",
    age=22,
    city="Punjab",
    role="Developer"
)


# ==========================================================
# 12. CALCULATOR USING **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("12. CALCULATOR USING **kwargs")
print("=" * 70)


def calculator(**kwargs):

    number1 = kwargs.get("number1", 0)

    number2 = kwargs.get("number2", 0)

    operation = kwargs.get("operation", "add")

    if operation == "add":

        result = number1 + number2

    elif operation == "subtract":

        result = number1 - number2

    elif operation == "multiply":

        result = number1 * number2

    elif operation == "divide":

        if number2 == 0:

            print("Cannot divide by zero.")

            return

        result = number1 / number2

    else:

        print("Invalid operation.")

        return

    print("Result:", result)


calculator(
    number1=20,
    number2=10,
    operation="add"
)

calculator(
    number1=20,
    number2=10,
    operation="multiply"
)

calculator(
    number1=20,
    number2=10,
    operation="divide"
)


# ==========================================================
# 13. STUDENT INFORMATION
# ==========================================================

print("\n" + "=" * 70)
print("13. STUDENT INFORMATION")
print("=" * 70)


def student_info(**student):

    print("Student Information:")

    for key, value in student.items():

        print(f"{key.title()}: {value}")


student_info(
    name="Bhomdev",
    age=22,
    course="BCA",
    skill="Python",
    goal="AI Engineer"
)


# ==========================================================
# 14. SHOPPING CART USING **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("14. SHOPPING CART")
print("=" * 70)


def shopping_cart(**items):

    total = 0

    for item, price in items.items():

        print(f"{item}: ₹{price}")

        total += price

    print("Total:", total)


shopping_cart(
    laptop=55000,
    mouse=800,
    keyboard=1500
)


# ==========================================================
# 15. USER PROFILE
# ==========================================================

print("\n" + "=" * 70)
print("15. USER PROFILE")
print("=" * 70)


def create_profile(**profile):

    print("\n--- USER PROFILE ---")

    for key, value in profile.items():

        print(f"{key.title()}: {value}")


create_profile(
    name="Bhomdev",
    age=22,
    location="Punjab",
    profession="Python Developer",
    experience="Fresher"
)


# ==========================================================
# 16. DICTIONARY AS **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("16. DICTIONARY WITH **kwargs")
print("=" * 70)


user = {

    "name": "Bhomdev",

    "age": 22,

    "city": "Punjab"

}


def display_user(**kwargs):

    print(kwargs)


display_user(**user)


# ==========================================================
# 17. MODIFY kwargs
# ==========================================================

print("\n" + "=" * 70)
print("17. MODIFY kwargs")
print("=" * 70)


def modify_data(**kwargs):

    kwargs["status"] = "Active"

    print(kwargs)


modify_data(
    name="Bhomdev",
    role="Developer"
)


# ==========================================================
# 18. RETURN kwargs
# ==========================================================

print("\n" + "=" * 70)
print("18. RETURN kwargs")
print("=" * 70)


def create_data(**kwargs):

    return kwargs


data = create_data(
    name="Bhomdev",
    age=22,
    skill="Python"
)

print(data)


# ==========================================================
# 19. REAL-LIFE APPLICATION
# ==========================================================

print("\n" + "=" * 70)
print("19. REAL-LIFE APPLICATION")
print("=" * 70)


def api_request(**options):

    print("API Request Configuration:")

    for key, value in options.items():

        print(f"{key}: {value}")


api_request(
    method="GET",
    url="/users",
    timeout=30,
    authentication=True
)


# ==========================================================
# 20. IMPORTANT RULE
# ==========================================================

print("\n" + "=" * 70)
print("20. IMPORTANT RULE")
print("=" * 70)

print("""
**kwargs collects EXTRA KEYWORD arguments.

Example:

def function(name, **kwargs):
    pass

name -> normal parameter
kwargs -> remaining keyword arguments
""")


# ==========================================================
# 21. COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("21. COMMON MISTAKES")
print("=" * 70)

print("❌ Thinking kwargs is a tuple.")
print("❌ Forgetting that kwargs is a dictionary.")
print("❌ Confusing **kwargs with dictionary unpacking.")
print("❌ Accessing a missing key without checking.")
print("❌ Using **kwargs when fixed parameters are enough.")
print("❌ Forgetting that **kwargs handles keyword arguments.")


# ==========================================================
# 22. BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("22. BEST PRACTICES")
print("=" * 70)

print("✔ Use **kwargs when keyword arguments are dynamic.")

print("✔ Remember that kwargs is a dictionary.")

print("✔ Use .get() when a key may not exist.")

print("✔ Use meaningful names for normal parameters.")

print("✔ Don't use **kwargs unnecessarily.")

print("✔ Use **kwargs for flexible configuration data.")


# ==========================================================
# 23. INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("23. INTERVIEW QUESTIONS")
print("=" * 70)


questions = [

    "What is **kwargs?",

    "What type of object is kwargs?",

    "Why do we use **kwargs?",

    "Can **kwargs accept zero arguments?",

    "Can normal parameters be used with **kwargs?",

    "What is the difference between **kwargs and dictionary unpacking?",

    "How do you access values inside kwargs?",

    "When should **kwargs be used?"

]


for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")


# ==========================================================
# 24. SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("24. SUMMARY")
print("=" * 70)

print("✔ **kwargs accepts variable keyword arguments.")

print("✔ kwargs is stored as a dictionary.")

print("✔ **kwargs can accept zero or many arguments.")

print("✔ Normal parameters can come before **kwargs.")

print("✔ kwargs supports key-value based data.")

print("✔ Dictionary unpacking uses **.")

print("✔ **kwargs is commonly used in decorators.")

print("\n" + "=" * 70)
print("       End of 02_kwargs_basics.py")
print("=" * 70)
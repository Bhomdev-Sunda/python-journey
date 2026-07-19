# ==========================================================
#        Python Modules & Packages Practice Project
# ==========================================================

import math
import random
import datetime
import statistics
import calendar

# ==========================================================
# FUNCTIONS
# ==========================================================

def line():
    print("=" * 70)


def welcome():
    line()
    print("        DAY 12 - MODULES & PACKAGES PRACTICE")
    line()


def calculate_circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print("\nCircle Information")
    print("-" * 40)
    print("Radius        :", radius)
    print("Area          :", round(area, 2))
    print("Circumference :", round(circumference, 2))


def random_lucky_number():
    lucky = random.randint(1, 100)
    print("\nYour Lucky Number :", lucky)


def random_password():

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    password = ""

    for _ in range(8):
        password += random.choice(characters)

    print("\nGenerated Password :", password)


def student_statistics(marks):

    print("\nStudent Statistics")
    print("-" * 40)

    print("Marks   :", marks)
    print("Highest :", max(marks))
    print("Lowest  :", min(marks))
    print("Average :", round(statistics.mean(marks), 2))


def show_date_time():

    now = datetime.datetime.now()

    print("\nCurrent Date & Time")
    print("-" * 40)

    print("Date :", now.strftime("%d-%m-%Y"))
    print("Time :", now.strftime("%I:%M:%S %p"))
    print("Day  :", now.strftime("%A"))


def show_calendar():

    year = datetime.datetime.now().year

    print("\nCalendar -", year)
    print("-" * 40)

    print(calendar.month(year, datetime.datetime.now().month))


def math_operations():

    number = 49

    print("\nMath Operations")
    print("-" * 40)

    print("Number        :", number)
    print("Square Root   :", math.sqrt(number))
    print("Power (5^3)   :", math.pow(5, 3))
    print("Factorial 6   :", math.factorial(6))
    print("Ceil(8.3)     :", math.ceil(8.3))
    print("Floor(8.9)    :", math.floor(8.9))
    print("Pi Value      :", math.pi)


# ==========================================================
# MAIN PROGRAM
# ==========================================================

welcome()

name = input("\nEnter Your Name : ")

print("\nWelcome,", name)

# ----------------------------------------------------------

radius = float(input("\nEnter Circle Radius : "))

calculate_circle(radius)

# ----------------------------------------------------------

math_operations()

# ----------------------------------------------------------

random_lucky_number()

random_password()

# ----------------------------------------------------------

marks = []

print("\nEnter Marks of 5 Subjects")

for i in range(1, 6):

    mark = int(input(f"Subject {i} : "))

    marks.append(mark)

student_statistics(marks)

# ----------------------------------------------------------

show_date_time()

show_calendar()

# ----------------------------------------------------------

line()

print("SUMMARY")

line()

print("✔ Imported multiple built-in modules.")
print("✔ Used math module.")
print("✔ Used random module.")
print("✔ Used datetime module.")
print("✔ Used statistics module.")
print("✔ Used calendar module.")
print("✔ Created reusable functions.")
print("✔ Built a meaningful practice project.")

line()

print("Program Completed Successfully.")

line()
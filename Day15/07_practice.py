print("=" * 60)
print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
print("=" * 60)


class Student:

    # Constructor
    def __init__(self, roll_no, name, age, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    # Display student details
    def display(self):
        print("-" * 40)
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)
        print("Marks   :", self.marks)

    # Grade Calculation
    def grade(self):

        if self.marks >= 90:
            return "A+"

        elif self.marks >= 80:
            return "A"

        elif self.marks >= 70:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 50:
            return "D"

        else:
            return "Fail"

    # Pass or Fail
    def result(self):

        if self.marks >= 40:
            return "PASS"

        return "FAIL"

    # Scholarship Eligibility
    def scholarship(self):

        if self.marks >= 90:
            return "Eligible"

        return "Not Eligible"

    # Update Marks
    def update_marks(self, new_marks):

        self.marks = new_marks

        print("Marks Updated Successfully!")

    # Student Summary
    def summary(self):

        print("\nStudent Summary")
        print("-" * 40)
        print("Name          :", self.name)
        print("Grade         :", self.grade())
        print("Result        :", self.result())
        print("Scholarship   :", self.scholarship())


# ==================================================
# Creating Objects
# ==================================================

student1 = Student(101, "Bhomdev", 22, "Python", 95)

student2 = Student(102, "Rahul", 21, "AI", 76)

student3 = Student(103, "Aman", 20, "Data Science", 58)

students = [student1, student2, student3]


# ==================================================
# Display All Students
# ==================================================

print("\nALL STUDENTS")

for student in students:
    student.display()


# ==================================================
# Student Reports
# ==================================================

print("\nGENERATING REPORTS")

for student in students:
    student.summary()


# ==================================================
# Update Marks
# ==================================================

print("\nUPDATING MARKS")

student2.update_marks(88)

student2.summary()


# ==================================================
# Object Identity
# ==================================================

print("\nOBJECT IDENTITY")

print(student1 is student2)

print(id(student1))
print(id(student2))


# ==================================================
# __dict__
# ==================================================

print("\nOBJECT DATA")

print(student1.__dict__)

print(student2.__dict__)


# ==================================================
# Dynamic Attribute
# ==================================================

print("\nADDING NEW ATTRIBUTE")

student1.city = "Delhi"

print(student1.city)

print(student1.__dict__)


# ==================================================
# hasattr()
# ==================================================

print("\nCHECKING ATTRIBUTES")

print(hasattr(student1, "name"))

print(hasattr(student1, "salary"))


# ==================================================
# getattr()
# ==================================================

print("\nUSING getattr()")

print(getattr(student1, "name"))

print(getattr(student1, "course"))

print(getattr(student1, "salary", "Attribute Not Found"))


# ==================================================
# setattr()
# ==================================================

print("\nUSING setattr()")

setattr(student1, "college", "ABC College")

print(student1.college)


# ==================================================
# delattr()
# ==================================================

print("\nUSING delattr()")

print(hasattr(student1, "city"))

delattr(student1, "city")

print(hasattr(student1, "city"))


# ==================================================
# Final Report
# ==================================================

print("\nFINAL REPORT")

for student in students:

    print("-" * 40)

    print("Name         :", student.name)

    print("Course       :", student.course)

    print("Marks        :", student.marks)

    print("Grade        :", student.grade())

    print("Result       :", student.result())

    print("Scholarship  :", student.scholarship())


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 60)
print("DAY 15 PRACTICE COMPLETED")
print("=" * 60)

print("""
Topics Practiced

✔ Class

✔ Object

✔ Attributes

✔ Methods

✔ self

✔ Constructor (__init__)

✔ Instance Variables

✔ Object Creation

✔ Multiple Objects

✔ hasattr()

✔ getattr()

✔ setattr()

✔ delattr()

✔ __dict__()

✔ id()

✔ Real-world Student Management System

Congratulations!
You have completed the Day 15 Practice Project.
""")

print("=" * 60)
print("END OF PROGRAM")
print("=" * 60)
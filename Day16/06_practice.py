#        (Encapsulation + Inheritance + Polymorphism
#         + Abstraction + super())

from abc import ABC, abstractmethod

print("=" * 70)
print("      EMPLOYEE MANAGEMENT SYSTEM USING OOP")
print("=" * 70)


# ==========================================================
# ABSTRACT CLASS
# ==========================================================

class Employee(ABC):

    company = "OpenAI Pvt. Ltd."

    def __init__(self, emp_id, name, salary):

        self.emp_id = emp_id

        self.name = name

        self.__salary = salary

    # Getter
    def get_salary(self):

        return self.__salary

    # Setter
    def set_salary(self, salary):

        if salary >= 0:

            self.__salary = salary

        else:

            print("Salary cannot be negative.")

    @abstractmethod
    def calculate_bonus(self):

        pass

    def show_details(self):

        print("-" * 60)
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      :", self.get_salary())
        print("Company     :", Employee.company)


# ==========================================================
# DEVELOPER CLASS
# ==========================================================

class Developer(Employee):

    def __init__(self, emp_id, name, salary, language):

        super().__init__(emp_id, name, salary)

        self.language = language

    def calculate_bonus(self):

        return self.get_salary() * 0.20

    def show_details(self):

        super().show_details()

        print("Role        : Developer")
        print("Language    :", self.language)
        print(f"Bonus       : ₹{self.calculate_bonus():,.2f}")


# ==========================================================
# MANAGER CLASS
# ==========================================================

class Manager(Employee):

    def __init__(self, emp_id, name, salary, department):

        super().__init__(emp_id, name, salary)

        self.department = department

    def calculate_bonus(self):

        return self.get_salary() * 0.30

    def show_details(self):

        super().show_details()

        print("Role        : Manager")
        print("Department  :", self.department)
        print(f"Bonus       : ₹{self.calculate_bonus():,.2f}")


# ==========================================================
# INTERN CLASS
# ==========================================================

class Intern(Employee):

    def __init__(self, emp_id, name, salary, duration):

        super().__init__(emp_id, name, salary)

        self.duration = duration

    def calculate_bonus(self):

        return self.get_salary() * 0.05

    def show_details(self):

        super().show_details()

        print("Role        : Intern")
        print("Duration    :", self.duration)
        print(f"Bonus       : ₹{self.calculate_bonus():,.2f}")


# ==========================================================
# EMPLOYEE DATABASE
# ==========================================================

employees = []


# ==========================================================
# MENU
# ==========================================================

while True:

    print("\n" + "=" * 70)
    print("1. Add Developer")
    print("2. Add Manager")
    print("3. Add Intern")
    print("4. View Employees")
    print("5. Update Salary")
    print("6. Exit")
    print("=" * 70)

    try:

        choice = int(input("Enter Choice : "))

    except ValueError:

        print("Please enter a valid number.")

        continue

    # ======================================================
    # ADD DEVELOPER
    # ======================================================

    if choice == 1:

        try:

            emp_id = int(input("Employee ID : "))
            name = input("Name : ")
            salary = float(input("Salary : "))
            language = input("Programming Language : ")

            developer = Developer(
                emp_id,
                name,
                salary,
                language
            )

            employees.append(developer)

            print("Developer Added Successfully.")

        except ValueError:

            print("Invalid Input.")

    # ======================================================
    # ADD MANAGER
    # ======================================================

    elif choice == 2:

        try:

            emp_id = int(input("Employee ID : "))
            name = input("Name : ")
            salary = float(input("Salary : "))
            department = input("Department : ")

            manager = Manager(
                emp_id,
                name,
                salary,
                department
            )

            employees.append(manager)

            print("Manager Added Successfully.")

        except ValueError:

            print("Invalid Input.")

    # ======================================================
    # ADD INTERN
    # ======================================================

    elif choice == 3:

        try:

            emp_id = int(input("Employee ID : "))
            name = input("Name : ")
            salary = float(input("Salary : "))
            duration = input("Internship Duration : ")

            intern = Intern(
                emp_id,
                name,
                salary,
                duration
            )

            employees.append(intern)

            print("Intern Added Successfully.")

        except ValueError:

            print("Invalid Input.")

    # ======================================================
    # VIEW EMPLOYEES
    # ======================================================

    elif choice == 4:

        if len(employees) == 0:

            print("No Employees Found.")

        else:

            print("\nEMPLOYEE RECORDS")

            for employee in employees:

                employee.show_details()

    # ======================================================
    # UPDATE SALARY
    # ======================================================

    elif choice == 5:

        try:

            emp_id = int(input("Employee ID : "))

            found = False

            for employee in employees:

                if employee.emp_id == emp_id:

                    new_salary = float(
                        input("New Salary : ")
                    )

                    employee.set_salary(new_salary)

                    print("Salary Updated Successfully.")

                    found = True

                    break

            if not found:

                print("Employee Not Found.")

        except ValueError:

            print("Invalid Input.")

    # ======================================================
    # EXIT
    # ======================================================

    elif choice == 6:

        print("\n" + "=" * 70)
        print("Thank You!")
        print("Day 16 Practice Completed Successfully.")
        print("=" * 70)

        break

    # ======================================================
    # INVALID OPTION
    # ======================================================

    else:

        print("Invalid Choice. Please Try Again.")

# ==========================================================
# END OF PROGRAM
# ==========================================================
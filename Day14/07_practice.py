# ==========================================================
#                 07_practice.py
#        Exception Handling Practice Project - Day 14
# ==========================================================

print("=" * 70)
print("         STUDENT MANAGEMENT SYSTEM")
print("     (Using Exception Handling)")
print("=" * 70)

students = {}


# ==========================================================
# MENU
# ==========================================================

while True:

    print("\n" + "=" * 70)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Calculate Percentage")
    print("6. Exit")
    print("=" * 70)

    try:

        choice = int(input("Enter Your Choice : "))

    except ValueError:

        print("Please enter a valid number.")

        continue

    # ======================================================
    # ADD STUDENT
    # ======================================================

    if choice == 1:

        print("\nADD STUDENT")
        print("-" * 70)

        try:

            roll = int(input("Enter Roll Number : "))

            if roll in students:

                raise ValueError("Roll Number already exists.")

            name = input("Enter Name : ").strip()

            if name == "":

                raise ValueError("Name cannot be empty.")

            marks = float(input("Enter Marks : "))

            if marks < 0 or marks > 100:

                raise ValueError("Marks must be between 0 and 100.")

            students[roll] = {

                "Name": name,

                "Marks": marks

            }

        except ValueError as error:

            print(error)

        else:

            print("Student Added Successfully.")

        finally:

            print("Add Student Operation Completed.")

    # ======================================================
    # VIEW STUDENTS
    # ======================================================

    elif choice == 2:

        print("\nSTUDENT RECORDS")
        print("-" * 70)

        if len(students) == 0:

            print("No Student Records Found.")

        else:

            print(f"{'Roll':<10}{'Name':<25}{'Marks'}")
            print("-" * 70)

            for roll, details in students.items():

                print(

                    f"{roll:<10}"

                    f"{details['Name']:<25}"

                    f"{details['Marks']}"

                )

    # ======================================================
    # SEARCH STUDENT
    # ======================================================

    elif choice == 3:

        print("\nSEARCH STUDENT")
        print("-" * 70)

        try:

            roll = int(input("Enter Roll Number : "))

            if roll not in students:

                raise KeyError("Student not found.")

            print("Name  :", students[roll]["Name"])
            print("Marks :", students[roll]["Marks"])

        except ValueError:

            print("Roll Number must be an integer.")

        except KeyError as error:

            print(error)

    # ======================================================
    # DELETE STUDENT
    # ======================================================

    elif choice == 4:

        print("\nDELETE STUDENT")
        print("-" * 70)

        try:

            roll = int(input("Enter Roll Number : "))

            if roll not in students:

                raise KeyError("Student does not exist.")

            del students[roll]

        except ValueError:

            print("Roll Number must be an integer.")

        except KeyError as error:

            print(error)

        else:

            print("Student Deleted Successfully.")

        finally:

            print("Delete Operation Completed.")

    # ======================================================
    # CALCULATE PERCENTAGE
    # ======================================================

    elif choice == 5:

        print("\nPERCENTAGE CALCULATOR")
        print("-" * 70)

        try:

            total = float(input("Enter Total Marks : "))
            obtained = float(input("Enter Obtained Marks : "))

            if total <= 0:

                raise ZeroDivisionError(
                    "Total Marks cannot be zero."
                )

            if obtained < 0 or obtained > total:

                raise ValueError(
                    "Obtained Marks are invalid."
                )

            percentage = (obtained / total) * 100

        except ZeroDivisionError as error:

            print(error)

        except ValueError as error:

            print(error)

        else:

            print(f"Percentage : {percentage:.2f}%")

        finally:

            print("Calculation Completed.")

    # ======================================================
    # EXIT
    # ======================================================

    elif choice == 6:

        print("\n" + "=" * 70)
        print("Thank You!")
        print("Day 14 Practice Completed Successfully.")
        print("=" * 70)

        break

    # ======================================================
    # INVALID OPTION
    # ======================================================

    else:

        print("Invalid Menu Choice!")

# ==========================================================
# END OF PROGRAM
# ==========================================================
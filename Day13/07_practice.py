# ==========================================================
#                 07_practice.py
#        Student File Management System - Day 13
# ==========================================================

print("=" * 70)
print("        STUDENT FILE MANAGEMENT SYSTEM")
print("=" * 70)

FILE_NAME = "Day13/students.txt"


# ==========================================================
# CREATE FILE IF NOT EXISTS
# ==========================================================

try:

    with open(FILE_NAME, "x") as file:

        pass

except FileExistsError:

    pass


# ==========================================================
# MENU
# ==========================================================

while True:

    print("\n" + "=" * 70)
    print("1. View All Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Count Students")
    print("5. File Information")
    print("6. Exit")
    print("=" * 70)

    choice = input("Enter Your Choice : ")

    # ======================================================
    # VIEW ALL STUDENTS
    # ======================================================

    if choice == "1":

        print("\nStudent Records")
        print("-" * 70)

        with open(FILE_NAME, "r") as file:

            data = file.read()

            if data.strip() == "":

                print("No Student Records Found.")

            else:

                print(data)

    # ======================================================
    # ADD STUDENT
    # ======================================================

    elif choice == "2":

        print("\nAdd Student")

        roll = input("Roll No : ")
        name = input("Name     : ")
        course = input("Course   : ")
        marks = input("Marks    : ")

        with open(FILE_NAME, "a") as file:

            file.write(f"{roll},{name},{course},{marks}\n")

            file.flush()

        print("\nStudent Added Successfully!")

    # ======================================================
    # SEARCH STUDENT
    # ======================================================

    elif choice == "3":

        search = input("\nEnter Student Name : ").lower()

        found = False

        with open(FILE_NAME, "r") as file:

            for line in file:

                if search in line.lower():

                    print("\nStudent Found")
                    print(line.strip())

                    found = True

        if not found:

            print("Student Not Found.")

    # ======================================================
    # COUNT STUDENTS
    # ======================================================

    elif choice == "4":

        with open(FILE_NAME, "r") as file:

            lines = file.readlines()

            print("\nTotal Students :", len(lines))

    # ======================================================
    # FILE INFORMATION
    # ======================================================

    elif choice == "5":

        with open(FILE_NAME, "r") as file:

            print("\nFile Information")
            print("-" * 40)

            print("File Name :", file.name)
            print("Mode      :", file.mode)
            print("Readable  :", file.readable())
            print("Writable  :", file.writable())

            print("\nCurrent Position :", file.tell())

            file.seek(0)

            print("After seek(0)    :", file.tell())

        print("Closed :", file.closed)

    # ======================================================
    # EXIT
    # ======================================================

    elif choice == "6":

        print("\nThank You!")
        print("Day 13 Practice Completed Successfully.")

        break

    # ======================================================
    # INVALID CHOICE
    # ======================================================

    else:

        print("\nInvalid Choice!")
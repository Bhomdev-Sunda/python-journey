#        EMPLOYEE INFORMATION MANAGEMENT SYSTEM

print("=" * 60)
print("\tEMPLOYEE INFORMATION MANAGEMENT SYSTEM")
print("=" * 60)

# Employee Details

emp_id = input("Enter Employee ID        : ")
emp_name = input("Enter Employee Name      : ")
age = int(input("Enter Age                : "))
gender = input("Enter Gender             : ")
department = input("Enter Department         : ")
designation = input("Enter Designation        : ")
company = input("Enter Company Name       : ")
city = input("Enter City               : ")
email = input("Enter Email              : ")
phone = input("Enter Phone Number       : ")
salary = float(input("Enter Salary             : "))

# Employee Report

print("\n" + "=" * 60)
print("\t\tEMPLOYEE REPORT")
print("=" * 60)

print(f"Employee ID      : {emp_id}")
print(f"Employee Name    : {emp_name}")
print(f"Age              : {age}")
print(f"Gender           : {gender}")
print(f"Department       : {department}")
print(f"Designation      : {designation}")
print(f"Company          : {company}")
print(f"City             : {city}")
print(f"Email            : {email}")
print(f"Phone            : {phone}")
print(f"Salary           : ₹{salary:.2f}")

# String Indexing

print("\n" + "-" * 60)
print("STRING INDEXING")
print("-" * 60)

print(f"First Letter of Name       : {emp_name[0]}")
print(f"Last Letter of Name        : {emp_name[-1]}")

print(f"First Letter of Company    : {company[0]}")
print(f"Last Letter of Company     : {company[-1]}")

print(f"First Letter of Department : {department[0]}")
print(f"Last Letter of Department  : {department[-1]}")

# String Slicing

print("\n" + "-" * 60)
print("STRING SLICING")
print("-" * 60)

print(f"First 3 Letters            : {emp_name[:3]}")
print(f"Last 3 Letters             : {emp_name[-3:]}")
print(f"First 5 Letters Company    : {company[:5]}")
print(f"Last 5 Letters Company     : {company[-5:]}")
print(f"Reverse Name               : {emp_name[::-1]}")
print(f"Every 2nd Character        : {emp_name[::2]}")
print(f"Every 3rd Character        : {emp_name[::3]}")
print(f"Without First Character    : {emp_name[1:]}")
print(f"Without Last Character     : {emp_name[:-1]}")

# String Methods

print("\n" + "-" * 60)
print("STRING METHODS")
print("-" * 60)

print(f"Upper Case                 : {emp_name.upper()}")
print(f"Lower Case                 : {emp_name.lower()}")
print(f"Title Case                 : {emp_name.title()}")
print(f"Capitalize                 : {emp_name.capitalize()}")
print(f"Swap Case                  : {emp_name.swapcase()}")

print(f"\nLength of Name             : {len(emp_name)}")
print(f"Length of Company          : {len(company)}")
print(f"Length of Department       : {len(department)}")

print(f"\nReplace Spaces             : {emp_name.replace(' ', '_')}")
print(f"Count of 'a'               : {emp_name.lower().count('a')}")
print(f"Count of Spaces            : {emp_name.count(' ')}")
print(f"Find 'a'                   : {emp_name.lower().find('a')}")

print(f"\nStarts with 'B'            : {emp_name.startswith('B')}")
print(f"Ends with 'a'              : {emp_name.endswith('a')}")

print(f"\nIs Alphabet Only           : {emp_name.isalpha()}")
print(f"Is Upper                   : {emp_name.isupper()}")
print(f"Is Lower                   : {emp_name.islower()}")
print(f"Is Title                   : {emp_name.istitle()}")

# Escape Sequences

print("\n" + "-" * 60)
print("ESCAPE SEQUENCES")
print("-" * 60)

print("New Line Example")
print(f"{emp_name}\n{company}")

print("\nTab Example")
print(f"Name\t:\t{emp_name}")

print("\nDouble Quotes")
print(f"\"{emp_name}\"")

print("\nBackslash")
print("C:\\Users\\Employee")

# String Concatenation

print("\n" + "-" * 60)
print("STRING CONCATENATION")
print("-" * 60)

message = "Welcome " + emp_name + " to " + company + "."

print(message)

# String Repetition

print("\n" + "-" * 60)
print("STRING REPETITION")
print("-" * 60)
print("*" * 40)
print("=" * 40)
print("-" * 40)

# Professional Employee Summary

print("\n" + "=" * 60)
print("\t\tFINAL EMPLOYEE SUMMARY")
print("=" * 60)

print(f"""
Employee ID        : {emp_id}
Employee Name      : {emp_name}
Age                : {age}
Gender             : {gender}
Department         : {department}
Designation        : {designation}
Company            : {company}
City               : {city}
Email              : {email}
Phone              : {phone}
Salary             : ₹{salary:.2f}

First Character    : {emp_name[0]}
Last Character     : {emp_name[-1]}

Reverse Name       : {emp_name[::-1]}

Upper Case         : {emp_name.upper()}
Lower Case         : {emp_name.lower()}
Title Case         : {emp_name.title()}

Length             : {len(emp_name)}

Company Starts With: {company[0]}
Company Ends With  : {company[-1]}
""")

print("=" * 60)
print("THANK YOU FOR USING EMPLOYEE INFORMATION SYSTEM")
print("=" * 60)
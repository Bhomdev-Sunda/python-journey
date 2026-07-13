#             IF ELIF ELSE STATEMENT IN PYTHON

print("=" * 60)
print("           EMPLOYEE PERFORMANCE SYSTEM")
print("=" * 60)

# Employee Details

employee_name = input("Enter Employee Name : ")
employee_score = int(input("Enter Performance Score (0-100) : "))

# If Elif Else Statement
if employee_score >= 90:
    print("\nPerformance Rating : Excellent")
    print(f"Congratulations, {employee_name}!")
    print("You are eligible for Promotion and Bonus.")

elif employee_score >= 75:
    print("\nPerformance Rating : Good")
    print(f"Well done, {employee_name}!")
    print("You are eligible for a Performance Bonus.")

elif employee_score >= 50:
    print("\nPerformance Rating : Average")
    print(f"Keep improving, {employee_name}.")
    print("You need to work on your performance.")

else:
    print("\nPerformance Rating : Poor")
    print(f"Sorry, {employee_name}.")
    print("Performance Improvement Plan Required.")

# End
print("\nThank You for Using Employee Performance System.")
print("=" * 60)
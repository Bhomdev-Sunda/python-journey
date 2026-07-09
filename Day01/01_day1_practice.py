# Print your name.
print("My name is Bhomdev.")

# Print your age.
print("My age is 22years.")

# Take two numbers and add them.
num1 = float(input("Enter 1st number :"))
num2 = float(input("Enter 2nd number :"))
sum = num1 + num2
print("The sum of these two numbers is = ", sum)

# Calculate the area of a rectangle.
length = float(input("Enter length of the rectangle :"))
width = float(input("Enter width of the rectangle :"))
area = length*width
print("area of the rectangle is: ", area)

# Swap two numbers.
dig1 = float(input("Enter first digit :"))
dig2 = float(input("Enter second digit :"))
dig1, dig2 = dig2, dig1
print("After swapping:")
print("First digit =", dig1)
print("Second digit =", dig2)

# Celsius to Fahrenheit converter.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

# Fahrenheit to Celsius converter.
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius =", celsius)

# Even or odd checker.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an Even number.")
else:
    print(number, "is an Odd number.")
# Largest of three numbers

numb1 = float(input("Enter first number: "))
numb2 = float(input("Enter second number: "))
numb3 = float(input("Enter third number: "))

if numb1 >= numb2 and numb1 >= numb3:
    print(numb1, "is the greatest")
elif numb2 >= numb1 and numb2 >= numb3:
    print(numb2, "is the greatest")
else:
    print(numb3, "is the greatest")

# Calculate simple interest.
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time (years): "))

si = (p * r * t) / 100
print(f"Simple Interest = {si}")
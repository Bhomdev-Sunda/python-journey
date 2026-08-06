print("=" * 70)
print("              POLYMORPHISM IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS POLYMORPHISM?
# ==========================================================

# Polymorphism means "Many Forms".
#
# The same method or function can perform
# different tasks depending on the object.

print("\nWHAT IS POLYMORPHISM?")
print("-" * 70)

print("Polymorphism means 'Many Forms'.")
print("One interface can have many implementations.")
print("The same method behaves differently for")
print("different objects.")

# ==========================================================
# WHY DO WE USE POLYMORPHISM?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE POLYMORPHISM?")
print("=" * 70)

print("1. Code Reusability")
print("2. Flexibility")
print("3. Easy Maintenance")
print("4. Cleaner Code")
print("5. Extensibility")

# ==========================================================
# SIMPLE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE POLYMORPHISM")
print("=" * 70)


class Dog:

    def sound(self):

        print("Dog says: Bark Bark")


class Cat:

    def sound(self):

        print("Cat says: Meow Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# ==========================================================
# METHOD OVERRIDING
# ==========================================================

print("\n" + "=" * 70)
print("2. METHOD OVERRIDING")
print("=" * 70)


class Animal:

    def speak(self):

        print("Animals make sounds.")


class Lion(Animal):

    def speak(self):

        print("Lion Roars")


class Cow(Animal):

    def speak(self):

        print("Cow Moos")


lion = Lion()
cow = Cow()

lion.speak()
cow.speak()

# ==========================================================
# POLYMORPHISM USING LOOP
# ==========================================================

print("\n" + "=" * 70)
print("3. POLYMORPHISM USING LOOP")
print("=" * 70)

animals = [Dog(), Cat(), Lion(), Cow()]

for animal in animals:

    animal.sound() if hasattr(animal, "sound") else animal.speak()

# ==========================================================
# BUILT-IN POLYMORPHISM
# ==========================================================

print("\n" + "=" * 70)
print("4. BUILT-IN POLYMORPHISM")
print("=" * 70)

print(len("Python"))
print(len([10, 20, 30, 40]))
print(len((1, 2, 3)))
print(len({"A": 1, "B": 2}))

# ==========================================================
# FUNCTION POLYMORPHISM
# ==========================================================

print("\n" + "=" * 70)
print("5. FUNCTION POLYMORPHISM")
print("=" * 70)


def display(item):

    print(item)


display("Python")
display(500)
display(25.5)
display([1, 2, 3])

# ==========================================================
# DUCK TYPING
# ==========================================================

print("\n" + "=" * 70)
print("6. DUCK TYPING")
print("=" * 70)


class Bird:

    def fly(self):

        print("Bird is Flying")


class Airplane:

    def fly(self):

        print("Airplane is Flying")


def start_flying(object_name):

    object_name.fly()


bird = Bird()
plane = Airplane()

start_flying(bird)
start_flying(plane)

# ==========================================================
# REAL-LIFE PAYMENT EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("7. PAYMENT SYSTEM")
print("=" * 70)


class UPI:

    def pay(self):

        print("Payment via UPI")


class CreditCard:

    def pay(self):

        print("Payment via Credit Card")


class Cash:

    def pay(self):

        print("Payment using Cash")


payments = [UPI(), CreditCard(), Cash()]

for payment in payments:

    payment.pay()

# ==========================================================
# SHAPE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("8. SHAPE EXAMPLE")
print("=" * 70)


class Circle:

    def area(self):

        print("Area = π × r²")


class Rectangle:

    def area(self):

        print("Area = Length × Width")


class Triangle:

    def area(self):

        print("Area = 1/2 × Base × Height")


shapes = [

    Circle(),

    Rectangle(),

    Triangle()

]

for shape in shapes:

    shape.area()

# ==========================================================
# OPERATOR POLYMORPHISM
# ==========================================================

print("\n" + "=" * 70)
print("9. OPERATOR POLYMORPHISM")
print("=" * 70)

print(5 + 10)

print("Hello " + "Python")

print([1, 2] + [3, 4])

# ==========================================================
# TYPE CHECKING
# ==========================================================

print("\n" + "=" * 70)
print("10. TYPE CHECKING")
print("=" * 70)

print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(lion, Animal))

# ==========================================================
# BENEFITS
# ==========================================================

print("\n" + "=" * 70)
print("BENEFITS OF POLYMORPHISM")
print("=" * 70)

benefits = [

    "Cleaner Code",

    "Easy Maintenance",

    "Flexible Programs",

    "Reusable Code",

    "Professional Design",

    "Easy Extension"

]

for item in benefits:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting method overriding.")
print("❌ Different method names.")
print("❌ Wrong indentation.")
print("❌ Confusing overloading with overriding.")
print("❌ Forgetting object creation.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use common method names.")
print("✔ Keep method behavior meaningful.")
print("✔ Override only when necessary.")
print("✔ Follow OOP principles.")
print("✔ Write readable code.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Payment Gateway",

    "Game Development",

    "Vehicle Management",

    "Drawing Software",

    "Banking Systems",

    "Hospital Management",

    "AI & Machine Learning",

    "GUI Applications"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Polymorphism means Many Forms.")
print("✔ Same method can behave differently.")
print("✔ Method overriding is the most common form.")
print("✔ Duck typing is supported in Python.")
print("✔ Built-in functions also show polymorphism.")
print("✔ Polymorphism improves flexibility and reuse.")

print("=" * 70)
print("End of 03_polymorphism.py")
print("=" * 70)
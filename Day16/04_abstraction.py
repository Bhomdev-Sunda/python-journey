from abc import ABC, abstractmethod

print("=" * 70)
print("               ABSTRACTION IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS ABSTRACTION?
# ==========================================================

# Abstraction means hiding the implementation details
# and showing only the essential features to the user.
#
# Example:
# You drive a car using the steering wheel,
# accelerator, and brakes.
# You don't need to know how the engine works internally.

print("\nWHAT IS ABSTRACTION?")
print("-" * 70)

print("Abstraction hides internal implementation.")
print("It exposes only the required functionality.")
print("Python provides abstraction using the abc module.")

# ==========================================================
# WHY DO WE USE ABSTRACTION?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE ABSTRACTION?")
print("=" * 70)

print("1. Hide unnecessary details")
print("2. Improve security")
print("3. Reduce complexity")
print("4. Standardize code")
print("5. Improve maintainability")

# ==========================================================
# ABSTRACT CLASS
# ==========================================================

print("\n" + "=" * 70)
print("1. ABSTRACT CLASS")
print("=" * 70)


class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass


print("Animal is an abstract class.")
print("Objects of Animal cannot be created.")

# ==========================================================
# IMPLEMENTING ABSTRACT METHOD
# ==========================================================

print("\n" + "=" * 70)
print("2. IMPLEMENTING ABSTRACT METHOD")
print("=" * 70)


class Dog(Animal):

    def sound(self):

        print("Dog says: Bark Bark")


class Cat(Animal):

    def sound(self):

        print("Cat says: Meow Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# ==========================================================
# MULTIPLE CHILD CLASSES
# ==========================================================

print("\n" + "=" * 70)
print("3. MULTIPLE CHILD CLASSES")
print("=" * 70)


class Bird(Animal):

    def sound(self):

        print("Bird says: Chirp Chirp")


bird = Bird()

bird.sound()

# ==========================================================
# ABSTRACT CLASS WITH NORMAL METHOD
# ==========================================================

print("\n" + "=" * 70)
print("4. ABSTRACT + NORMAL METHODS")
print("=" * 70)


class Vehicle(ABC):

    def start(self):

        print("Vehicle Started")

    @abstractmethod
    def fuel_type(self):

        pass


class Car(Vehicle):

    def fuel_type(self):

        print("Fuel Type : Petrol")


car = Car()

car.start()
car.fuel_type()

# ==========================================================
# BANK EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("5. BANK EXAMPLE")
print("=" * 70)


class Bank(ABC):

    @abstractmethod
    def interest_rate(self):

        pass


class SBI(Bank):

    def interest_rate(self):

        print("SBI Interest Rate : 6.5%")


class HDFC(Bank):

    def interest_rate(self):

        print("HDFC Interest Rate : 7%")


sbi = SBI()
hdfc = HDFC()

sbi.interest_rate()
hdfc.interest_rate()

# ==========================================================
# PAYMENT SYSTEM
# ==========================================================

print("\n" + "=" * 70)
print("6. PAYMENT SYSTEM")
print("=" * 70)


class Payment(ABC):

    @abstractmethod
    def pay(self):

        pass


class UPI(Payment):

    def pay(self):

        print("Payment through UPI")


class CreditCard(Payment):

    def pay(self):

        print("Payment through Credit Card")


class Cash(Payment):

    def pay(self):

        print("Payment using Cash")


payments = [

    UPI(),

    CreditCard(),

    Cash()

]

for payment in payments:

    payment.pay()

# ==========================================================
# SHAPE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("7. SHAPE EXAMPLE")
print("=" * 70)


class Shape(ABC):

    @abstractmethod
    def area(self):

        pass


class Circle(Shape):

    def area(self):

        print("Area = π × r²")


class Rectangle(Shape):

    def area(self):

        print("Area = Length × Width")


circle = Circle()
rectangle = Rectangle()

circle.area()
rectangle.area()

# ==========================================================
# CHECKING OBJECT TYPES
# ==========================================================

print("\n" + "=" * 70)
print("8. TYPE CHECKING")
print("=" * 70)

print(isinstance(circle, Shape))
print(isinstance(dog, Animal))
print(issubclass(Car, Vehicle))

# ==========================================================
# TRYING TO CREATE ABSTRACT OBJECT
# ==========================================================

print("\n" + "=" * 70)
print("9. ABSTRACT OBJECT")
print("=" * 70)

try:

    animal = Animal()

except TypeError as error:

    print(error)

# ==========================================================
# BENEFITS OF ABSTRACTION
# ==========================================================

print("\n" + "=" * 70)
print("BENEFITS OF ABSTRACTION")
print("=" * 70)

benefits = [

    "Hides Complexity",

    "Improves Security",

    "Cleaner Code",

    "Better Maintainability",

    "Standardized Design",

    "Professional Development"

]

for item in benefits:

    print("✔", item)

# ==========================================================
# ABSTRACT CLASS RULES
# ==========================================================

print("\n" + "=" * 70)
print("RULES OF ABSTRACT CLASSES")
print("=" * 70)

print("✔ Import ABC and abstractmethod.")
print("✔ Inherit from ABC.")
print("✔ Use @abstractmethod.")
print("✔ Child class must implement all abstract methods.")
print("✔ Cannot create objects of abstract classes.")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to import ABC.")
print("❌ Forgetting @abstractmethod.")
print("❌ Creating objects of abstract class.")
print("❌ Not implementing abstract methods.")
print("❌ Confusing abstraction with encapsulation.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use abstraction for common interfaces.")
print("✔ Keep abstract methods meaningful.")
print("✔ Use descriptive class names.")
print("✔ Don't expose implementation details.")
print("✔ Design reusable classes.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Machines",

    "Banking Systems",

    "Payment Gateways",

    "Vehicle Software",

    "Hospital Management",

    "Game Development",

    "AI & Machine Learning",

    "Operating Systems"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Abstraction hides implementation details.")
print("✔ Python uses the abc module for abstraction.")
print("✔ ABC stands for Abstract Base Class.")
print("✔ @abstractmethod creates abstract methods.")
print("✔ Abstract classes cannot be instantiated.")
print("✔ Child classes must implement abstract methods.")
print("✔ Abstraction makes code cleaner and more maintainable.")

print("=" * 70)
print("End of 04_abstraction.py")
print("=" * 70)
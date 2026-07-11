# Restaurant Billing System

print("\nWelcome to Bhomdev's Restaurant 🍕")
print("-" * 40)

# Ask customer details
name = input("Customer Name : ")
age = int(input("Customer Age : "))

# Show menu
print("\nMenu")
print("1. Pizza      - ₹250")
print("2. Burger     - ₹150")
print("3. Cold Drink - ₹50")

# Take order
pizza = int(input("\nHow many Pizza? : "))
burger = int(input("How many Burger? : "))
drink = int(input("How many Cold Drinks? : "))

# Item prices
PIZZA_PRICE = 250
BURGER_PRICE = 150
DRINK_PRICE = 50

# Calculate item bills
pizza_bill = pizza * PIZZA_PRICE
burger_bill = burger * BURGER_PRICE
drink_bill = drink * DRINK_PRICE

# Calculate total bill
subtotal = pizza_bill + burger_bill + drink_bill
gst = subtotal * 0.05
total = subtotal + gst

# Apply discount if bill is above 1000
final_bill = total

if total >= 1000:
    discount = total * 0.10
    final_bill -= discount
else:
    discount = 0

# Comparison operators
adult = age >= 18
discount_available = subtotal >= 1000
empty_order = subtotal == 0
bill_exists = subtotal != 0
big_order = subtotal > 2000
small_order = subtotal < 500

# Logical operators
free_delivery = subtotal >= 500 and adult
special_offer = subtotal >= 1500 or pizza >= 3
valid_order = not empty_order

# Membership operator
menu = ["Pizza", "Burger", "Cold Drink"]

print("\nChecking Menu")
print("Pizza in menu :", "Pizza" in menu)
print("Coffee in menu :", "Coffee" in menu)
print("Tea not in menu :", "Tea" not in menu)

# Identity operator
fav_menu = menu

print("\nIdentity Operator")
print(menu is fav_menu)
print(menu is not fav_menu)

new_menu = ["Pizza", "Burger", "Cold Drink"]

print(menu == new_menu)
print(menu is new_menu)

# Operator precedence
result = 10 + 5 * 2
print("\nOperator Precedence")
print("10 + 5 * 2 =", result)

# Print final bill
print("\n" + "=" * 40)
print("FINAL BILL")
print("=" * 40)

print("Customer :", name)
print("Age      :", age)

print("\nItems")
print(f"Pizza ({pizza}) : ₹{pizza_bill}")
print(f"Burger ({burger}) : ₹{burger_bill}")
print(f"Cold Drink ({drink}) : ₹{drink_bill}")

print("-" * 40)
print(f"Subtotal : ₹{subtotal:.2f}")
print(f"GST       : ₹{gst:.2f}")
print(f"Discount  : ₹{discount:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")

# Show order status
print("\nOrder Status")
print("Adult Customer     :", adult)
print("Discount Eligible  :", discount_available)
print("Free Delivery      :", free_delivery)
print("Special Offer      :", special_offer)
print("Valid Order        :", valid_order)
print("Big Order          :", big_order)
print("Small Order        :", small_order)
print("Bill Exists        :", bill_exists)

print("\nThank You! Visit Again 😊")
#        SUPERMARKET BILLING & INVENTORY MANAGEMENT SYSTEM

print("=" * 70)
print("        SUPERMARKET BILLING & INVENTORY MANAGEMENT SYSTEM")
print("=" * 70)

# ==========================================================
# STORE INFORMATION
# ==========================================================

STORE_NAME = "Bhomdev Supermarket"
STORE_GST = 0.18

# ==========================================================
# INVENTORY DATABASE
# [ID, Product Name, Category, Price, Stock]
# ==========================================================

inventory = [
    [101, "Rice", "Grocery", 60, 100],
    [102, "Sugar", "Grocery", 45, 80],
    [103, "Milk", "Dairy", 30, 50],
    [104, "Bread", "Bakery", 40, 60],
    [105, "Butter", "Dairy", 55, 40],
    [106, "Eggs", "Dairy", 8, 200],
    [107, "Cooking Oil", "Grocery", 180, 35],
    [108, "Tea Powder", "Beverages", 220, 25],
    [109, "Coffee", "Beverages", 350, 20],
    [110, "Soap", "Personal Care", 35, 120]
]

# ==========================================================
# SHOPPING CART
# ==========================================================

cart = []

# ==========================================================
# CUSTOMER DETAILS
# ==========================================================

print("\nCustomer Registration")
print("-" * 70)

customer_name = input("Customer Name     : ").title()
customer_mobile = input("Mobile Number     : ")
customer_city = input("City              : ").title()

# String Methods
print("\nCustomer Details Preview")
print("-" * 70)

print(f"Upper Case     : {customer_name.upper()}")
print(f"Lower Case     : {customer_name.lower()}")
print(f"Title Case     : {customer_name.title()}")

if len(customer_name) >= 3:
    print(f"First 3 Letters : {customer_name[:3]}")
    print(f"Last 3 Letters  : {customer_name[-3:]}")

print(f"Reverse Name    : {customer_name[::-1]}")
print(f"Name Length     : {len(customer_name)}")

# ==========================================================
# MEMBERSHIP OPERATOR
# ==========================================================

cities = [
    "Delhi",
    "Mumbai",
    "Patiala",
    "Chandigarh",
    "Jaipur",
    "Mohali"
]

if customer_city in cities:
    print("Service Available in Your City")
else:
    print("Home Delivery Not Available")

# ==========================================================
# IDENTITY OPERATOR
# ==========================================================

print("\nIdentity Operator Demo")

number1 = 100
number2 = 100

print(number1 is number2)
print(number1 is not number2)

# ==========================================================
# DISPLAY INVENTORY
# ==========================================================

print("\n" + "=" * 70)
print("AVAILABLE PRODUCTS")
print("=" * 70)

print(f"{'ID':<8}{'PRODUCT':<20}{'CATEGORY':<18}{'PRICE':<10}{'STOCK'}")
print("-" * 70)

for product in inventory:
    print(
        f"{product[0]:<8}"
        f"{product[1]:<20}"
        f"{product[2]:<18}"
        f"₹{product[3]:<9}"
        f"{product[4]}"
    )

print("-" * 70)

# ==========================================================
# INVENTORY SUMMARY
# ==========================================================

print("\nInventory Summary")

print(f"Total Products : {len(inventory)}")

total_stock = 0

for product in inventory:
    total_stock += product[4]

print(f"Total Stock    : {total_stock}")

# ==========================================================
# MAIN MENU
# ==========================================================

while True:

    print("\n" + "=" * 70)
    print("MAIN MENU")
    print("=" * 70)

    print("1. View Products")
    print("2. Search Product")
    print("3. Purchase Product")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Inventory Report")
    print("7. Exit")

    choice = int(input("\nEnter Your Choice : "))

    match choice:

        case 1:

            print("\nAVAILABLE PRODUCTS")
            print("-" * 70)

            for product in inventory:
                print(
                    f"{product[0]}  | "
                    f"{product[1]:15} | "
                    f"{product[2]:15} | "
                    f"₹{product[3]:5} | "
                    f"Stock : {product[4]}"
                )

        case 2:

            print("\n🚧 Search Product")
            print("Feature Coming in Part 2")

        case 3:

            print("\n🚧 Purchase Product")
            print("Feature Coming in Part 2")

        case 4:

            print("\n🚧 Shopping Cart")
            print("Feature Coming in Part 3")

        case 5:

            print("\n🚧 Checkout")
            print("Feature Coming in Part 4")

        case 6:

            print("\n🚧 Inventory Report")
            print("Feature Coming in Part 4")

        case 7:

            print("\nThank You For Visiting")
            print(STORE_NAME)
            break

        case _:

            print("Invalid Choice")

# PART 2 - PRODUCT SEARCH & PURCHASE SYSTEM

print("\n" + "="*70)
print("PART 2 - PRODUCT SEARCH & PURCHASE")
print("="*70)

while True:
    print("\n1. Search Product")
    print("2. Purchase Product")
    print("3. Return to Main Menu")

    option = input("Choose: ")

    if option == "3":
        break

    elif option == "1":
        keyword = input("Enter product name: ").strip().lower()
        found = False

        for product in inventory:
            if keyword in product[1].lower():
                print("-"*70)
                print(f"ID       : {product[0]}")
                print(f"Name     : {product[1]}")
                print(f"Category : {product[2]}")
                print(f"Price    : ₹{product[3]}")
                print(f"Stock    : {product[4]}")
                print("-"*70)
                found = True

        if not found:
            print("Product not found.")

    elif option == "2":

        while True:
            try:
                pid = int(input("Enter Product ID: "))
                break
            except ValueError:
                print("Enter a valid numeric Product ID.")

        selected = None

        for product in inventory:
            if product[0] == pid:
                selected = product
                break

        if selected is None:
            print("Invalid Product ID.")
            continue

        while True:
            qty = int(input("Enter Quantity: "))

            if qty <= 0:
                print("Quantity must be greater than zero.")
                continue

            if qty > selected[4]:
                print("Insufficient stock.")
                retry = input("Try another quantity? (y/n): ").lower()
                if retry == "y":
                    continue
                break

            amount = qty * selected[3]

            discount = 0
            if amount >= 2000:
                discount = amount * 0.20
            elif amount >= 1000:
                discount = amount * 0.10
            elif amount >= 500:
                discount = amount * 0.05

            gst = (amount - discount) * STORE_GST
            total = amount - discount + gst

            selected[4] -= qty

            cart.append([
                selected[0],
                selected[1],
                qty,
                selected[3],
                amount,
                discount,
                gst,
                total
            ])

            print("\nItem Added Successfully")
            print(f"Product  : {selected[1]}")
            print(f"Quantity : {qty}")
            print(f"Amount   : ₹{amount:.2f}")
            print(f"Discount : ₹{discount:.2f}")
            print(f"GST      : ₹{gst:.2f}")
            print(f"Total    : ₹{total:.2f}")
            break

    else:
        pass
        print("Invalid Menu Option.")


# PART 3 - CART MANAGEMENT
print("\n" + "="*70)
print("PART 3 - CART MANAGEMENT")
print("="*70)

while True:
    print("\n1. View Cart")
    print("2. Update Quantity")
    print("3. Remove Item")
    print("4. Cart Summary")
    print("5. Clear Cart")
    print("6. Return")

    ch=input("Choose: ")

    if ch=="6":
        break

    elif ch=="1":
        if not cart:
            print("Cart is empty.")
            continue
        print("-"*70)
        for i,item in enumerate(cart,1):
            print(f"{i}. {item[1]} Qty:{item[2]} Total: ₹{item[7]:.2f}")
        print("-"*70)

    elif ch=="2":
        if not cart:
            print("Cart is empty."); continue
        idx=int(input("Cart item number: "))-1
        if idx<0 or idx>=len(cart):
            print("Invalid."); continue
        new_qty=int(input("New quantity: "))
        if new_qty<=0:
            print("Invalid."); continue
        pid=cart[idx][0]
        inv=None
        for p in inventory:
            if p[0]==pid:
                inv=p; break
        old_qty=cart[idx][2]
        diff=new_qty-old_qty
        if diff>inv[4]:
            print("Not enough stock."); continue
        inv[4]-=diff
        amount=new_qty*cart[idx][3]
        disc=0
        if amount>=2000: disc=amount*0.20
        elif amount>=1000: disc=amount*0.10
        elif amount>=500: disc=amount*0.05
        gst=(amount-disc)*STORE_GST
        total=amount-disc+gst
        cart[idx][2]=new_qty
        cart[idx][4]=amount
        cart[idx][5]=disc
        cart[idx][6]=gst
        cart[idx][7]=total
        print("Updated.")

    elif ch=="3":
        if not cart:
            print("Cart empty."); continue
        idx=int(input("Cart item number: "))-1
        if 0<=idx<len(cart):
            item=cart.pop(idx)
            for p in inventory:
                if p[0]==item[0]:
                    p[4]+=item[2]
            print("Removed:",item[1])

    elif ch=="4":
        backup=cart.copy()
        subtotal=sum(x[4] for x in backup)
        print("Items:",len(backup))
        print("Subtotal:",subtotal)
        names=[x[1] for x in backup]
        names.sort()
        print("Sorted:",names)
        names.reverse()
        print("Reverse:",names)
        if backup:
            print("First item index:",backup.index(backup[0]))
            print("First product count:",names.count(names[0]))

    elif ch=="5":
        confirm=input("Clear cart? y/n: ").lower()
        if confirm=="y":
            for item in cart:
                for p in inventory:
                    if p[0]==item[0]:
                        p[4]+=item[2]
            cart.clear()
            print("Cart cleared.")
    else:
        pass
        print("Invalid choice.")

# ==========================================================
#           PART 4A - CHECKOUT & BILL GENERATION
# ==========================================================

print("\n" + "=" * 70)
print("                 CHECKOUT")
print("=" * 70)

# ----------------------------------------------------------
# Check Whether Cart is Empty
# ----------------------------------------------------------

if len(cart) == 0:
    print("\nYour Shopping Cart is Empty.")
    print("Please Purchase Products First.")
else:

    print("\nCustomer Details")
    print("-" * 70)

    print(f"Customer Name   : {customer_name}")
    print(f"Mobile Number   : {customer_mobile}")
    print(f"City            : {customer_city}")

    print("\nPurchased Products")
    print("-" * 70)

    print(
        f"{'ID':<8}"
        f"{'PRODUCT':<20}"
        f"{'QTY':<8}"
        f"{'PRICE':<10}"
        f"{'TOTAL'}"
    )

    print("-" * 70)

    subtotal = 0
    total_discount = 0
    total_gst = 0
    grand_total = 0
    total_items = 0

    # ------------------------------------------------------
    # Display Cart Items
    # ------------------------------------------------------

    for item in cart:

        product_id = item[0]
        product_name = item[1]
        quantity = item[2]
        price = item[3]
        amount = item[4]
        discount = item[5]
        gst = item[6]
        total = item[7]

        subtotal += amount
        total_discount += discount
        total_gst += gst
        grand_total += total
        total_items += quantity

        print(
            f"{product_id:<8}"
            f"{product_name:<20}"
            f"{quantity:<8}"
            f"₹{price:<9}"
            f"₹{total:.2f}"
        )

    print("-" * 70)

    # ------------------------------------------------------
    # Bill Summary
    # ------------------------------------------------------

    print("\nBill Summary")
    print("-" * 70)

    print(f"Total Products Purchased : {len(cart)}")
    print(f"Total Quantity           : {total_items}")
    print(f"Subtotal                 : ₹{subtotal:.2f}")
    print(f"Discount                 : ₹{total_discount:.2f}")
    print(f"GST                      : ₹{total_gst:.2f}")
    print(f"Grand Total              : ₹{grand_total:.2f}")

    print("-" * 70)

    # ------------------------------------------------------
    # Payment Method
    # ------------------------------------------------------

    print("\nSelect Payment Method")

    print("1. Cash")
    print("2. UPI")
    print("3. Debit Card")
    print("4. Credit Card")

    payment = int(input("\nEnter Choice : "))

    match payment:

        case 1:
            payment_method = "Cash"

        case 2:
            payment_method = "UPI"

        case 3:
            payment_method = "Debit Card"

        case 4:
            payment_method = "Credit Card"

        case _:
            payment_method = "Cash"

    print(f"\nPayment Method : {payment_method}")

    # ------------------------------------------------------
    # Payment Status
    # ------------------------------------------------------

    print("\nProcessing Payment...")

    payment_success = True

    if payment_success:

        print("Payment Successful")
        print("Order Confirmed")

    else:

        print("Payment Failed")
        print("Please Try Again")

    print("\n" + "=" * 70)
    print("               TAX INVOICE")
    print("=" * 70)

    print(f"Store Name      : {STORE_NAME}")
    print(f"Customer        : {customer_name}")
    print(f"Mobile          : {customer_mobile}")
    print(f"City            : {customer_city}")
    print(f"Payment Mode    : {payment_method}")

    print("-" * 70)

    print(f"Items Purchased : {len(cart)}")
    print(f"Total Quantity  : {total_items}")

    print("-" * 70)

    print(f"Subtotal        : ₹{subtotal:.2f}")
    print(f"Discount        : ₹{total_discount:.2f}")
    print(f"GST             : ₹{total_gst:.2f}")

    print("=" * 70)
    print(f"GRAND TOTAL     : ₹{grand_total:.2f}")
    print("=" * 70)

    # ==========================================================
#        PART 4B - INVENTORY REPORT & SALES SUMMARY
# ==========================================================

if len(cart) > 0:

    # ------------------------------------------------------
    # Remaining Inventory Report
    # ------------------------------------------------------

    print("\n" + "=" * 70)
    print("              REMAINING INVENTORY REPORT")
    print("=" * 70)

    print(
        f"{'ID':<8}"
        f"{'PRODUCT':<20}"
        f"{'CATEGORY':<18}"
        f"{'PRICE':<10}"
        f"{'STOCK'}"
    )

    print("-" * 70)

    total_inventory_stock = 0

    for product in inventory:

        total_inventory_stock += product[4]

        print(
            f"{product[0]:<8}"
            f"{product[1]:<20}"
            f"{product[2]:<18}"
            f"₹{product[3]:<9}"
            f"{product[4]}"
        )

    print("-" * 70)

    print(f"Total Remaining Stock : {total_inventory_stock}")

    # ------------------------------------------------------
    # Sales Summary
    # ------------------------------------------------------

    print("\n" + "=" * 70)
    print("                  SALES SUMMARY")
    print("=" * 70)

    highest_bill = 0
    highest_product = ""

    for item in cart:

        if item[7] > highest_bill:
            highest_bill = item[7]
            highest_product = item[1]

    print(f"Customer Name        : {customer_name}")
    print(f"Items Purchased      : {len(cart)}")
    print(f"Total Quantity       : {total_items}")
    print(f"Highest Value Item   : {highest_product}")
    print(f"Highest Bill Amount  : ₹{highest_bill:.2f}")

    print(f"Overall Sale         : ₹{grand_total:.2f}")

    # ------------------------------------------------------
    # Shopping Cart Details
    # ------------------------------------------------------

    print("\nShopping Cart Records")

    for index, item in enumerate(cart, start=1):

        print("-" * 70)

        print(f"Item Number   : {index}")
        print(f"Product ID    : {item[0]}")
        print(f"Product Name  : {item[1]}")
        print(f"Quantity      : {item[2]}")
        print(f"Unit Price    : ₹{item[3]}")
        print(f"Amount        : ₹{item[4]:.2f}")
        print(f"Discount      : ₹{item[5]:.2f}")
        print(f"GST           : ₹{item[6]:.2f}")
        print(f"Final Total   : ₹{item[7]:.2f}")

    print("-" * 70)

    # ------------------------------------------------------
    # String Operations
    # ------------------------------------------------------

    print("\n" + "=" * 70)
    print("              STRING OPERATIONS")
    print("=" * 70)

    print(f"Original Name      : {customer_name}")
    print(f"Upper Case         : {customer_name.upper()}")
    print(f"Lower Case         : {customer_name.lower()}")
    print(f"Title Case         : {customer_name.title()}")

    print(f"Length             : {len(customer_name)}")

    print(f"First Character    : {customer_name[0]}")
    print(f"Last Character     : {customer_name[-1]}")

    print(f"First 3 Letters    : {customer_name[:3]}")
    print(f"Last 3 Letters     : {customer_name[-3:]}")

    print(f"Reverse Name       : {customer_name[::-1]}")

    print(f"Starts With 'B'    : {customer_name.startswith('B')}")
    print(f"Ends With 'a'      : {customer_name.endswith('a')}")

    print(f"Replace 'a' -> '*' : {customer_name.replace('a', '*')}")

    print(f"Count of 'a'       : {customer_name.lower().count('a')}")

    # ------------------------------------------------------
    # List Operations
    # ------------------------------------------------------

    print("\n" + "=" * 70)
    print("               LIST OPERATIONS")
    print("=" * 70)

    product_names = []

    for item in cart:
        product_names.append(item[1])

    print("Original List")
    print(product_names)

    copied_list = product_names.copy()

    print("\nCopied List")
    print(copied_list)

    copied_list.sort()

    print("\nSorted List")
    print(copied_list)

    copied_list.reverse()

    print("\nReverse Sorted List")
    print(copied_list)

    if len(copied_list) > 0:

        print(f"\nFirst Product : {copied_list[0]}")
        print(f"Last Product  : {copied_list[-1]}")

        print(f"\nFirst Two Products : {copied_list[:2]}")
        print(f"Last Two Products  : {copied_list[-2:]}")

    print(f"\nTotal Products In List : {len(copied_list)}")

    # ------------------------------------------------------
    # Thank You Screen
    # ------------------------------------------------------

    print("\n" + "=" * 70)
    print("           THANK YOU FOR SHOPPING WITH US")
    print("=" * 70)

    print(f"""
Customer Name : {customer_name}
Store         : {STORE_NAME}

Your purchase has been completed successfully.

Please visit again.

Have a wonderful day!

⭐⭐⭐⭐⭐
""")

    print("=" * 70)

    # ------------------------------------------------------
    # Clear Shopping Cart
    # ------------------------------------------------------

    cart.clear()

    print("Shopping Cart Cleared Successfully.")

    print("=" * 70)
    print("PROJECT EXECUTED SUCCESSFULLY")
    print("=" * 70)
#              HOTEL MANAGEMENT SYSTEM
print("="*60)
print("               HOTEL MANAGEMENT SYSTEM")
print("="*60)

guest_name = input("Guest Name        : ")
age = int(input("Age               : "))
phone = input("Phone Number      : ")
city = input("City              : ")
days = int(input("Number of Days    : "))

print("\nRoom Types")
print("1. Standard")
print("2. Deluxe")
print("3. Premium")
print("4. Suite")

choice = int(input("Choose Room (1-4): "))

match choice:
    case 1:
        room_type="Standard"; rate=1500
    case 2:
        room_type="Deluxe"; rate=2500
    case 3:
        room_type="Premium"; rate=4000
    case 4:
        room_type="Suite"; rate=6000
    case _:
        room_type="Standard"; rate=1500

subtotal = rate * days
gst = subtotal * 0.18
discount = 0

if age >= 60:
    discount += subtotal * 0.10

if days >= 5:
    if room_type in ("Premium","Suite"):
        breakfast = "Free"
    else:
        breakfast = "Not Included"
    discount += subtotal * 0.05
else:
    breakfast = "Not Included"

grand_total = subtotal + gst - discount

print("\nGenerating Available Rooms")
for room in range(101,111):
    print(f"Room {room}")

print("\nHotel Layout")
for floor in range(1,4):
    print(f"Floor {floor}")
    for room in range(1,6):
        if room == 3:
            print("  Room Under Maintenance")
            continue
        print(f"  Room {floor}{room:02d}")

print("\nCheck-in Menu")
while True:
    cmd=input("Type checkin or exit: ").lower()
    if cmd=="exit":
        break
    elif cmd=="checkin":
        print("Check-in Successful.")
    else:
        pass
        print("Invalid option.")

hotel_name="Grand Python Hotel"

print("\n"+"="*60)
print("                 HOTEL BILL")
print("="*60)
print(f"Guest Name      : {guest_name.title()}")
print(f"City            : {city.title()}")
print(f"Phone           : {phone}")
print(f"Room Type       : {room_type}")
print(f"Stay            : {days} Days")
print(f"Hotel           : {hotel_name}")
print("-"*60)
print(f"Subtotal        : ₹{subtotal:.2f}")
print(f"GST (18%)       : ₹{gst:.2f}")
print(f"Discount        : ₹{discount:.2f}")
print(f"Grand Total     : ₹{grand_total:.2f}")
print(f"Breakfast       : {breakfast}")
print("-"*60)
print("String Operations")
print(f"Upper           : {guest_name.upper()}")
print(f"Lower           : {guest_name.lower()}")
print(f"Title           : {guest_name.title()}")
print(f"First Letter    : {guest_name[0]}")
print(f"Last Letter     : {guest_name[-1]}")
print(f"First 3 Letters : {guest_name[:3]}")
print(f"Last 3 Letters  : {guest_name[-3:]}")
print(f"Reverse Name    : {guest_name[::-1]}")
print(f"Length          : {len(guest_name)}")
print(f"Starts with B   : {guest_name.startswith('B')}")
print(f"Ends with a     : {guest_name.endswith('a')}")
print("="*60)
print("Thank You For Visiting!")
print("="*60)

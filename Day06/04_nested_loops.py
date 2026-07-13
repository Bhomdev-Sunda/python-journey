#              NESTED LOOPS IN PYTHON
print("=" * 60)
print("         COMPANY SEATING ARRANGEMENT")
print("=" * 60)

# Display Office Seating Layout
print("\nEmployee Seating Plan:\n")

for floor in range(1, 4):
    print(f"Floor {floor}")

    for seat in range(1, 6):
        print(f"   Seat {seat}  --> Available")

    print("-" * 40)

# End
print("\n" + "=" * 60)
print("Office Seating Plan Generated Successfully.")
print("=" * 60)
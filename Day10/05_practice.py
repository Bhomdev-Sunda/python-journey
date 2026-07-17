# Student Club Management (Sets)
print("="*60)
print("STUDENT CLUB MANAGEMENT SYSTEM")
print("="*60)

python_club={"Rahul","Aman","Bhomdev","Neha"}
ai_club={"Bhomdev","Priya","Aman","Riya"}

print("\nPython Club:",python_club)
print("AI Club:",ai_club)

python_club.add("Karan")
ai_club.update(["Sonia","Rohit"])

python_club.discard("Neha")
ai_club.remove("Riya")

print("\nUnion:", python_club.union(ai_club))
print("Intersection:", python_club.intersection(ai_club))
print("Difference:", python_club.difference(ai_club))
print("Symmetric Difference:", python_club.symmetric_difference(ai_club))

core={"Aman","Bhomdev"}
print("\nSubset:", core.issubset(python_club))
print("Superset:", python_club.issuperset(core))

name=input("\nEnter student name: ").title()
if name in python_club or name in ai_club:
    print(name,"found.")
else:
    print(name,"not found.")

print("\nLooping Python Club")
for student in sorted(python_club):
    print(student)

lengths={student:len(student) for student in python_club}
print("\nDictionary Comprehension:", lengths)

rules=frozenset({"Respect","Discipline","Attendance"})
print("\nFrozen Set:", rules)

print("\nProject Completed Successfully!")

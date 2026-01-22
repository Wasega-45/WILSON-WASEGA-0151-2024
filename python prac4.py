
# Using a class to represent a structure

class Student:
    def __init__(self, reg_no, name, age, average_mark):
        self.reg_no = reg_no
        self.name = name
        self.age = age
        self.average_mark = average_mark


student1 = Student(2051, "Wilson", 20, 62.8)

print("Student Details")
print("Reg No:", student1.reg_no)
print("Name:", student1.name)
print("Age:", student1.age)
print("Average Mark:", student1.average_mark)
print()

marks = int(input("Enter marks: "))

# IF - ELIF - ELSE
if marks >= 70:
    print("Grade: Distinction")
elif marks >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")

# SWITCH equivalent using match-case (Python 3.10+)
grade = input("Enter grade (A/B/C): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Invalid Grade")

# ---------- ITERATION STATEMENTS ----------

# FOR LOOP
print("\nFor Loop Output:")
for i in range(1, 6):
    print(i, end=" ")
print()

# WHILE LOOP
print("\nWhile Loop Output:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# DO-WHILE equivalent using while True
print("\nDo-While Loop Output:")
j = 1
while True:
    print(j, end=" ")
    j += 1
    if j > 5:
        break

print()
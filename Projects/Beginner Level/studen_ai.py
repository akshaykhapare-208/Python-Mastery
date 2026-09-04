from tabulate import tabulate


# -------------------------------
# School Information
# -------------------------------

school_info = ("Python Mastery School", "2026", "A")

subjects = ["Python", "Math", "English", "Science", "Computer"]
marks = [85, 92, 78, 88, 95]


# -------------------------------
# Student Information
# -------------------------------

student_name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
roll_no = int(input("Enter Your Roll No: "))
student_class = input("Enter Your Class: ")


# -------------------------------
# Calculations
# -------------------------------

total_marks = sum(marks)
maximum_marks = len(marks) * 100
percentage = (total_marks / maximum_marks) * 100
average = total_marks / len(marks)


# -------------------------------
# Grade Calculation
# -------------------------------

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


# -------------------------------
# Subject Table
# -------------------------------

table = []

for i in range(len(subjects)):
    table.append([subjects[i], marks[i]])


# -------------------------------
# Student Report
# -------------------------------

print("\n" + "=" * 45)
print("           STUDENT REPORT")
print("=" * 45)

print(f"Student Name  : {student_name}")
print(f"Age           : {age}")
print(f"Roll Number   : {roll_no}")
print(f"Class         : {student_class}")
print(f"School        : {school_info[0]}")
print(f"Academic Year : {school_info[1]}")
print(f"Section       : {school_info[2]}")

print("\n" + "-" * 45)
print("              MARKS")
print("-" * 45)

print(tabulate(
    table,
    headers=["Subject", "Marks"],
    tablefmt="grid"
))

print("-" * 45)

print(f"Total Marks   : {total_marks}/{maximum_marks}")
print(f"Percentage    : {percentage:.2f}%")
print(f"Average       : {average:.2f}")
print(f"Grade         : {grade}")

print("=" * 45)
from tabulate import tabulate

subjects = ["Python", "Math", "English", "Science", "Computer"]
school_info = ("Python Mastery School", "2026", "A")
marks = [85, 92, 78, 88, 95]

student_name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
roll_no = int(input("Enter Your Roll No: "))
student_class = input("Enter Your Class: ")

print(''' =================================== \n
         STUDENT REPORT            \n
    ===================================
''')

print("Student Name  : " , student_name)
print("Age           : " , age)
print("Roll Number   : " , roll_no)
print("Class         : " , student_class)

print("School        : " , school_info [0])
print("Academic Year : " , school_info [1])
print("Class         : " , school_info [2])

print(''' ---------------------------------------
Subjects                       Marks
-------------------------------------------------
''')
print(subjects [0] , marks [0] )
print(subjects [1] , marks [1] )
print(subjects [2] , marks [2] )
print(subjects [3] , marks [3] )
print(subjects [4] , marks [4] )
print("-------------------------------------------")

print("Total Marks: " , )





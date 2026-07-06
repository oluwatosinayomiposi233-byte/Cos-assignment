print("PERSONAL POCKET CGPA CALCULATOR")

courses = int(input("Enter the number of courses: "))

total_grade_points = 0
total_credit_units = 0

for i in range(1, courses + 1):
    print(f"\nCourse {i}")
    score = float(input("Enter score (0 - 100): "))
    credit = int(input("Enter credit unit: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    print("Grade:", grade)
    print("Grade Point:", point)

    total_grade_points += point * credit
    total_credit_units += credit

cgpa = total_grade_points / total_credit_units

print("\nRESULT")
print("Total Credit Units:", total_credit_units)
print("CGPA: {:.2f}".format(cgpa))

if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
else:
    print("Class of Degree: Pass")
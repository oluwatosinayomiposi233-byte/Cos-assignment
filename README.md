"""
=====================================================
   PERSONAL POCKET CGPA CALCULATOR (PPC)
   Using Python Selection Control Statements
=====================================================
This program allows a student to calculate their
Grade Point Average (GPA) for a semester and their
Cumulative GPA (CGPA) across multiple semesters,
without needing to visit the academic records office.

Grading System Used (5-Point Scale):
    A  = 70 - 100  -> 5 points
    B  = 60 - 69   -> 4 points
    C  = 50 - 59   -> 3 points
    D  = 45 - 49   -> 2 points
    E  = 40 - 44   -> 1 point
    F  = 0  - 39   -> 0 points
=====================================================
"""

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def score_to_grade_point(score):
    """
    Converts a numeric score (0-100) into a grade letter and
    grade point using SELECTION CONTROL STATEMENTS (if/elif/else).
    """
    if score >= 70:
        grade = 'A'
        point = 5
    elif score >= 60:
        grade = 'B'
        point = 4
    elif score >= 50:
        grade = 'C'
        point = 3
    elif score >= 45:
        grade = 'D'
        point = 2
    elif score >= 40:
        grade = 'E'
        point = 1
    else:
        grade = 'F'
        point = 0
    return grade, point


def get_valid_score(course_name):
    """Ensures the score entered is a valid number between 0 and 100."""
    while True:
        try:
            score = float(input(f"   Score obtained in {course_name} (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("   >> Score must be between 0 and 100. Try again.")
        except ValueError:
            print("   >> Invalid input. Please enter a number.")


def get_valid_units():
    """Ensures course unit/credit load entered is a positive whole number."""
    while True:
        try:
            units = int(input("   Course Units/Credits: "))
            if units > 0:
                return units
            else:
                print("   >> Units must be a positive number. Try again.")
        except ValueError:
            print("   >> Invalid input. Please enter a whole number.")


def calculate_semester_gpa():
    """Calculates GPA for a single semester based on user-entered courses."""
    print("\n--- SEMESTER GPA CALCULATION ---")

    while True:
        try:
            num_courses = int(input("How many courses did you offer this semester? "))
            if num_courses > 0:
                break
            print(">> Please enter a number greater than 0.")
        except ValueError:
            print(">> Invalid input. Please enter a whole number.")

    total_units = 0
    total_points = 0

    for i in range(1, num_courses + 1):
        print(f"\nCourse {i}:")
        course_name = input("   Course Code/Name: ")
        units = get_valid_units()
        score = get_valid_score(course_name)

        grade, point = score_to_grade_point(score)
        course_weighted_point = point * units

        total_units += units
        total_points += course_weighted_point

        print(f"   -> Grade: {grade} | Grade Point: {point} | "
              f"Weighted Point: {course_weighted_point}")

    if total_units == 0:
        print("No units entered. Cannot compute GPA.")
        return None

    gpa = total_points / total_units
    print("\n" + "=" * 45)
    print(f" Total Units       : {total_units}")
    print(f" Total Grade Points: {total_points}")
    print(f" SEMESTER GPA      : {gpa:.2f}")
    print("=" * 45)

    return gpa, total_units, total_points


def calculate_cgpa():
    """Calculates CGPA across multiple semesters/sessions."""
    print("\n--- CUMULATIVE CGPA CALCULATION ---")

    while True:
        try:
            num_semesters = int(input("How many semesters do you want to include? "))
            if num_semesters > 0:
                break
            print(">> Please enter a number greater than 0.")
        except ValueError:
            print(">> Invalid input. Please enter a whole number.")

    grand_total_units = 0
    grand_total_points = 0

    for s in range(1, num_semesters + 1):
        print(f"\n============ SEMESTER {s} ============")
        result = calculate_semester_gpa()

        if result is not None:
            gpa, units, points = result
            grand_total_units += units
            grand_total_points += points

    if grand_total_units == 0:
        print("No valid data entered. Cannot compute CGPA.")
        return

    cgpa = grand_total_points / grand_total_units
    print("\n" + "#" * 45)
    print(f" GRAND TOTAL UNITS        : {grand_total_units}")
    print(f" GRAND TOTAL GRADE POINTS : {grand_total_points}")
    print(f" YOUR CUMULATIVE CGPA     : {cgpa:.2f}")
    print("#" * 45)

    # Selection control statement to give remark based on CGPA class of degree
    if cgpa >= 4.50:
        remark = "First Class"
    elif cgpa >= 3.50:
        remark = "Second Class Upper"
    elif cgpa >= 2.40:
        remark = "Second Class Lower"
    elif cgpa >= 1.50:
        remark = "Third Class"
    else:
        remark = "Pass / Below Standard"

    print(f" CLASSIFICATION           : {remark}")
    print("#" * 45)


def display_menu():
    print("=" * 45)
    print("   PERSONAL POCKET CGPA CALCULATOR (PPC)")
    print("=" * 45)
    print(" 1. Calculate Semester GPA")
    print(" 2. Calculate Cumulative CGPA (Multiple Semesters)")
    print(" 3. Exit")
    print("=" * 45)


def main():
    clear_screen()
    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()

        # SELECTION CONTROL STATEMENT (if/elif/else)
        if choice == '1':
            calculate_semester_gpa()
            input("\nPress ENTER to return to menu...")
            clear_screen()

        elif choice == '2':
            calculate_cgpa()
            input("\nPress ENTER to return to menu...")
            clear_screen()

        elif choice == '3':
            print("\nThank you for using PPC. Stay focused, stay motivated!")
            break

        else:
            print(">> Invalid option. Please select 1, 2, or 3.\n")
            input("Press ENTER to continue...")
            clear_screen()


if __name__ == "__main__":
    main()

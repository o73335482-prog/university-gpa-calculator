def get_grade_points(grade: str) -> float:
    scale = {
        "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0,
        "F": 0.0
    }
    return scale.get(grade.strip().upper(), -1.0)


def calculate_semester_gpa():
    print("=== University GPA Calculator ===")
    try:
        num_courses = int(input("Enter number of courses: "))
    except ValueError:
        print("Invalid number.")
        return

    total_points = 0.0
    total_credits = 0.0

    for i in range(1, num_courses + 1):
        print(f"\nCourse {i}:")
        try:
            credits = float(input("  Credit hours (e.g., 3): "))
            grade = input("  Letter grade (e.g., A, B+, C): ")
        except ValueError:
            print("Invalid input. Skipping course.")
            continue

        points = get_grade_points(grade)
        if points < 0 or credits <= 0:
            print("Invalid grade or credit hours. Try again.")
            continue

        total_points += points * credits
        total_credits += credits

    if total_credits > 0:
        gpa = total_points / total_credits
        print(f"\nTotal Credits: {total_credits}")
        print(f"Semester GPA: {gpa:.2f} / 4.00")
    else:
        print("\nNo valid courses entered.")


if __name__ == "__main__":
    calculate_semester_gpa()

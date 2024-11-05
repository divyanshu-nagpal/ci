# calculate_grades.py

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    # Sample list of student grades
    students_grades = {
        "Alice": [85, 90, 78],
        "Bob": [92, 88, 84],
        "Charlie": [70, 75, 80],
        "Diana": [88, 90, 85]
    }

    # Calculate and save average grades
    with open("average_grades.txt", "w") as file:
        for student, grades in students_grades.items():
            average_grade = calculate_average(grades)
            file.write(f"{student}: {average_grade:.2f}\n")
            print(f"{student}'s average grade: {average_grade:.2f}")

if __name__ == "__main__":
    main()

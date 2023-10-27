def calculate_total_marks(marks):
    return sum(marks)

def calculate_percentage(total_marks, max_marks):
    return (total_marks / max_marks) * 100

def assign_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def main():
    num_students = int(input("Enter the number of students: "))
    max_marks = int(input("Enter the maximum marks: "))

    students = []
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        marks = [int(x) for x in input(f"Enter the marks of {name} (separated by space): ").split()]
        total_marks = calculate_total_marks(marks)
        percentage = calculate_percentage(total_marks, max_marks)
        grade = assign_grade(percentage)
        students.append({'name': name, 'marks': marks, 'total_marks': total_marks, 'percentage': percentage, 'grade': grade})

    print("\nMarklist of Students:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Total Marks: {student['total_marks']}")
        print(f"Percentage: {student['percentage']:.2f}%")
        print(f"Grade: {student['grade']}\n")

if __name__ == "__main__":
    main()

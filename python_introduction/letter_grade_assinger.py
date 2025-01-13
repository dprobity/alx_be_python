# Assumming you have a column of data of students scores on a particular subject

students_score = [50, 100, 70, 80, 90, 30]

for score in students_score:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"

    print(f"Your grade is:, {grade}")


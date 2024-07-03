"""https://www.hackerrank.com/challenges/grading/problem"""

def grading_student(grades):

    final_grades=[]

    for grade in grades:

        if grade < 38:
            final_grades.append(grade)
        else:
            next_multiple_5 = (grade + 4)//5 * 5

            if next_multiple_5 - grade < 3:
                final_grades.append(next_multiple_5)
            else:
                final_grades.append(grade)

    return final_grades


gr=[73,67,40,33]

print(grading_student(gr))

# https://www.codewars.com/kata/5ad0d8356165e63c140014d4
def final_grade(exam, projects):
    grade = 0
    if exam > 90 or projects > 10:
        grade = 100
    elif exam > 75 and projects >= 5:
        grade = 90
    elif exam > 50 and projects >= 2:
        grade = 75
    return grade

def calculate_marks(sub1, sub2, sub3):
    if sub1 < 0 or sub2 < 0 or sub3 < 0:
        return 'Invalid Marks'
    total = sub1 + sub2 + sub3
    average = total / 3
    if sub1 <= 39 or sub2 <= 39 or sub3 <= 39:
        status = 'Fail'
    else:
        status = 'Pass'
    def get_grade(marks):
        if marks < 0:
            return 'NA'
        elif marks <= 39:
            return 'F'
        elif marks <= 44:
            return 'P'
        elif marks <= 49:
            return 'C'
        elif marks <= 54:
            return 'B'
        elif marks <= 59:
            return 'B+'
        elif marks <= 69:
            return 'A'
        elif marks <= 79:
            return 'A+'
        else:
            return 'O'
    grade1 = get_grade(sub1)
    grade2 = get_grade(sub2)
    grade3 = get_grade(sub3)
    return total, average, status, grade1, grade2, grade3
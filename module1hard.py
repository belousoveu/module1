grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

students = tuple(students)
# 1st method:
student_grades1 = {students: sum(grades) / len(grades) for students, grades in zip(students, grades)}
# 2nd method:
student_grades2 = dict(zip(students, map(lambda x: sum(x) / len(x), grades)))

print(student_grades1)
print(student_grades2)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
students_dict = dict(zip(students, grades))
for key, value in zip(students_dict.keys(), students_dict.values()):
    students_dict[key] = sum(value) / len(value)
print(students_dict)
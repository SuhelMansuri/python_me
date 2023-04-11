names = {'John', 'Peter', 'kate', 'Rick', 'Tina'}

students = {}.fromkeys(names, 0.0)
print(students)

# print(students['Samir'])
print(students.get('ABC',99.99))
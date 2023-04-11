a_list = [101, 55, 40, 24, 78, 200, 75, 19, 16, 43]
b_list = [i for i in a_list if i % 2 != 0]
print(b_list)

students = {'John':8.9,'Peter':9.1, 'Kate':6.7, 'Tania':9.8, 'Tina':8.7}
# grade_o = [name for name, gpa in students.items() if gpa >= 9.0 and name.startswith('T')]
grade_o = {name:'O' for name, gpa in students.items() if gpa >= 9.0 }
print(grade_o)
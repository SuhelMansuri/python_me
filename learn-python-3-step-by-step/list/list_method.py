students = ['Teddy', 'Saloni', 'Nikita', 'John', 'Frank', 'Ali', 10, 20, 5.6, [3.5, 6.7, 7.9]]
for i in students:
    print(i)
    
x = students[-1][1]
print('x = ',x)
students[-1][1] = 9.99
print('students - ',students)
# y = x[1]

# print(type(y),'y = ',y)
students = ['Teddy', 'Saloni', 'Nikita', 'John', 'Frank', 'Ali']
### APPEND METHOD ###
print(students)
students.append('Tina')
print('students - ',students)
print(students)
lst1 = ['Tina', 'Raj', 'Bob']
students.append(lst1)
print('students - ',students)

### EXTEND METHOD ###
print(students)
students.extend('Tina')
print('students - ',students)
print(students)
lst1 = ['Tina', 'Raj', 'Bob']
students.extend(lst1)
print('students - ',students)

### INSERT METHOD ###

print('before - ',students)
students.insert(0,'Bob')
print('after insert bob - ',students)

students.insert(2,'Tina')
print('after insert Tina- ',students)

### CLEAR METHOD ###

students.clear()
print('after clear studs- ',students)

### COPY METHOD ###
print('before - ',students)
stud = students.copy()
print('Content of stud: ',stud )

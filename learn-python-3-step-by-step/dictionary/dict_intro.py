students = {'John': 6.78, 'Kat':9.89,'Raj':8.89, 'Ali':8.56,'Tridip':9.0}
print(len(students))
print(students['Raj'])
students['Raj'] = students['Raj'] + 2
print(students['Raj'])

my_dictionary = {}

for k in students:
    print(k, '-', students[k])
for v in students.values():
    print(v)
for j in students.keys():
    print(j)
for l, m in students.items():
    print(l, m)
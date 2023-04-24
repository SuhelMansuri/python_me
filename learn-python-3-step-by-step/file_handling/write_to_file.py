names = ['Tina', 'Rabi', 'Mathew', 'Rahman', 'Sandip', 'Liza', 'Peter', 'John']
with open('students.txt','w') as file_object:
    # file_object.write('\n')
    # file_object.writelines(', '.join(names))
    # file_object.write('Hello, Again.')
    for name in names:
        file_object.write(name)
        file_object.write('\n')
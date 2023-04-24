with open('names.txt', 'r') as file_object:
    print('Is file closed ?  - ',file_object.closed)
    for line in file_object:
        print(line[:-1])
print('Is file closed ?  - ',file_object.closed)
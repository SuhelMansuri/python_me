# file handling in pythone
file_object = open('names.txt', 'r') # 1. read - 'r', 2. write - 'w', 3. append - 'a'
# lines = file_object.read()
# lines = file_object.read(10)
# lines = file_object.readline()
# # print(lines, type(lines))
# print(lines, len(lines))
# lines = file_object.readline()
# print(lines, len(lines))
# file_object.close()
# lines = file_object.readlines()
# print(lines, type(lines))
for line in file_object:
    print(line[:-1])
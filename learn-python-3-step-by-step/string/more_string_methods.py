line = "Hello World! This is a Python string"
# c = line.count("xyz")
# print(c)

target = 'is'
start = 0
idx = line.find(target, start)
# print(idx)
while idx != -1:
    print('Index of target', idx)
    start = idx + 1
    idx = line.find(target, start)
    
print("Line Starts with 'hey' : ",line.startswith('Hey'))
print("Line Ends with '.' : ",line.endswith('.'))

    
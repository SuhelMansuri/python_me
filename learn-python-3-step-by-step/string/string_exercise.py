my_str = '3 abcxy'
pos = 2
list = my_str.split(' ')

print(list)
a = int(list[0])
str = list[1]
# print(a)
# print(str)
if pos == 1:
    print(str[0:a:1])
if pos == 2:
    print(str[a::])
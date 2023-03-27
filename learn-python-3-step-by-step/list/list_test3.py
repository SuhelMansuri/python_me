my_list = [10, 30, 40, 30, 50, 30, 50, 30, 20]

if 60 in my_list:
    print('60 is in the list')
else:
    print('60 is not in list')
    
c = my_list.count(30)
c1 = my_list.count(50)
print('Count(30): ',c)
print('Count(50): ',c1)

my_list.reverse() 
print(my_list)
x = my_list.pop(30)
print(my_list, x)

print(my_list)
my_list.remove(30)
print(my_list)

print(my_list)
while 30 in my_list:
    my_list.remove(30)
print(my_list)

x = my_list.index(30, 4, 8)
print(x)

target = 50
c = my_list.count(target)
start = 0
i = 1
while i <= c:
    indx = my_list.index(target, start)
    print(indx)
    start = indx + 1
    i = i + 1
    
        
# def dummy(x):
#     # print('x =', x, 'from function, before update')
#     print('From func. Before update x id of x :', id(x))
#     x = x + 1 
#     print('From func. After update  x id of x :', id(x))
#     # print('x =', x, 'from function, after update')
    
# x = 10
# print('Before call f(dummy) id of       x :', id(x))
# # print('x =', x, 'Before calling function dummy')
# dummy(x)
# print('After call f(dummy) id of        x :', id(x))
# # print('x =', x, 'After calling function dummy')

def dummy(x):
    print('x =', x, 'from function, before update')
    x = x + 1 
    print('x =', x, 'from function, after update')

def dummy2(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * 2
    
    
x = 10

print('x =', x, 'Before calling function dummy')
dummy(x)
print('x =', x, 'After calling function dummy')

my_list = [1, 2, 3, 4, 5]
print(my_list)
dummy2(my_list)
print(my_list)
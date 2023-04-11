# lst = []
# for i in range(10):
#     lst.append(i)
lst = [i for i in range(20)]

print(lst)
lst = [i**2 for i in range(20)]
print(lst)
lst = [i**3 for i in range(10)]
print(lst)
lst  = [i for i in range(100) if i % 2 == 0]
print('Even inegers : ',lst)
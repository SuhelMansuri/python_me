
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

product  = 1

for i in a_list:
    if i % 2 == 0:
        continue
    else:
        product = product + i
        print(i, end = ' ')
print()
print('Product of all odd numbers: ',product)
     
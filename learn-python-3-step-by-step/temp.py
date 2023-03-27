sum = 0
for i in range(1, 5, 2):
    print(i, end = ' - ')
    for j in range(2, 0, -1):
        sum += (i+j)
        print(j, end = ' + ')
print(sum)
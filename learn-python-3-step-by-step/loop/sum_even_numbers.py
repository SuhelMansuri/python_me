n = int(input('Enter interges for sum of even n: '))

sum = 0
i = 0

while i <= n:
    print(i, end = ' ')
    sum = sum + i
    i = i + 2
    
print('Sum of even numebrs is: ', sum)
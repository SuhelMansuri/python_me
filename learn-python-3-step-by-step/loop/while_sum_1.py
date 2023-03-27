num = int(input('Enter positive ineger number: '))

sum = 0

while num != 0:
    rem = num % 10
    print(rem, end = ' ' )
    num = num // 10
    sum = sum + rem
print('Sum is :',sum) 
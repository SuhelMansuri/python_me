def sum_digits(num):
    sum_d = 0
    sum_sq = 0
    num = abs(num)
    while num > 0:
        sum_d += num % 10
        sum_sq += (num % 10) ** 2
        num //= 10
        
    return sum_d, sum_sq
    print('Hello world')

s,sd = sum_digits(1234)
print('Sum of digits: ', s, '\n' ,'Sum of square of digits: ',sd)
s,sd = sum_digits(-512)
print('Sum of digits: ', s, '\n' ,'Sum of square of digits: ',sd)
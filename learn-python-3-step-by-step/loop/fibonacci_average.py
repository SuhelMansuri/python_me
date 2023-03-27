n = int(input('Please Enter positive number for fibonacchi range n: '))
sum = 0
a,b = 0,1
for i in range(n):
    print(a, end = ' ')
    sum = sum + a
    a,b = b, a+b
    avg = sum / n
print()
print('sum: ',sum)
print('avg: ',avg)
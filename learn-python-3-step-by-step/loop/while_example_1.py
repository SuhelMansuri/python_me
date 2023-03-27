# more example using while loop
# 1. Find sum of integers from 1 to n
# 2. Find sum of even integers and odd integers upto n
# 3. Find factorial of a number n

n = int(input('Enter positive integer n: '))

# 1. Find sum of integers from 1 to n

sum = 0
i = 1
while i <= n:
    print(i, end = ' ')
    sum = sum + i
    i = i + 1
print('sum of integers is: ',sum )

# 2. Find sum of even integers and odd integers upto n

sum = 0
i = 2
while i <= n:
    print(i, end = ' ')
    sum = sum + i
    i = i + 2
print('sum of integers is: ',sum )

# 3. Find factorial of a number n
fact = 1
i = 1
while i <= n:
    print(i, end = ' ')
    fact = fact * i
    i = i + 1
print('factorial of integers is: ',fact)
# finding the factors of a given positive integer

n = int(input('Enter positive ineger n: '))

print('Factores of ',n,'are: ', 1, end = ' ')
i = 2
sum = 1 + n
count = 2
while i <= n//2:
    if n % i == 0:
        
        sum = sum + i
        print(i, end = ' ')
        count = count + 1
    i = i + 1 
print(n)
print('Sum of all factors: ', sum)
print('Total factors: ', count)
# 5. Write a program to find the factorial of a given number. 
def factorial(num):
    i = 0
    fact = 1 
    for i in range(num, i, -1):
         fact = fact * i
         print(i)
    print(fact)
    return fact    
num = int(input('Please Enter number: '))
factorial(num)
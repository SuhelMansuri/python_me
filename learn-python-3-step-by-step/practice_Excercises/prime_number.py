# Write a program to check if a given number is prime or not.
def is_prime(n):
    count = 0
    if n <= 1:
        return False 
    else:
        for i in range(1,n+1):
            if n % i == 0:
                print('I - ',i,'Count - ',count)
                count = count +1
        print('number of factors - ',count)
        if count > 2:
            return False
            # print(i,': is not a Prime number')
        else:
            return True 
num  = int(input('Enter number- '))       
if is_prime(num) == True:
     print('Number is a prime number')
else:                
    print('Number: is not a Prime number')   
       
    
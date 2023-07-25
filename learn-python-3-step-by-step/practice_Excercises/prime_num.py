fact = []

n = int(input("Please Enter number: "))
for i in range(1,n+1):
    if n % i == 0:
        fact.append(i)
        fact_len = len(fact)      
print("Factors of given number: ",fact)
print("Total count of factors: ",fact_len)

if fact_len == 2:
    print("Given number is a prime number ")
else:
    print("Sorry! Given number is not a prime number ")
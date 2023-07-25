# Write a program that will check whether the number is armstrong number or not.
# An Armstrong number is one whose sum of digits raised to the power three equals the number itself. 371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371.

n = int(input("Enter three digit Number: "))

print("Count",len(str(n)))

a = n%10
print("a : ",a)
num = n // 10
print("num : ",num)
b = num % 10
print("b : ",b)
c = num //10
print("c : ",c)

sq = a ** 3 + b ** 3 + c ** 3 
print("sq : ",sq)

if n == sq:
    print("Given number is a armstrong number")
else:
    print("Given number is not a armstrong number")
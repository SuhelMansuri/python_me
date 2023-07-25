# Write a program that will take three digits from the user and add the square of each digit.

n = int(input("Enter three digit nyumber: "))
a = n%10
print("a : ",a)
num = n // 10
print("num : ",num)
b = num % 10
print("b : ",b)
c = num //10
print("c : ",c)

sq = a ** 2 + b ** 2 + c ** 2
print("sq : ",sq)
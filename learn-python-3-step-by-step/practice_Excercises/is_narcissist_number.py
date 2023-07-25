# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not
n = int(input("Enter 4 digit value: "))
a = n%10
print("a : ",a)
num = n // 10
print("num : ",num)
b = num % 10
print("b : ",b)
num1 = num // 10
print("num1 : ",num1)
c = num1 % 10
print("c : ",c)
d = num1 // 10
print("d : ",d)

narc = a**4 + b**4 + c**4 + d**4
print("narc : ",narc)


if narc == n:
    print("Given number is narcissist number")
else:
    print("Oh no: Given number is not narcissist number")



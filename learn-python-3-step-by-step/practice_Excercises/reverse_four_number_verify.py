# Write a program that will reverse a four digit number.Also it checks whether the reverse is true

n = int(input("Enter four Digit number: "))

a = n%10
print ('a = ',a)

num1 = n//10
print('num1 = ',num1)

b  = num1%10
print ('b = ',b)

num2 = num1//10
print('num2 = ',num2)

c  = num2%10
print ('c = ',c)

d = num2//10
print('d = ',d)

# d  = num3%10
# print ('d = ',d)

rev_num  = a*1000 + b*100 + c*10 + d
print(rev_num)

rev_str = str(n)[::-1]
rev_str1 = int(rev_str)
print(rev_str1)

if rev_str1 == rev_num:
    print("Reverse is True: ")
else:
    print("Reverse is False: ")

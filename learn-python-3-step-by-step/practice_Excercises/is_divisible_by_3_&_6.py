# Write a program that will tell whether the given number is divisible by 3 & 6
n = int(input("Enter the number : "))

if n % 3 == 0:
    if n % 6==0:
        print("Number is divisable by 3 and 6 ")
    else:
        print("Number is divisable by 3 but not divisable by 6")
else:
    print("Number is not divisable by 3 and 6")

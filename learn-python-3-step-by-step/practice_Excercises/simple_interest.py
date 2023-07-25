# Write a program to find the simple interest when the value of principle,rate of interest and timeperiod is given.

P = float(input("Please enter principal amount: "))
R = float(input("Please enter rate of intrest: "))
T = int(input("Please enter Time period : "))

simple_int = (P*R*T) / 100

print("Simple intrest amount is: ",simple_int)

total_due = P + simple_int
print("total due amount: ",total_due)
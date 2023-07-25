# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1 litre milk is 40Rs.
pi = 3.142
r = float(input("Please enter radious of cylinder in cm: "))
h = float(input("Please enter height of cylinder in cm: "))

volume = pi * (r**2) * h
ltr = volume/1000
cost = ltr * 40
print("Volume of cylinder will be: ",volume)
print("How much milk we can store into cylinder: ",ltr)
print("Cost of milk is: ",cost)

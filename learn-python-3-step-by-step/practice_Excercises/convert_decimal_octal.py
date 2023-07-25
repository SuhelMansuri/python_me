# Convert Decimal number to octal using print() output formatting
# The octal number of decimal number 8 is 10

number = 15
print(oct(number)[-2:])

# The octal number of decimal number 8 is 10

num = 56.85753
y = float(round(num,2))
print(y)

# Print all factors of a given number provided by the user

n = int(input("Please enter positive number: "))

for i in range(1, n+1):
    if n%i == 0:
        print(i, end=",")
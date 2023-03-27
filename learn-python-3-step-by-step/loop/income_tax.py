# Calculating Income Tax
# Income                    Tax %
# --------------------------------
# >= 0 and < 10000.0            0
# >= 10000.0 and < 25000.0     10
# >= 25000.0 and < 50000.0     20
# >= 50000.0                   30 
# If the income in < 0, program should print "Invalid Income"

income = float(input('Enter you income: '))

tax = 0.0

if income < 0:
    print('invalid income')
else:
    if income < 10000.0:
        tax = 0.0
    elif income < 25000.0:
        tax = income * 0.10
    elif income < 50000:
        tax = income * 0.20
    else:
        tax = income * 0.30
    
    print('Yout tax is: $',tax)
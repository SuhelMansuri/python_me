x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))

#if x > y:
#    m = x
#else:
#    m = y

m = x if x > y and x > z else y if y > z else z
    
print('Maximum is ', m)
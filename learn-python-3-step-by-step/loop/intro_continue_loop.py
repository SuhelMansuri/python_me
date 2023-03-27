#for i in 'Hello Wor  ld Tis is a good example to understand continue':
#    if i == ' ':
#        continue
#    print(i, end = '*')
#    
#print()
#print('End of loop')
n = int(input('Enter a number: '))
i =1
while i<= n:
    if i %2 == 0:
        i =  i + 1
        continue
    print(i, end = ' ')
    i =i + 1
    
print()
print('At the end of while')
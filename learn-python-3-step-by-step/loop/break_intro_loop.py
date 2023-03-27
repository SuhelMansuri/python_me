n = int(input("Enter a positive number: "))
 #using while loop        
i =1 
sum = 0
while i <= n:
    sum = sum + i
    if sum >= 15:
        print('for i = ', i,'breaking the loop')
        break
    i= i + 1
    
print('Sum: ', sum)

# using for loop
sum = 0
i = 1 
for i in 'HelloWorld':
    if i == ' ':
        break
    print(i, end = '*')
    
print()
print('End of loop')
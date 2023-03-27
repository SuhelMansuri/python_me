n = int(input('Please enter positive integer number of lines n: '))
row = 1
while row  <= n:
   col = 1
   while col <= row:
       print('*', end = '')
       col = col + 1
   print()
   row = row + 1
    
print('Thank you')
    
n = int(input('Please enter positive integer number of lines n: '))
row = 1
while row  <= n:
    col = n
    while col >= row:
        print('*', end = ' ')
        col = col - 1
    print()
    row = row + 1
    
print('Thank you')

n = int(input('Please enter positive integer number of lines n: '))
row = 1
while row  <= n:
    col = 1
    while col <= row:
        print(row, end = ' ')
        col = col + 1
    print()
    row = row + 1
    
print('Thank you!!!')

        

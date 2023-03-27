# program to check if a year is leap year

year = int(input('Enter year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, ' is a leap year')
else:
    print(year, ' is not a leap year')

#if year % 4 == 0:
#    #print('You are in first if block'
#    #print(year, ' may be a leap year')
#    if year % 100 == 0: 
#        if year % 400 == 0:
#            print(year, ' is a leap year')
#        else:
#            print(year, ' is not a leap year')
#    else:
#        print(year, ' is a leap year')       
#else:
#    print(year, ' is not a leap year')
        
    
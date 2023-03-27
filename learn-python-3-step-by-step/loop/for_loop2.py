#In this coding exercise you will use the for loop and the range function to print the following:

#    80-Hello Python
#    78-Hello Python
#    76-Hello Python
#    74-Hello Python
#    72-Hello Python

#You must use a for loop and range function to do this.
for i in range(80, 70, -2):
    str = 'Hello Python'
    print(i,'-',str,end='\n',sep='')
    #print(i,'-',str,end = '',sep='')
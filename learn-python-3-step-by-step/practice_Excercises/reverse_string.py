# 4. Write a program to reverse a given string.



def reverse(str): 
    rev_str = str[::-1]
    print(rev_str,' ')    
    return str
str = str(input('Enter string - '))
reverse(str)
        
    
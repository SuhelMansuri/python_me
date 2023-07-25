# 6. Write a program to check if a given string is a palindrome or not.

str = str(input('Enter string - '))
rev_str = str[::-1]
print('String - ',str)
print('Reverse_String - ',rev_str)

if str == rev_str:
    print('Given string is palindrome string')
else:
    print('Given string is not palindrome string')
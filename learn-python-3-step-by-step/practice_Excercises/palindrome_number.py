# Check Palindrome Number Write a program to check if the given number is a palindromenumber.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

n = int(input("Please enter number: "))
rev_n = str(n)[::-1]

if n == int(rev_n):
    print("Given number is palindrome number")
else:
    print("Sorry! Given number is not palindrome number")
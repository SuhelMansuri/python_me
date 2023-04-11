# Print each character of a string twice

# In this coding exercise you will print each characters of a supplied string twice. Please do exactly what is asked to pass through the auto tester. Please read the instructions carefully and try. The string my_str will be initialized by the tester, you will never need to read input. Your task will be to print each character of my_str twice.

# Example: if content of my_str is "abc", output: "aabbcc"   

# There should be NO NEWLINE at the end of the output.  

my_str = 'abc'

for i in my_str:
    print(i,end='')
    print(i,end='')
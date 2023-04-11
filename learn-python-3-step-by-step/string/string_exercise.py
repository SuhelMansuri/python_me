# Apply slicing on string - a simple exercise.

# In this coding exercise you will apply string slicing on a string as instructed. The string and other necessary parameters will be supplied by the tester, you will not write any input function to read them from the keyboard. Please read the instructions below before you start.

# Tester will initialize 2 variables in your program, the first is a string named my_str and the second is an integer named pos.  Now, please look into the example below to understand the task.

# Example 1:

# my_str = '3 abcxy'

# pos = 1

# Now, first you will need to split the string my_str on space into 2 parts, the first will contain '3' and the second 'abcxy', you will use the split method of string for this purpose.  Convert that first part (which is '3' in this case) to integer using int function.

# Now, depending on the value of pos, you need to do the following:

# when pos = 1, then takeout (using string slicing) first 3 (the first part of the string) letters from the string "abcxy" and print, otherwise, when pos = 2, then take out the portion of the string "abcxy" starting from position 3 and print into the console.

# For this example, since pos = 1, so your output should be "xyz", had pos = 2, then your output would be "xy". There should be a newline to the end of the string when you print.

# Example 2:

# my_str = '5 testingPython'

# pos = 2

# Your output should be: "ngPython" and a new line to the end.

# Example 3:

# my_str = '4 JohnRambo'

# pos = 1

# Your output should be: "John" and a new line

# Example 4:

# my_str = "0 abccba123"

# pos = 2

# output: "abccba123" and a new line

# Example 5:

# my_str = "0 abccba123"

# pos = 1

# output: "a" and a new line



my_str = '3 abcxy'
pos = 2
list = my_str.split(' ')

print(list)
a = int(list[0])
str = list[1]
# print(a)
# print(str)
if pos == 1:
    print(str[0:a:1])
if pos == 2:
    print(str[a::])
# Write a program to find the largest number in a given list.
num_list = [2,3,4,6,8,10,15,67,8,45,78,3,5,6,34,25]

largest = num_list[0]
for a in num_list:
    if a > largest:
        largest = a
print(largest)
       

# Create a new list from a two list using the following condition Given a two list of numbers, write a program 
# to create a new list such that the new list should contain odd numbers from the first list and evennumbers
# from the second list.
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l1_odd = []
l2_even = []

for i in l1:
    if i % 2 != 0:
        l1_odd.append(i)
    # else:
    #     l1_odd.append(i)
print(l1_odd)
for j in l2:
    if j % 2 == 0:
        l2_even.append(j)
print(l2_even)

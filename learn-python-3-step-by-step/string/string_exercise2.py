# Find number of strings in a list that ends with full stop '.'

# In this coding exercise you will find the count of strings in a list that has a full stop '.' at the end. The list containing the strings will be initialized and supplied by auto tester.

# Please write the code exactly as instructed, if you write anything other than what is asked then the auto tester will fail to pass your code.



str_list = ['abcd.', 'vcdfdf', 'andfsjfjs.', 'akdamkdkd.', 'Hello.']
count_fullstop = 0
i = 0
for i in str_list:
    if i.endswith('.'):
        count_fullstop = count_fullstop + 1
print(count_fullstop)


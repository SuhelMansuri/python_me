l1  = [4,5,6,2,3,9,1,4,5,6,3]

n = int(input("please enter number between 0 to 9: "))

# Using in buit method
# if n in l1:
#     print("Given number is in a list.")
# else:
#     print("Oh! Given number is not in a list.")

# for i in l1:
#     if i == n:
#         print("Given number is in a list.")
#         break
        
# else:
#         print("Oh! Given number is not in a list.")
        
###############
num_found = False
for i in l1:
    if i == n:
        num_found = True
        print("Given number is in a list.")
        break
        
if not num_found:
    print("Oh! Given number is not in a list.")
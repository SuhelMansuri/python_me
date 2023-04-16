import random

# colors = ['Light gray', 'Cyan', 'Black']
# sel_colors = random.choices(colors, weights = [40, 40, 20], k = 8)
# print(sel_colors)

my_list = list(range(100))

print(my_list)
print()
random.shuffle(my_list)
print(my_list)
print()

selecte_vals = random.sample(my_list, k = 5)
print(selecte_vals)
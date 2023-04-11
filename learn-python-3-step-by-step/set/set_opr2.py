set_a = {'c','x','d','b','b','p','a'}
set_b = {'d','p','z'}

# set_a.difference_update(set_b)
# set_a.symmetric_difference_update(set_b)
# print(set_a)
# print(set_a.isdisjoint(set_b))
# if 'd' in set_a:
#     print('d exists as member')
# else:
#     print('d is not a member')
print(set_a.issuperset(set_b) )   
print(set_b.issubset(set_a) )   
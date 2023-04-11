set_a = {10, 20, 30, 40, 50, 30, 30}
print(set_a, type(set_a), len(set_a))
# print(set_a[0])
for x in set_a:
    print(x)
set_a.add(100)
print(set_a)
set_a.add(100)
print(set_a)
# set_a.remove(20)
# set_a.discard(200)
set_a.clear()
print(set_a)
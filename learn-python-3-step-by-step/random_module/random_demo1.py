import random
min = 5
max = 12
width = max - min
for i in range(10):
    #v = random.random() * width + min # >=0 < 1, [0,1]
    #v = random.uniform(min, max)
    v = random.randint(min, max)
    print(v)
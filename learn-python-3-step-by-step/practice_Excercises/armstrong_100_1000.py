# Print all the armstrong numbers in the range of 100 to 1000
am = []
for i in range(100,1000):
   a = i % 10 # 123  3
   num = i // 10 #123 12
   b = num % 10 #12 2
   c  =num // 10 # 12 1
   sq = a**3 + b**3 + c**3
   if sq == i:
       am.append(i)
print(am)
   
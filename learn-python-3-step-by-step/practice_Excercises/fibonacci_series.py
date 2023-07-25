
i=0
add = 0

value  = []
value.append(0)
value.append(1)
for i in range(i,5,1):
        print(add,end=",")
        add = value[i] + value[i+1]
        value.append(add)
        print(value)
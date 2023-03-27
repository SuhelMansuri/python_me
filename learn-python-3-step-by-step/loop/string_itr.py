my_str = "XYZ"

for i in my_str:
    for j in my_str:
        if i != j:
            for k in my_str:
                if i != k and j != k:
                    print(i,j,k)
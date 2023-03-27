## ---- The following code will be used to initialize 
base_rate = float(input("Please enter base rate: "))
num_of_days = int(input("Please enter number of days: "))
occupancy = int(input("Please enter number of occupants: "))
view = input("Please enter view type S : Sea View(25% more on base cost) || G : Garden View(10% more on base cost) || D : Standard view(regular cost) ")

#### ---- Do not change anything in the above lines, you must use the variables base_rate, num_of_days, occupancy and view as 
### declared above and initialized by the autotester. Write your code just below.

## HINTS: You need to use if-elif

if occupancy == 1 :
    if view == 'S' :
        base_rate = base_rate + base_rate * 0.25
    elif view == 'G':
        base_rate = base_rate + base_rate * 0.10
    else:
        base_rate = base_rate + 0

elif occupancy == 2 :
    if view == 'S' :
        base_rate = base_rate + base_rate * 0.25 + base_rate * 0.20
    elif view == 'G':
        base_rate = base_rate + base_rate * 0.10 + base_rate * 0.20
    else:
        base_rate = base_rate + base_rate * 0.20
        
else: 
    if view == 'S' :
        base_rate = base_rate + base_rate * 0.25 + base_rate * 30
    elif view == 'G':
        base_rate = base_rate + base_rate * 0.10 + base_rate * 30
    else:
        base_rate = base_rate + base_rate * 30
        
base_rate = base_rate * num_of_days

base_rate = base_rate + base_rate * 0.10
print(base_rate) 
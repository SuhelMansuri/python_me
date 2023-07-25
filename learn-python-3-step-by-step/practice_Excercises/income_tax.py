# Calculate income tax for the given income by adhering to the below rules first 10k--> 0% second10 --> 10% remaining-->20%

# Expected Output:
# For example, suppose the taxable income is 45000 the income tax payable is
# 10000
# 0% + 10000
# 10% + 25000*20% = $6000.

inc = int(input("Please enter you income: "))
tax = 0
if inc <= 10000:
    tax = 0 
    print("tax ==== ",tax)
    
else:
    a = inc - 10000
    
    b = a - 10000
    t1 = (a-b) * 0.1
    t2 = b * 0.2
    tax = t1 + t2
    aft_tax_inc = inc - tax
    print("tax ==== ",tax)
    print("aft_tax_inc ==== ",aft_tax_inc)
    
    
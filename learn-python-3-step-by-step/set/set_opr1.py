cricket = {'India','England','Austalia','New Zealand','Pakistan','Bangladesh','South Africa'}
soccer = {'England','India','Bangladesh','Spain','USA'}

# either_or_both = cricket.union(soccer)
either_or_both = cricket| soccer
print(either_or_both)

# # both = cricket.intersection(soccer)
both = cricket & soccer
print(both)

# only_cricket = cricket.difference(soccer)
only_cricket = cricket - soccer
print(only_cricket)

# only_soccer = soccer.difference(cricket)
only_soccer = soccer - cricket
print(only_soccer)
# either_or = cricket.symmetric_difference(soccer)
either_or = cricket ^ soccer
print(either_or)

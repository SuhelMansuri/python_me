# The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. 
# You have to write a program to find out the population at the end of each of the last 10years. 
# For eg current population is 10000 so the output should be like this:
#10th year - 10000
#9th year - 9000
#8th year - 8100 and so on

population = 10000
print('10th year - ',population)
for i in range(9, 0, -1):
    new_pop = population - (0.1 * population)
    population = new_pop
    print(i,'th year - ', round(new_pop))
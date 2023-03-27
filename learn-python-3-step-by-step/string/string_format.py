name1 = 'Samir'
name2 = 'Aadam'
duration = 10
score1 = 90.5683
score2 = 91.6793
# str = name1 + ' and ' + name2 + ' are friends for ' + str(duration) + ' years!'


str = '{0:->10} and {1:15} are friends for {2:.^20} years, score of {0:10} is {3:10.2f}'.format(name1, name2, duration, score1, score2)
print(str)
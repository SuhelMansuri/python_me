try: 
    my_list = [1,2,3,4,5,6]
    my_list.remove(3)
    print(my_list)
    my_list.remove(100)
    print(my_list)
except ValueError as ve:
    print('Something bad happened in the try block')
    print(ve.args)
    
print('In the main flow of program')


# students = {'John' :9.97 ,'Peter' :7.87,'Tina' :8.25}
# print(students['Rambo'])
# print('This will never execute')

# age = int(input('please enter your age:'))
# if age >= 13 and age<=19:
#     print('Teen age')
# else:
#     print('Not Teen age')

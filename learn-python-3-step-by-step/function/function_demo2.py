def say_hello(name,age):
    print('--- In the function ---')
    if age <= 20:
        print('Hello!',name)
    else:
        print('Hey !',name)
    print('Welcome!', name,age)
    print('Hope you re doing well')
    print('--- Leaving the function say_hello ---')
    print()
    
print('The program started',sep=' ', end='\n')
say_hello('John', 25) # calling the function
print('Back to main flow')
say_hello('Peter', 14)
print('Bye!!!.')
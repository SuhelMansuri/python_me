import random
# for i in range(10):
#     contact = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
#     # = f'{random.randint(100,999)-555-{random.randint(1000,9999)}}'
#     print(contact)

for i in range(10):
    first_name = ['Adrian','Austine', 'Diana', 'Emily', 'John']
    last_name = ['Berry','Dickens', 'Howard', 'Langdon', 'Martin']

    f_name = random.choice(first_name)
    l_name = random.choice(last_name)
    name = f_name + ' ' + l_name
    contact = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
     
    
    print(name, '\n', contact, end='\n')
    print()
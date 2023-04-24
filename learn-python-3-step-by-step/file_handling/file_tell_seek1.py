with open('input.txt','r') as file_object:
    pos  = file_object.tell()
    print('position =',pos)
    content = file_object.read(5)
    pos  = file_object.tell()
    print('position =',pos)
    file_object.seek(10)
    pos  = file_object.tell()
    print('position =',pos)
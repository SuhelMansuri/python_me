with open('input.txt', 'r') as file_object:
    while True:
        content = file_object.read(8)
        if content == '':
            break
        print(content, end = '$')
    
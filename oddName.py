"""Marina Sugita"""
name = ''
while name.strip(' ') == '':
    name = input('Enter name: ')
print(name[::2])

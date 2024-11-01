# 

name = input("what's your name? ")

if name == 'Harry':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
elif name == 'Ron':
    print('Gryffindor')
elif name == 'Hermione':
    print('Gryffindor')
else:
    print('Who?')
#improving the code
name = input("what's your name? ")

if name == 'Harry' or name == 'Ron' or name == 'Hermione':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
else:
    print('Who?')

#making it more better using keyword match

name = input("what's your name? ")

match name:

    case 'Harry':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case 'Ron':
        print('Gryffindor')
    case 'Hermione':
        print('Gryffindor')
    case _:
        print('Who ?')

#making it more better using keyword match

name = input("what's your name? ")

match name:

    case 'Harry' | 'Ron' | 'Hermoine':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who ?')

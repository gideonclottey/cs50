# a code that checks if a number is odd or even
x= int(input('what is x? '))

if x % 2 == 0:
    print('Even')
else:
    print('odd')

#implementing using function 
def main():
    x= int(input('what is x? '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(n):
    if x % 2 == 0:
        return True
    else:
        return False
    
main()

#  Improving the code 
def main():
    x= int(input('what is x? '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(n):
    return n % 2 == 0
    
main()

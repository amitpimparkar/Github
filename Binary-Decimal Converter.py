#Binary to Decimal and Back Converter - 
#Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
def myfunc():
    choice=input('B-H OR H-B?')
    if choice=='H-B':
        h=int(input('Please enter interger to convert to binary'))
        b=bin(h)
        print(f'Binary Equivalent of {h} is {b}')
    else:
        b=(input('Please enter binary to convert to integer'))
        
        print(b)
        print(type(b))
        h=int(b,2)
        print(f'Binary Equivalent of {b} is {h}')
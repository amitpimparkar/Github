#how to calculate value of Pi upto digits given at runtime.
import math
def myfunc(n):
    x=round(math.pi,n)
    print(f'Value of Pi is: {x}' )

#how to calculate value of Pi upto digits given at runtime-2
# e instead of p (pi). Enter a number and have the program generate e up to that many decimal places.
import math

def myfunc(n):
    e=float(input('Please Enter the Number :'))
    new_e=round(e,n)
    print(f'Orginal Number {e}')
    print(f'Updated Number {new_e}')
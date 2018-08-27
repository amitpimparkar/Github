#Kangaroo Movement

def myfunc():
    x1=int(input('Enter Kangaroo1 start position'))
    x2=int(input('Enter Kangaroo2 start position'))
    v1=int(input('Enter Kangaroo1 jump distance'))
    v2=int(input('Enter Kangaroo2 jump distance'))
    print('Kangaroo1 start position:-',x1)
    print('Kangaroo2 start position:-',x2)
    print('Kangaroo1 jump distance:-',v1)
    print('Kangaroo2 jump distance:-',v2)
    print((x2 - x1) % (v1 - v2))
    if (x1 == x2) & (v1 == v2):
        print('Entering Loop1')
        print('Yes')
    elif (x1 == x2) & (v1 > v2):
        print('Entering Loop2')
        print('No')
    elif (x1 <= x2) & (v1 <= v2):
        print('Entering Loop3')
        print('No')
    elif (x2 - x1) % (v1 - v2) == 0:
        print('Entering Loop4')
        print('Yes')
    else:
        print('Entering Loop5')
        print('No')
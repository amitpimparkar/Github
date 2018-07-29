# to get prime factors of a given number
def myfunc(x):
    a=1
    #z=''
    for num in range(x):
        if num==0:
            pass
        else:
            if x%num==0:
                x=x/num
                #a+=num
                a+=x
                #z+=num
                print(num)
                #print(a)
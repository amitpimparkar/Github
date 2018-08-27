#Two Sum
def myfunc(x):
    
    t=int(input('Enter Target Value'))
    y=[]
    l=[]
    rf=False
    for i in (x):
        y.append(i)
    #print(y)
    
        diff=t-i
    #print(diff)
        if diff in x:
        
            l.append(x.index(i))
            l.append(x.index(diff))
            rf=True
            print(l)
            break
        
    if rf==False:
        print('No Result Found')
#Diagonal Difference

def myfunc()
    m=int(input("Enter the number of rows"))
    n=int(input("Enter the number of columns"))
    a=[]
    for i in range(0,n):
        a.append([])
    for i in range(0,m):
        for j in range(0,n):
            a[i].append(j)
            a[i][j]=0#Initialising to 0
    for i in range(0,m):
        for j in range(0,n):
            print('entry in row:',i+1,'column:',j+1)
            a[i][j]=int(input())#appending
    print(a)
    N=m
    sec=sum(a[i][N-i-1] for i in range(N))#a[0][n-1]+a[1][n-2]+a[2][n-3]
    fir=sum(a[i][i] for i in range(N))#a[0][0]+a[1][1]+a[2][2]
    print("Cardinality:",N)
    print("Second Diagonal Difference:",sec)
    print('\n')
    print("First Digonal DIfference:",fir)
    print('\n')
    print("Absolute DIfference:",abs(fir-sec))
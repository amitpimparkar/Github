#Longest Substring
def myfunc():
    inp=input('Please enter a string')

    x = []
    y = []
    for c in inp:#abcabcbb
        if c in x:#to find out if a char is in empty list
            y.append(''.join(x))#append
            new_ind = x.index(c) + 1#if found break the list by new index
            x = x[new_ind:]#new x
        x += c
    #print(current)
    y.append(''.join(x))
    print(y)

    longest = max(y,key=len)
    return longest
def linearSearch(l,x):
    for i in range(0,len(l)):
        if l[i] == x:
            return i
l1 = [x for x in range(0,10,2)]
print(linearSearch(l1,4))        

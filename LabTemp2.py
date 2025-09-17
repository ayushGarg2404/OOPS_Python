l1 =[]
for i in range(10) :
    l1.append(int(input()))
t1 = tuple(l1) 
print(t1)   
for elem in t1:
    primeCheck = True
    for num in range(2,elem//2):
        if(elem%num==0) :
            primeCheck = False
    if(primeCheck):
        print(elem)        
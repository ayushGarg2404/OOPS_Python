
dict = {}
t1 = (10,10,50,30,50,40)
for elem in t1:
    if(elem in dict):
        dict[elem]+=1
    else :
        dict[elem]=1
for elem in dict:
    print(elem,dict[elem])          
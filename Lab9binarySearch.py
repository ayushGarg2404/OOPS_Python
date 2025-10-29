def binarySeach(l,x,start,end):
    mid = (start+end)//2
    if l[mid] == x:
        return mid
    elif l[mid]>x:
        return binarySeach(l,x,start,mid)
    elif l[mid]<x:
        return binarySeach(l,x,mid+1,end)
l1 = [x for x in range(0,10,2)]
print(binarySeach(l1,8,0,len(l1)-1))    


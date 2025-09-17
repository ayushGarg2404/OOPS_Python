#wrte a fn which calcualte area if borth len and bred are provided. return rec area. if only len is provided return square area
def area(*params):
    if len(params)==1:
        return params[0]**2
    else:
        return params[0]*params[1]
print(area(5),area(3,4))    

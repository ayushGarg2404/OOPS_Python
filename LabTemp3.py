t1 = (10,20,30,50,60)
elem = [30,70]
for elem in elem:
    numPres = False
    for el in t1:
        if elem == el:
            numPres = True
    if numPres :
        print(f"Number {elem} is present")

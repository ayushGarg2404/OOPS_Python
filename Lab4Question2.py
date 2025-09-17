print("Enter five names: ")
l1 = []
for i in range(5) :
    l1.append(input())
l1 = sorted(l1)
for i in l1:
    print(i)    
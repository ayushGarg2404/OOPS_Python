import math
print("Enter ten integers: ")
list1 = []
max = -math.inf
min = math.inf
math.inf 
for num in range(10) :
    list1.append(int(input()))
for num in list1:
    if num>max:
        max = num
    if num<min :
        min = num
print("Max is",max)
print("Min is",min)



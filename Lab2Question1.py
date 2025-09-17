import math
x1 = int(input("Enter the first point x-coordiantes:\n"))
y1 =  int(input("Enter the first point y-coordiantes:\n"))
x2 = int(input("Enter the second point x-coordiantes:\n"))
y2 =  int(input("Enter the second point y-coordiantes:\n"))
Distance = math.pow((math.pow(x1-x2,2)+math.pow(y1-y2,2)),0.5)
print(f"Distance between the two poins is: {Distance}")
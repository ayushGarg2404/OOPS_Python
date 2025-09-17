num = int(input())
a = True
for numbers in range(1,num//2):
    if num%numbers !=0:
        a = False
if a:
    print("Number is prime")
else:
    print("Number is not prime")
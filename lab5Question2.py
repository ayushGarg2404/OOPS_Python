# a cafe allow customer to order multiple items write a function totl bill *items where each item is given as a tuple(name,price) this fn should return the total bill
def totalBill(*items):
    sum = 0
    for i in items:
        sum+=i[1]
    return sum 
print(totalBill(("Coffee",50),("Tea",30)))
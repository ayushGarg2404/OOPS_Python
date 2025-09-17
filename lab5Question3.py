# in e commerce system apply discount(price,discount) is frequently used. management asked to reduce repetive fn definition.
originalPrice_Discount = (50,5)
newPrice = lambda X: X[0]-(X[1]*X[0]/100)
print(newPrice(originalPrice_Discount))

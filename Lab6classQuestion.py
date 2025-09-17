prices = []
for i in range(4):
    prices.append(int(input()))
subtotal = sum(prices)  
discounted_subtotal = subtotal
if(subtotal>1000):
    discounted_subtotal = subtotal-(subtotal*0.1)
gst = 12/100*discounted_subtotal
grandTotal = gst+discounted_subtotal
print("original subTotal:",subtotal,"discounted subtotal:",discounted_subtotal,"tax total:",gst,"grand total:",grandTotal)     
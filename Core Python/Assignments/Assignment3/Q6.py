#Write a program to calculate profit or loss

cost_price=int(input('Enter Cost Price:'))
selling_price=int(input('Enter Selling Price:'))
if(selling_price>cost_price):
    print('Profit=',selling_price-cost_price)
elif(cost_price>selling_price):
    print('Loss=',cost_price-selling_price)
else:
    print('No Profit No Loss')
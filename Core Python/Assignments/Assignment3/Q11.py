#Accept age of five people and also per person ticket amount and then calculate total amount 
#  to ticket to travel for all of them based on following condition
# a)Children below 12= 30% discount
# b)Senior Citizen(above 59)=50% discount
# c)Other need to pay full

age=int(input('Enter 1st Person Age:'))
ticket=int(input('Enter 1st Person ticket:'))
total_price=0
if(age<12):
    total_price=total_price+(ticket-ticket*0.3)
elif(age>59):
    total_price=total_price+(ticket-ticket*0.5)
else:
    total_price=total_price+ticket


age=int(input('Enter 2nd Person Age:'))
ticket=int(input('Enter 2nd Person ticket:'))
if(age<12):
    total_price=total_price+(ticket-ticket*0.3)
elif(age>59):
    total_price=total_price+(ticket-ticket*0.5)
else:
    total_price=total_price+ticket


age=int(input('Enter 3rd Person Age:'))
ticket=int(input('Enter 3rd Person ticket:'))
if(age<12):
    total_price=total_price+(ticket-ticket*0.3)
elif(age>59):
    total_price=total_price+(ticket-ticket*0.5)
else:
    total_price=total_price+ticket


age=int(input('Enter 4th Person Age:'))
ticket=int(input('Enter 4th Person ticket:'))
if(age<12):
    total_price=total_price+(ticket-ticket*0.3)
elif(age>59):
    total_price=total_price+(ticket-ticket*0.5)
else:
    total_price=total_price+ticket


age=int(input('Enter 5th Person Age:'))
ticket=int(input('Enter 5th Person ticket:'))
if(age<12):
    total_price=total_price+(ticket-ticket*0.3)
elif(age>59):
    total_price=total_price+(ticket-ticket*0.5)
else:
    total_price=total_price+ticket

print('Total Ticket Amount=',total_price)


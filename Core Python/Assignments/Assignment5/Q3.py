#Accept no. of passengers from user and per ticket cost.The accept age of each passenger and 
#then calculate total amount to ticket to travel for all of them based on following condition
# a)Children below 12= 30% discount
# b)Senior Citizen(above 59)=50% discount
# c)Other need to pay full

n=int(input('Enter Number of Passengers:'))
i=1
total_ticket=0
while i<=n:
    age=int(input(f'Enter the Age of {i} Person:'))
    ticket=int(input(f'Enter the Ticket of {i} Person:'))
    if(age<12):
        total_ticket+=ticket-ticket*0.3
    elif(age>59):
        total_ticket+=ticket-ticket*0.5
    else:
        total_ticket+=ticket
    i=i+1
print('Total Amount of Ticket=',total_ticket)

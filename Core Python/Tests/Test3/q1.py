# A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

amount=int(input('Enter a Amount:'))
D=[2000,500,200,100,50,20,10,5]
for i in D:
    note=amount//i
    amount=amount%i
    print('Note',i,'=',note)
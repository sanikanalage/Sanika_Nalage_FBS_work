#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount

#Take amount from user
amount=int(input('Enter amount:'))

#Perform Operation
n500=amount//500
amount=amount%500
n200=amount//200
amount=amount%200
n100=amount//100
amount=amount%100
n50=amount//50
amount=amount%50
n20=amount//20
amount=amount%20
n10=amount//10
amount=amount%10

#Display result
print(f'500 Notes={n500}')
print(f'200 Notes={n200}')
print(f'100 Notes={n100}')
print(f'50 Notes={n50}')
print(f'20 Notes={n20}')
print(f'10 Notes={n10}')
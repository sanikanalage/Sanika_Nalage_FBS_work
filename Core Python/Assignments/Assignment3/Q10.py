#write a program to check if person is eligible to marry or not(male age>=21 and 
# female age>=18)

gender=input('Enter Gender(male/female):')
age=int(input('Enter Age:'))

if(gender=='female'):
    if(age>=18):
        print('Eligible for Marriage.')
    else:
        print('Not Eligible for Marriage.')
else:
    if(age>=21):
        print('Eligible for Marriage.')
    else:
        print('Not Eligible for Marriage.')
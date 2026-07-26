gender=input('Enter Gender(m/f):')
age=int(input('Enter Age:'))

if(gender=='f'):
    if(age>=18):
        print('Eligible for Marriage.')
    else:
        print('Not Eligible for Marriage.')
else:
    if(age>=21):
        print('Eligible for Marriage.')
    else:
        print('Not Eligible for Marriage.')
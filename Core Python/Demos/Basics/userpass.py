import random
userId=input('Enter the User ID:')
password=input('Enter the Password:')
if (userId=="sanika" and password=="Sanika@22"):
    captcha=random.randint(1000,9999)
    print(f'Your Captcha={captcha}')
    chuser=int(input('Enter the Captcha='))
    if chuser==captcha:
        print('User Login Successfully.')
    else:
        print('Invalid Captcha')
else:
    print('User is Invalid.')
#Write a program to prompt user to enter userid and password.After verifying userid and
# password display a 4 digit random number and ask user to enter the same.If user enters 
# same number thenshow him success message otherwise failed.(Something like Captcha) 

import random
userId=input('Enter UserId:')
password=input('Enter password:')
if(userId=='sanikanalage' and password=='Sanika@22'):
    captcha=random.randint(1000,9999)
    print('Captcha=',captcha)
    user_captcha=int(input('Enter Captcha:'))
    if(user_captcha==captcha):
        print('Login Successfully.')
    else:
        print('Invalid Captcha.')
else:
    print('Invalid UserId and Password.')
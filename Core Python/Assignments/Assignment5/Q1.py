#Write a program to prompt user to enter userid and password.If Id and password is incorrect
#  give me him chance to re-enter the credentials.Let him try 3 times.After that program to 
#  terminate.

userid='sanika'
password='Sanika@22'
attempt=1
while attempt<=3:
    uid=input('Enter User Id:')
    pwd=input('Enter Password:')
    if(uid==userid and pwd==password):
        print('Login Successful.')
        break
    else:
        print('Invalid UserId or Password.')
        attempt+=1
if(attempt==4):
    print('Program Terminated')
#Que11.WAP to check if a given number is Armstrong number or not.

def chkArmstrong(num):
    count=len(str(num))
    temp=num
    sum=0
    while(temp>0):
        d=temp%10
        sum+=d**count
        temp//=10
    if(sum==num):
        print(f'{num} is Armstrong Number.')
    else:
        print(f'{num} is not Armstrong Number.')
num=int(input('Enter Number:'))
chkArmstrong(num)
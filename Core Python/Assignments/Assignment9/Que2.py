#Que2 Write a program to check if given number is Armstrong or not using recursive function

def chkArmstrong(num):
    if(num>0):
        d=num%10
        return d**count + chkArmstrong(num//10)
    else:
        return 0
num=int(input('Enter Number:'))
count=len(str(num))
res=chkArmstrong(num)
if(res==num):
    print(f'{num} is Armstrong Number.')
else:
    print(f'{num} is not Armstrong Number.')
#WAP to check if given number is Armstrong or not

num=int(input('Enter Number:'))
count=len(str(num))
temp=num
sum=0
while(num>0):
    d=num%10
    sum=sum+(d**count)
    num=num//10
if(temp==sum):
    print(f'{temp} is Armstrong Number.')
else:
    print(f'{temp} is not Armstrong Number.')
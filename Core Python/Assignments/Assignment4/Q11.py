#WAP to check if given number strong number

num=int(input('Enter Number:'))
temp=num
sum=0
while(num>0):
    d=num%10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if(temp==sum):
    print(f'{temp} is Strong Number.')
else:
    print(f'{temp} is not Strong Number.')
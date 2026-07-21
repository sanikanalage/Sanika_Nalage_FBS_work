#WAP to check if given number is perfect number

num=int(input('Enter Number:'))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(num==sum):
    print(f'{num} is Perfect Number.')
else:
    print(f'{num} is not Prime Number.')
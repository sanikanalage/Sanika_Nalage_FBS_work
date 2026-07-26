num=int(input('Enter a number:'))
sum=0
while(num>0):
    d=num%10
    sum=sum+d
    num=num//10
print(f'Sum of Digits in number={sum}')
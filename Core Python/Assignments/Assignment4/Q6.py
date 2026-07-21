#WAP to check if a given number is prime number or not

num=int(input('Enter Number:'))
if(num>1):
    for i in range(2,num//2+1):
        if(num%i==0):
            print(f'{num} is not Prime Number.')
            break
    else:
        print(f'{num} is Prime Number.')
else:
    print(f'{num} is not Prime nor Composite.')

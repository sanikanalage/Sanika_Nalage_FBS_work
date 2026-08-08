#Que8. Write a program to check whether a number is prime or not using recursion

def prime(num,i):
    if(num==i):
        return True
    if(num%i==0):
        return False
    return prime(num,i+1)

num=int(input('Enter a Number:'))
if(num>1):
    res=prime(num,2)
    if res:
        print(f'{num} is Prime Number.')
    else:
        print(f'{num} is not Prime Number.')
else:
    print(f'{num} is not Prime Number.')
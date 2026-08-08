#Que7. Write a program to find sum of digits using recursion

def sumDigit(num):
    if(num>0):
        d=num%10
        return d + sumDigit(num//10)
    else:
        return 0
num=int(input('Enter Number:'))
res=sumDigit(num)
print('Sum of Digits =',res)
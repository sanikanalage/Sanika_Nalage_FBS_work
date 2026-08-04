#Que7.Wrie a program to find sum of digits of a number

def sumDigits(num):
    sum=0
    while(num>0):
        d=num%10
        sum+=d
        num//=10
    return sum
num=int(input('Enter a Number:'))
print('Sum of Digits =',sumDigits(num))
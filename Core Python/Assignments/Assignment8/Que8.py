#Que8.Wrie a program to find reverse of a number

def reverse(num):
    rev=0
    while(num>0):
        d=num%10
        rev=rev*10+d
        num//=10
    return rev
num=int(input('Enter a Number:'))
print('Reverse Number =',reverse(num))

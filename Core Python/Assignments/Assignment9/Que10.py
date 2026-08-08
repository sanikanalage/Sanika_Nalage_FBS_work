#Que.10 Write a program to reverse a number using recursion.

def reverse(num,rev):
    if(num>0):
        d=num%10
        rev=rev*10+d
        return reverse(num//10,rev)
    else:
        return rev

num=int(input('Enter Number:'))
res=reverse(num,0)
print('Reverse Number=',res)
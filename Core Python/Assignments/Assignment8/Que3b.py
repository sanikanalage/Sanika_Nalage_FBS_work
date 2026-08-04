# Que3. Write a program to find sum of following series using function
# b)1!+2!+3!+4!+______+n!

def sumfact(n):
    sum=0
    fact=1
    for i in range(1,n+1):
        fact*=i
        sum+=fact
    return sum
n=int(input('Enter n:'))
res=sumfact(n)
print('Sum=',res)
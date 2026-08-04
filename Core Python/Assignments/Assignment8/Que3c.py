# Que3. Write a program to find sum of following series using function
# c)1^1+2^2+3^3+4^4+______+n^n

def powerSum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i**i
    return sum
n=int(input('Enter n:'))
res=powerSum(n)
print('Sum =',res)
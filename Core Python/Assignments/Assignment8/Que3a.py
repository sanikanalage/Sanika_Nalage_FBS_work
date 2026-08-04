# Que3. Write a program to find sum of following series using function
# a)1+2+3+4+______+n

def sumSeries(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
n=int(input('Enter n:'))
res=sumSeries(n)
print('Sum of Series=',res)
# Que4.Sum of all odd numbers between 1 to n

def oddSum(n):
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum
n=int(input('Enter n:'))
res=oddSum(n)
print('Sum =',res)
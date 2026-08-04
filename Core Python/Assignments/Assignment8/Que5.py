#Que5.Sum of all prime numbers between 1 to n

def primeSum(n):
    sum=0
    for i in range(1,n+1):
        if(i>1):
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                sum+=i
    return sum
n=int(input('Enter n:'))
res=primeSum(n)
print('Sum = ',res)
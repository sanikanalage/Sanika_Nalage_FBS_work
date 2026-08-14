n=int(input('Enter n:'))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(i/fact)
print('Sum of Series:',sum)
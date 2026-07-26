x=int(input('Enter the Number:'))
n=int(input('Enter the n:'))
dem=1
sign=1
sum=0
for i in range(1,n+1):
    sum+=sign*(x**i/dem)
    dem+=2
    sign*=-1
print('Sum of Series:',sum)
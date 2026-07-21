#WAP to print sum of series upto n
n=int(input('Enter n:'))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f'The Sum of 1 to {n} Numbers is {sum}.')
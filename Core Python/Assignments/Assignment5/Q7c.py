#Write a program to solve the following series

#c)Find the sum of geometric series from 1 to n where the common ratio is 2

n=int(input('Enter n:'))
term=1
sum=0
for i in range(1,n+1):
    sum=sum+term
    term=term*2
print(f'The Sum of Geometric Series from 1 to {n} is {sum}')
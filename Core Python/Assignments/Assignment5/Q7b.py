#Write a program to solve the following series

#b) N+N^2+N^3+N^4+______+N^N(here ^ means Exponent)

N=int(input('Enter N:'))
sum=0
for i in range(1,N+1):
    sum=sum+(N**i)
print('Sum of Series=',sum)

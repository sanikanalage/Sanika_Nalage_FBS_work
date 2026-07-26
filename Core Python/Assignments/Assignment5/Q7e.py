#Write a program to solve the following series

#d) X - X^2/3 + X^3/5 - X^4/7 +______to n terms

x=int(input('Enter the Number:'))
n=int(input('Enter the Ending Value:'))
dem=1
sign=1
sum=0
for i in range(1,n+1):
    sum+=sign*(x**i)/dem
    dem+=2
    sign*=-1
print('Sum of Series=',sum)

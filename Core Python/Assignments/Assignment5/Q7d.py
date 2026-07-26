#Write a program to solve the following series

#d) s=a+a^2/2+a^3/3+_____+a^10/10

a=int(input('Enter a:'))
sum=0
for i in range(1,11):
    sum=sum+((a**i)/i)
print('The Sum Of Series=',sum)
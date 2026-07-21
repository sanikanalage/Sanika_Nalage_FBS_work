#WAP to print factorial of a number

num=int(input('Enter Number:'))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f'The Factorial of {num} is {fact}.')
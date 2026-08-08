#Que5. Write a program to find factorial using recursion


def factorial(num):
    if(num>0):
        return num * factorial(num-1)
    else:
        return 1
num=int(input('Enter Number:'))
res=factorial(num)
print(f'Factorial of {num} is =',res) 
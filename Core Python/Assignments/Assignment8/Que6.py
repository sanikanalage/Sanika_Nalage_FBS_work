#Que6.Write a program to print the following fibonacci series using functions 
# 0 1 1 2 3 5 8 n terms

def fibonacci(n):
    a=-1
    b=1
    for i in range(n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
n=int(input('Enter n:'))
print('Fibonacci Series:')
fibonacci(n)
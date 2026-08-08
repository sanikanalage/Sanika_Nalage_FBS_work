#Que6. Write a program to print fibonacci series using recursion

def fabonacci(n,a,b):
    if(n>0):
        c=a+b
        print(c,end=' ')
        return fabonacci(n-1,b,c)
n=int(input('Enter number of terms:'))
print('Fibonacci Series:')
fabonacci(n,-1,1)
#Que1. Write a program to find sum of following series  using recursive functions:
#    i)1!+2!+3!+_____+n!
#Note-for fact and sum two recursive functions


def fact(n):
    if(n>0):
        return n * fact(n-1)
    else:
        return 1
def sumFact(n):
    if(n>0):
        return fact(n) + sumFact(n-1)
    else:
        return 0

n=int(input('Enter n:'))
res=sumFact(n)
print('Sum of Series:',res)
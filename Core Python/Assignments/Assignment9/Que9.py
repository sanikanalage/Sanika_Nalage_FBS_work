#Que9. Write aprogram to calculate the m to the power n using recursion

def power(m,n):
    if(n>0):
        return m * power(m,n-1)
    else:
        return 1
m=int(input('Enter Value of m:'))
n=int(input('Enter Value of n:'))
res=power(m,n)
print(f'{m} raised to the power of {n} = {res}')
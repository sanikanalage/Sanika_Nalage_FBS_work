#Que15.Python Program to find larger string without using built-in functions

n=int(input('Enter Number of Strings:'))
large=''
for i in range(n):
    s=input('Enter String:')
    count=0
    for j in s:
        count+=1
    large_count=0
    for j in large:
        large_count+=1
    if count>large_count:
        large=s
print('Larger String=',large)
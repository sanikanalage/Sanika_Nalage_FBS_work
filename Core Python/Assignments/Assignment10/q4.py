#Que4.Write a program to reverse a list

li=[10,20,30,40,50]
rev=[]
for i in range(len(li)-1,-1,-1):
    rev=rev+[li[i]]
print('Original List =',li)
print('Reverse List =',rev)

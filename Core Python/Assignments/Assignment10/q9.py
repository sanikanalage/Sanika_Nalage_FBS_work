#Que9.Write a program to having  n number of elements in the list and find out even and odd elements in that list and 
#and then create two separate lists which will have even elements and other will have odd elements

n=int(input('Enter number of Elements:'))
li=[]
for i in range(n):
    num=int(input('Enter Element:'))
    li+=[num]
even=[]
odd=[]
for i in range(0,len(li)):
    if(li[i]%2==0):
        even+=[li[i]]
    else:
        odd+=[li[i]]
print('Original List =',li)
print('Even list =',even)
print('Odd List =',odd)
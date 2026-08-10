#Que10.Write a program to remove all occurrences of a given element in the list

li=[10,20,10,30,10,40,20]
num=int(input('Enter Element to remove:'))
new=[]
for i in range(0,len(li)):
    if(li[i]!=num):
        new+=[li[i]]
print('Original List =',li)
print('After Removing =',new)

#Que7.Write a program to create a new list from existing list.Which contain cube of each number of list

li=[1,2,3,4,5,6]
new=[]
for i in range(0,len(li)):
    new+=[li[i]**3]
print('Original List =',li)
print('New list =',new)
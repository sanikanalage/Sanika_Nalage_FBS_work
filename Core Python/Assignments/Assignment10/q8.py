#Que8. Write a program to create a dupliacate of an existing list. It should not point to same list.

li=[10,20,30,40]
new=[]
for i in range(0,len(li)):
    new+=[li[i]]
print('Original list =',li)
print('Duplicate list =',new)
print(li is new)
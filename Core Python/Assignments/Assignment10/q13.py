#que13.Write a program to print list after removing even numbers

li=[56,23,90,12,25,60]
new=[]
for i in range(0,len(li)):
    if(li[i]%2!=0):
        new+=[li[i]]
print('Original List =',li)
print('List after removing even numbers =',new)
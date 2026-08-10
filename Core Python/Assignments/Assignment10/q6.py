#Que6.Write a program to remove duplicates from the list

li=[10,20,10,30,20,40,30]
new=[]
for i in range(0,len(li)):
    count=0
    for j in range(i):
        if(li[i]==li[j]):
            count+=1
    if count==0:
        new+=[li[i]]
print('Original list =',li)
print('After removing duplicates =',new)
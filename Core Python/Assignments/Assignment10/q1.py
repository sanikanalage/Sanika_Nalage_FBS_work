#Que1.Write a program to find sum of all elements of list.

li=[10,20,30,40]
sum=0
for i in range(0,len(li)):
    sum+=li[i]
print('Sum of all elements of list =',sum)
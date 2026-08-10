#Que1. Python Program to put Even and odd Elements of list into two different lists

li=[52,23,96,28,69,72]
even=[]
odd=[]
for i in range(0,len(li)):
    if(li[i]%2==0):
        even.append(li[i])
    else:
        odd.append(li[i])
print('Original List =',li)
print('Even list =',even)
print('Odd List =',odd)
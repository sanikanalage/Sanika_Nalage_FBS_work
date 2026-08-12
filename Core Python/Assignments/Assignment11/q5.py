#Que5. Python Program to sort a List According to the length of the elements within the list 

li = ["apple", "cat", "banana", "hi", "mango"]
print('Original List =',li)
for i in range(1,len(li)):
    for j in range(0,len(li)-1):
        if(len(li[j])>len(li[j+1])):
            li[j],li[j+1]=li[j+1],li[j]
print("Sorted List =", li)
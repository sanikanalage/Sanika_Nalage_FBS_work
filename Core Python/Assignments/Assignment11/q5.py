#Que5. Python Program to sort a List According to the length of the elements within the list 

li = ["apple", "cat", "banana", "hi", "mango"]
print('Original List =',li)
li.sort(key=len)
print("Sorted List =", li)
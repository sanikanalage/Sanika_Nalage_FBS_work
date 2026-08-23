#Que3 Write a Python Program to find all the unique words and count the frequency of occurence from a given list of 
# strings.Use Python set data type

li=['python','java','python','c','java','python']
s=set(li)
print('List=',li)
print('Unique Words=',s)
for word in s:
    count=li.count(word)
    print(word,'=',count)

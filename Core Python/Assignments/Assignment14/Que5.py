#Que5.Write a Python program to find the longest common prefix of all strings.Use the Python set.

li=['flow','flower','flour']
s1=set()
s2=set()
s3=set()
for i in range(1,len(li[0])+1):
    s1.add(li[0][:i])
for i in range(1,len(li[1])+1):
    s2.add(li[1][:i])
for i in range(1,len(li[2])+1):
    s3.add(li[2][:i])
common=s1.intersection(s2,s3)
longest=''
for word in common:
    if len(word)>len(longest):
        longest=word
print('Strings=',li)
print('Longest common prefix=',longest)

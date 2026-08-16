#Que12.Python Program to count number of lowercase characters in a string

#Without using Method
# s=input('Enter string:')
# count=0
# for i in s:
#     if(i>='a' and i<='z'):
#         count+=1
# print('Number of Lowercase Characters=',count)

#With using Method
s=input('Enter String:')
count=0
for i in s:
    if i.islower():
        count+=1
print('Number of Lowercase Characters=',count)
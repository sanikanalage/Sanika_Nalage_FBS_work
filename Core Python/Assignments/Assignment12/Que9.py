#Que9.Python Program to calculate the Numbers of Words and Number of Characters Present in a string.

#Without using method
# s=input('Enter String:')
# countch=0
# countw=1
# for i in s:
#     if(i!=' '):
#         countch+=1
#     if(i==' '):
#         countw+=1
# print('Number of Words=',countw)
# print('Number of Characters=',countch)

#With using method
s=input('Enter String:')
words=len(s.split())
characters=len(s.replace(' ',''))
print('Number of Words=',words)
print('Number of Charcters=',characters)
#Que3.Python Program to Detect if Two strings are Anagram

#Without using Method
# s1=input('Enter First String:')
# s2=input('Enter Second String:')
# counts1=0
# counts2=0
# if(len(s1)!=len(s2)):
#     print('Not Anagram')
# else:
#     for ch in s1:
#         for i in s1:
#             if ch==i:
#                 counts1+=1
#         for j in s2:
#             if ch==j:
#                 counts2+=1
#     if(counts1==counts2):
#         print('Anagram')
#     else:
#         print('Not Anagram')

#With Using Method
s1=input('Enter First String:')
s2=input('Enter Second String:')
if(sorted(s1)==sorted(s2)):
    print('Anagram')
else:
    print('Not Anagram')
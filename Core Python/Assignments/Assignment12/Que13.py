#Que13. Python Program to count number of digits and letters in a string

#Without using Method
# s=input('Enter String:')
# countd=0
# countl=0
# for i in s:
#     if (i>='0' and i<='9'):
#         countd+=1
#     elif ((i>='a' and i<='z') or (i>='A' and i<='Z')):
#         countl+=1
# print('Number of Digits=',countd)
# print('Number of letters=',countl)

#Without using Method
s=input('Enter String:')
countd=0
countl=0
for i in s:
    if i.isdigit():
        countd+=1
    elif i.isalpha():
        countl+=1
print('Number of Digits=',countd)
print('Number of letters=',countl)

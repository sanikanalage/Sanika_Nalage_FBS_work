#Que4. Python Program to form a New String Where the first character and the Last character have been Exchanged.

#Without using Method
# s=input('Enter String:')
# new=s[len(s)-1]
# for i in range(1,len(s)-1):
#     new=new+s[i]
# new=new+s[0]
# print('Original String:',s)
# print('New String:',new)

#With using Method
s=input('Enter String:')
new=s[len(s)-1]+s[1:len(s)-1]+s[0]
print('Original String:',s)
print('New String:',new)

#Que6.Python Proram to take in a string and replace every blank space with hyphen.

#Without using Method
# s=input('Enter String:')
# new=''
# for i in s:
#     if i==' ':
#         new=new+'-'
#     else:
#         new=new+i
# print('Original String=',s)
# print('New String=',new)


#With using Method
s=input('Enter String:')
res=s.replace(' ','-')
print('Original String=',s)
print('New String=',res)


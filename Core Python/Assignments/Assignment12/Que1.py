#Que1.Python Program to replace all occurrence of 'a' with '$' in a string

# s=input('Enter String:')
# new=''
# for i in s:
#     if i=='a':
#         new=new+'$'
#     else:
#         new=new+i
# print('Original String=',s)
# print('New String=',new)


s=input('Enter String:')
res=s.replace('a','$')
print('Original String=',s)
print('New String=',res)
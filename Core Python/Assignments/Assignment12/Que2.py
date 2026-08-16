#Que2. Python Program to remove all nth Index Character from a None-Empty String

#Without using method
# s=input('Enter String:')
# n=int(input('Enter Index you want to remove:'))
# new=''
# for i in range(0,len(s)):
#     if i!=n:
#         new=new+s[i]
# print('Original String:',s)
# print('New String:',new)

#With using method
s=input('Enter String:')
n=int(input('Enter Index you want to remove:'))
new=s[:n]+s[n+1:]
print('Original String:',s)
print('New String:',new)

#Que8. Python Program to remove the characters of odd Index values in a string

#Without using Method
s=input('Enter String:')
new=''
for i in range(0,len(s)):
    if i%2==0:
        new=new+s[i]
print('Original String=',s)
print('New String=',new)

#With using Method
s=input('Enter String:')
res=s[::2]
print('Original String=',s)
print('New String=',res)
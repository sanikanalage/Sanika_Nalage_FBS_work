str=input('Enter String:')
rev=''
for i in range(len(str)-1,-1,-1):
    rev+=str[i]
if(str==rev):
    print('String is Palindrome.')
else:
    print('String is not palindrome.')
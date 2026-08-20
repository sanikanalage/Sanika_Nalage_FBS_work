str1=input('Enter First String:')
str2=input('Enter Second String:')
if(len(str1)==len(str2)):
    di={}
    for i in str1:
        if i in di:
            di[i]=di[i]+1
        else:
            di[i]=1
    for i in str2:
        if i in di:
            di[i]=di[i]-1
        else:
            di[i]=-1
    for i in di:
        if di[i]!=0:
            print('not anagram')
            break
    else:
        print('Anagram')
else:
    print('Not Anagram')


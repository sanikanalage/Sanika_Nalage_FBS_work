str1=input('Enter First String:')
str2=input('Enter Second String:')
if(len(str1)==len(str2)):
    di1={}
    for i in str1:
        if i in di1:
            di1[i]=di1[i]+1
        else:
            di1[i]=1
    di2={}
    for i in str2:
        if i in di2:
            di2[i]=di2[i]+1
        else:
            di2[i]=1
    if(di1==di2):
        print('Anagram')
    else:
        print('Not Anagram')
else:
    print('Not Anagram')

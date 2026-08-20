# #Method1-Using Method

# a=input('Enter string 1:')
# b=input('Enter string 2:')
# li1=list(a)
# li2=list(b)
# li1.sort()
# li2.sort()
# if(li1==li2):
#     print('Anagram')
# else:
#     print('Not Anagram')


#Method2-Without using Methods

a=input('Enter string 1:')
b=input('Enter string 2:')
counta=0
countb=0
if(len(a)!=len(b)):
    print('Not anagram.')
else:
    for ch in a:
        for i in a:
            if ch==i:
                counta+=1
        for j in b:
            if ch==j:
                countb+=1
    if counta==countb:
        print('Anagram')
    else:
        print('This is not Anagram.')


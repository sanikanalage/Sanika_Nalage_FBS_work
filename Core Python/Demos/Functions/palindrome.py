def chkpalindrome():
    num=int(input('Enter Number:'))
    temp=num
    rev=0
    while(num>0):
        d=num%10
        num=num//10
        rev=rev*10+d
    if(rev==temp):
        print(f'{temp} is Palindrome Number.')
    else:
        print(f'{temp} is not Palindrome Number.')

chkpalindrome()
chkpalindrome()
chkpalindrome()
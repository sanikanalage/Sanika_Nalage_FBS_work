def chkPalindrome(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        rev=rev*10+d
        temp//=10
    if(rev==num):
        return True
    else:
        return False

data=[603,59695,1551,790,262]
res=list(map(chkPalindrome,data))
print(res)
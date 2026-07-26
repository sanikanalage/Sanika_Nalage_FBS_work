n=int(input('Enter a number:'))
temp=n
rev=0
while(n>0):
    d=n%10
    n=n//10
    rev=rev*10+d
if(rev==temp):
    print('Number is Palindrome.')
else:
    print('Number is not Palindrome.')
#Que9.Wrie a program to check if entered number is a palindrome or not

def chkPalindrome(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        rev=rev*10+d
        temp//=10
    if(rev==num):
        print(f'{num} is Palindrome.')
    else:
        print(f'{num} is not Palindrome.')
num=int(input('Enter Number:'))
chkPalindrome(num)
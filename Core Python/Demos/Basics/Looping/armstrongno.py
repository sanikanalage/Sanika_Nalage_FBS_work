#Write a program to check Armstrong Number
no=int(input('Enter a Number:'))
count=len(str(no))
temp=no
total=0
while(no>0):
    d=no%10
    total+=(d**count)    #total=total+(d**count)
    no=no//10
print(total)
if(temp==total):
    print('The Number is Armstrong.')
else:
    print('The Number is not Armstrong. ')
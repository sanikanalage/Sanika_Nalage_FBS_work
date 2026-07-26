#WAP to print Armstrong number within a given range

start=int(input('Enter Strating Number:'))
end=int(input('Enter Ending Number:'))
for num in range(start,end+1):
    temp=num
    count=len(str(num))
    sum=0
    while(num>0):
        d=num%10
        sum=sum+(d**count)
        num=num//10
    if(sum==temp):
        print(temp)

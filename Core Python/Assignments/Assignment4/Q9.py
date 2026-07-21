#WAP to print all numbers in a range divisible by a given number

num=int(input('Enter Number:'))
start=int(input('Enter Starting Number:'))
end=int(input('Enter Ending number:'))
for i in range(start,end+1):
    if(i%num==0):
        print(i)
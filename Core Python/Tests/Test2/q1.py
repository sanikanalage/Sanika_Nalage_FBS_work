# Que1 Write a program to find first n primenumbers. 


# n=int(input('Enter n:'))
# for i in range(1,n+1):
#     if i!=1:
#         for j in range(2,i//2):
#             if i%j==0:
                
#                 break
#         else:
#             print(i)


n=int(input('Enter n:'))
count=0
num=2
while count<n:
    for i in range(2,num//2):
        if num%i==0:
                break                           
    else:
        print(num)
        count+=1
    num+=1
#Que5.Accept a number from user and check if this element is present in the list or not.
# Also tell how many times it is present in the list

li=[10,20,10,30,10,40,20]
num=int(input('Enter number:'))
count=0
for i in range(0,len(li)):
    if(li[i]==num):
        count+=1
if count>0:
    print('Element is Present')
    print('Number of times =',count)
else:
    print('Element is not Present')

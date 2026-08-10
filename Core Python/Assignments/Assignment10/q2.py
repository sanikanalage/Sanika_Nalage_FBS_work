#Que2.Write a program to find maximum and minimum element in a list.

li=[62,46,3,79,16,30]
max=li[0]
min=li[0]
for i in range(0,len(li)):
    if(li[i]>max):
        max=li[i]
    if(li[i]<min):
        min=li[i]
print('Maximum Element =',max)
print('Minimum Element =',min)
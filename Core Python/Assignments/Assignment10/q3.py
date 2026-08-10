#Que3.Write a program to find the second largest element in the list

li=[62,46,3,79,82,16,93]
max=li[0]
second_max=li[0]
for i in range(0,len(li)):
    if(li[i]>max):
        second_max=max
        max=li[i]
    elif(li[i]>second_max):
        second_max=li[i]
print('Second Largest Element in the List =',second_max)
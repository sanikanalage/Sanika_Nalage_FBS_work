def bubbleSort(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
                print(li)
    
li=[60,50,40,30,20,10]
print('Before Sorting:',li)
bubbleSort(li)
print('After Sorting:',li)
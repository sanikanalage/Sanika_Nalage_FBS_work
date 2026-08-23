#Que4.Write a Python Program that finds all pairs of elements in a list whose sum is equal to a given value

li=[2,4,3,5,7,8,9]
target=int(input('Enter target sum value:'))
pairs=set()
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==target:
            pairs.add((li[i],li[j]))
print('List=',li)
print('Target=',target)
print(f'Pairs whose sum is {target} = {pairs}')
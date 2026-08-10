#Que3.Python Program to sort the list According to the second element in sublist

li = [[2, 3], [6, 2], [1, 1], [3, 4]]

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i][1] > li[j][1]:
            li[i],li[j] =li[j],li[i]

print("Sorted list:", li)
#Que4. Python Program to find the Second Largest Number in a list Using Bubble sort

li = [52,7,22,90,82,12]

for i in range(1,len(li)):
    for j in range(0, len(li)-1):
        if li[j] > li[j + 1]:
            li[j],li[j+1] = li[j+1],li[j]

print("Sorted list:", li)
print("Second largest number:", li[-2])
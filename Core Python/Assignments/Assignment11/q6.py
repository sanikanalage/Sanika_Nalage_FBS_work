#Que6. Python Program to find the Union Of two Lists

li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]

union = li1.copy()

for i in li2:
    if i not in union:
        union.append(i)

print("List 1 =", li1)
print("List 2 =", li2)
print("Union =", union)
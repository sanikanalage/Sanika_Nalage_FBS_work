# Que 5.Python Program to Find the Union of two Lists without
# using set concept.

# li1=[10,20,30,40]
# li2=[50,60,70,80]
# print("li1",li1)
# print("li2",li2)
# print('Union= ',li1+li2)


li1 = [10,20,30,40]
li2 = [30,40,50,60]
li3 = []
for i in li1:
    li3.append(i)
for i in li2:
    if i not in li3:
        li3.append(i)
print("li1",li1)
print("li2",li2)
print("Union =", li3)
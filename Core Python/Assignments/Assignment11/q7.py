#Que.7 Python Program to Find the Intersection of two lists

li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]

intersection = []

for i in li1:
    if i in li2:
        intersection.append(i)

print("List 1 =", li1)
print("List 2 =", li2)
print("Intersection =", intersection)
#Que10.Write a program to print list after removing even numbers.

li = [45,62,10,59,21,74]

new = li.copy()

for i in li:
    if i % 2 == 0:
        new.remove(i)

print("Original List =", li)
print("After Removing Even Numbers =", new)
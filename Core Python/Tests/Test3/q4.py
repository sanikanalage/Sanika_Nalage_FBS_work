# Que 4.There is a list with some numbers. Create a new
# dictionary using this list in such a way that key is
# number and value is frequency of occurrence of that
# number in list.
# [1,3,4,1,2,3,6,7,1,2,4]
# {1:3,3:2,2:2,4:2,6:1,7:1}

li=[1,3,4,1,2,3,6,7,1,2,4]
dict={}

for i in li:
    count=0
    for j in li:
        if i==j:
            count+=1
    dict[i]=[count]
print(dict)


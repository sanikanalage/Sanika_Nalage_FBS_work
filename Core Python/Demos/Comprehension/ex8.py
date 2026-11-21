li=[2,3,4,16]
dict={}
for i in li:
    dict[i]=i**2
print(dict)

li=[2,3,4,16]
dict={i:i**2 for i in li}
print(dict)


li=[2,3,4,16]
dict={i:i**2 for i in li if i%2==0}
print(dict)

x=10
y=10
z=20
li1=[10,20]
li2=[10,20]
#1.is
print(x is y)
print(id(x))
print(id(y))

print(li1 is li2)
print(id(li1))
print(id(li2))

t1=(10,20)
t2=(10,20)

print(t1 is t2)
print(id(t1))
print(id(t2))

#2.is not
print(x is not z)
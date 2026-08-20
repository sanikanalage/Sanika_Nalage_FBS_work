#1.structure:Denoted by []
li=[10,20,30,40]
print(type(li))

#2.type of data:heterogenous
li=[10,3.14,'abc']
print(li)

#3.sequence: Ordered

#4.Changable:Mutable
print(id(li))
li[1]=17.63
print(id(li))
print(li)

#5.Duplication:allowed

li=[10,10,20,30,20,10]
print(li)
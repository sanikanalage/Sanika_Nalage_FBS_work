#Que6.Python Program to Multiply All the Items in a dictionary

#Without using method
d={'a':2,'b':3,'c':4,'d':5}
mul=1
for i in d:
    mul*=d[i]
print('Dictionary=',d)
print('Multipliaction of all Items=',mul)

#With using method
d={'a':2,'b':3,'c':4,'d':5}
mul=1
for i in d.values():
    mul*=i
print('Dictionary=',d)
print('Multipliaction of all Items=',mul)
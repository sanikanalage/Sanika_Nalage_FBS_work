#Que5.Python Program to sum All the Items in a Dictionary

#Without using method
d={'a':10,'b':20,'c':30}
sum=0
for i in d:
    sum+=d[i]
print('Dictionary=',d)
print('Sum of all Items=',sum)

#With using method
d={'a':10,'b':20,'c':30}
sum=0
for i in d.values():
    sum+=i
print('Dictionary=',d)
print('Sum of all Items=',sum)
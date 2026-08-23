#Que2. Write a python program to remove the intersection of a second set with a first set

s1={10,20,30,40}
s2={30,40,50,60}
print('first set=',s1)
print('Second Set=',s2)
s1.difference_update(s2)
print('Set 1 after removing intersection=',s1)
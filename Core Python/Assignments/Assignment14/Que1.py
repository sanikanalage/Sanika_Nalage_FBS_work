#Que1.Write a program to find elements in a given set that are not in another set.

s1={10,20,30,40}
s2={20,40,60,80,100}
res=s1.difference(s2)
print('Set 1=',s1)
print('Set 2=',s2)
print('Elements in set 1 but not in set2=',res)
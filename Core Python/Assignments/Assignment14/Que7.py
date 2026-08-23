#Que7.Give two sets of numbers,write a Python program to find the missing numbers in the second set as compared to the 
#  first and vice versa.Use the python set.

s1={10,20,30,40,50}
s2={20,40,60,80,100}
print('first set=',s1)
print('Second set =',s2)
missing_in_s2=s1.difference(s2)
missing_in_s1=s2.difference(s1)
print('Missing in Set 2 =',missing_in_s2)
print('Missing in set 1 =',missing_in_s1)
#Que10. Python Program to take in two strings and display the larger string without using Built-in Functions

s1=input('Enter First String:')
s2=input('Enter Second String:')
counts1=0
counts2=0
for i in s1:
    counts1+=1
for i in s2:
    counts2+=1
if(counts1>counts2):
    print('Larger String=',s1)
elif(counts2>counts1):
    print('Larger String=',s2)
else:
    print('Both Strings are equal.')


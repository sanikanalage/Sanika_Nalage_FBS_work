#Que1.Python Program to add a Key-Value Pair to the Dictionary

#Without using built-in functions
# d={'id':101,'name':'Sanika','age':21}
# key=input('Enter Key:')
# value=input('Enter Value:')
# print('Original Dictionary:',d)
# d[key]=value
# print('Updated Dictionary:',d)


#With using built-in functions
d={'id':101,'name':'Sanika','age':21}
key=input('Enter Key:')
value=input('Enter Value:')
print('Original Dictionary:',d)
d.update({key:value})
print('Updated Dictionary:',d)
#Que7.Python Program to remove the Given key from a Dictionary

d={'id':101,'name':'Sanika','age':21,'city':'satara'}
key=input('Enter Key to remove:')
print('Dictionary=',d)
if key in d:
    d.pop(key)
    print('Updated Dictionary:',d)
else:
    print('Key does not Exist')
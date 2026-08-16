#Que3.Python Program to check if a Given Key Exists in a Dictionary or not

#Without using method
d={'id':101,'name':'Sanika','age':21,'city':'Satara'}
key=input('Enter Key to search:')
if key in d:
    print('Key exists in Dictionary.')
else:
    print('Key does not exists in Dictionary.')

#With using method
d={'id':101,'name':'Sanika','age':21,'city':'Satara'}
key=input('Enter Key to search:')
if(d.get(key)!=None):
    print('Key exists in Dictionary.')
else:
    print('Key does not exists in Dictionary.')
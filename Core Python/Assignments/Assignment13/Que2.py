#Que2.Python Program to concatenate Two Dictionaries into one

#Without using method
# d1={'a':10,'b':20}
# d2={'c':30,'d':40}
# d={}
# for key in d1:
#     d[key]=d1[key]
# for key in d2:
#     d[key]=d2[key]
# print('Dictionary 1:',d1)
# print('Dictionary 2:',d2)
# print('Concatenated Dictionary:',d)

#With using method
d1={'a':10,'b':20}
d2={'c':30,'d':40,'a':20}
print('Dictionary 1:',d1)
d1.update(d2)
print('Dictionary 2:',d2)
print('Concatenated Dictionary:',d1)
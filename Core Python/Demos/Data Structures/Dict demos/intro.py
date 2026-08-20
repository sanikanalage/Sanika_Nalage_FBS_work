#1.Structure:denoted by {}
di={1:'Python' ,'Released':1991 ,'Developer':'Guido van rossum'}
print(type(di))

#2.Type of data: Heterogenous
print(di)

#3.Sequence: Orderd
print(di)

#4.Changeble: key-Immutable , value-Mutable , dict:size-Mutable
di[1]='Python Programming'
di[3]=100
di[1]='Java'
print(di)

#Duplication: keys-Unique , values-duplication allowed
di1={1:'Python' ,'Released':1991 ,'Developer':'Guido van rossum', 1:'Java', 3:1991}
print(di1[1])
# 1.Structure : denoted by ({})
fs=frozenset({10,20,30,40})
print(type(fs))

#2.Type of data: Heterogenous
fs=frozenset({10,3.14,'Sanika'})
print(fs)

#3.Sequence: Unordered
fs=frozenset({10,3.14,'Sanika',30,20,'a'})
print(fs)

#4.Changeble: Immutable
# fs.add(50)  raise error

#5.Duplication: Unique

fs=frozenset({10,3.14,10,'a','Sanika',30,20,'a'})
print(fs)

fs1=frozenset({10,20,30,40})
fs2=frozenset({30,40,50,60})
fs3=frozenset({50,60})

fs4=fs1.copy()
print(fs4)
print(fs1.difference(fs2))
print(fs1.intersection(fs2))
print(fs3.issubset(fs2))
print(fs2.issuperset(fs3))
print(fs1.isdisjoint(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.union(fs2))



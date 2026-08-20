#1.Structure : Denoted by {}, set()

# s1={}
# print(type(s1))          #<class 'dict'>
# s1=set()
# print(type(s1))          #<class 'set'>

#2.Type of data : Heterogenous
s1={22,85,'sanika',3.14,'A',21.10,78}
# print(s1)                                    #{3.14, 85, 22, 21.1, 'sanika', 78, 'A'}

#3.Sequence: Unordered

# print(s1)                                    #{3.14, 85, 22, 21.1, 'sanika', 78, 'A'}

#4.Changeble :Mutable,Not Replaceable
s1.add(80)
print(s1)

#5.Unique
s2={22,85,'sanika',22,3.14,22,'A',21.10,'A',78}
print(s2)

#Que4.Python Program to generate a Dictonary that contains Numbers(between 1 to n) in the form(x:x*x).

#Without using method
# n=int(input('Enter n:'))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print('Dictionary=',d)


#With using method
n=int(input('Enter n:'))
d={}
for i in range(1,n+1):
    d.update({i:i*i})
print('Dictionary=',d)
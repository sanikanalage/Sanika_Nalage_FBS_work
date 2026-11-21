# Transforming

# li=[3,9,18,45,20]
# newli=[]
# for i in li:
#     if(i%2==0):
#         newli.append('even')
#     else:
#         newli.append('odd')
# print(li)
# print(newli)

li=[3,9,18,45,20]
newli=['even' if x%2==0 else 'odd' for x in li]
print(li)
print(newli)


# start=int(input('Enter Start number:'))
# end=int(input('Enter End number:'))
# li=[]
# newli=[]
# for i in range(start,end+1):
#     li.append(i)
#     newli.append(i**0.5)
# print('Old List=',li)
# print('New List=',newli)

start=int(input('Enter Start number:'))
end=int(input('Enter End number:'))
li=[x for x in range(start,end+1)]
newli=[x**0.5 for x in range(start,end+1)]
print('Old List=',li)
print('New List=',newli)


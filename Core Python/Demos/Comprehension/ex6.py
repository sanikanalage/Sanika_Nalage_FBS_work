# Filtering
# start=int(input('Enter Start number:'))
# end=int(input('Enter End number:'))
# li=[]
# for i in range(start,end+1):
#     if(i%2!=0):
#         li.append(i*i)
# print(li)

start=int(input('Enter Start number:'))
end=int(input('Enter End number:'))
li=[i**2 for i in range(start,end+1) if i%2!=0]
print(li)

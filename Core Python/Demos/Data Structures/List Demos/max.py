li=[45,34,81,77,53,34,26,82]

max=li[0]
for ind in range(1,len(li)):
    if(li[ind]>max):
        max=li[ind]

print('Maximum Element=',max)
# for i in range(1,6):
#     for j in range(6-i,0,-1):
#         if(i==1 or j==1 or j==6-i):
#             print(j,end=' ')
#         else:
#             print(' ',end=' ')
#     print()

for i in range(1,6):
    for j in range(6-i,0,-1):
         if(i==1 or j==1 or i+j==6):
             print(j,end=' ')
         else:
             print(' ',end=' ')
    print()


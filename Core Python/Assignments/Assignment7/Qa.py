#Que.1 Write a program to print following patterns.
#a)       * 
#       *   * 
#     *       *
#   *           *
# *               *
# *               *
#   *           *
#     *       *
#       *   *
#         *

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        if(j==1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,i):
        if(i-j==1):
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()   

for i in range(1,6):
    for j in range(1,i):
        print(' ',end=' ')
    for j in range(1,7-i):
        if(j==1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,6-i):
        if(i+j==5):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,6):
    for j in range(1,i):
        print(' ',end=' ')
    for j in range(i,6):
        print('*',end=' ')
    for j in range(1,6-i):
        print('*',end=' ')
    print()
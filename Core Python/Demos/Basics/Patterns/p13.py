for i in range(1,6):
    for j in range(1,6):
        if((i==2 or i==3 or i==4) and (j==2 or j==3 or j==4)):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
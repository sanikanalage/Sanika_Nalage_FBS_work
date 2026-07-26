for i in range(1,6):
    for j in range(1,7-i):
        if(i==1 or j==1 or i+j==6):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Write a program print following patterns-
# e)         A
#          A B C
#        A B C D E
#      A B C D E F G
#    A B C D E F G H I

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    k=1+i
    for j in range(1,i):
        print(chr(64+k),end=' ')
        k=k+1
    print()

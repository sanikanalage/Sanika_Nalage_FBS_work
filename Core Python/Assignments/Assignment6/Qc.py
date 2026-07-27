#Write a program print following patterns-
# c)     1
#      1   1
#    1   2   1
#   1  3   3   1

for i in range(1,5):
    k=1
    for j in range(1,5-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(' ',k,end=' ')
        k=k*(i-j)//j
    print()
    
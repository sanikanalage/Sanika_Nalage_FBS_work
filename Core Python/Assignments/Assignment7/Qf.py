#Que.1 Write a program to print following patterns.
#f) 1 2 3 4 5 
#   2     5 
#   3   5 
#   4 5 
#   5        


for i in range(1,6):
    for j in range(i,6):
        if(i==1 or j==5 or i==j):
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
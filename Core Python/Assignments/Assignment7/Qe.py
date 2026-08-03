#Que.1 Write a program to print following patterns.
#e)       1   
#       1   2   
#     1       3   
#   1           4   
# 1   2   3   4   5   


for i in range(1,6):
   
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        if(i==5):
            print(j,end='   ')
        elif(j==1 or i==j):
            print(j,end='   ')
        else:
            print(' ',end='   ')
    print()
    
    

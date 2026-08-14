#Que4. Write a program to print pattern
#  1 0 1 0 1
#  0 1 0 1 0
#  1 0 1 0 1
#  0 1 0 1 0
#  1 0 1 0 1

for i in range(1,6):
    for j in range(1,6):
        if(i%2!=0 and j%2!=0):
            print('1',end=' ')
        elif(i%2==0 and j%2==0):
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
#Que12. Write a program to create three lists of numbers,their squares and cubes

li=[1,2,3,4,5]
squares=[]
cubes=[]
for i in range(0,len(li)):
    squares+=[li[i]**2]
    cubes+=[li[i]**3]
print('Numbers =',li)
print('Squares =',squares)
print('Cubes =',cubes)
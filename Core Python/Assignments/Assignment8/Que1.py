#Que1. Write a program to calculate area of rectangle

def areaRectangle(length,breadth):
    return length*breadth
l=int(input('Enter Length of Rectangle:'))
b=int(input('Enter Breadth of Rectangle:'))
res=areaRectangle(l,b)
print('Area of Rectangle=',res)
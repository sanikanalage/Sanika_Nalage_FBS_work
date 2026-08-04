#Que2. Write a program to calculate area of circle

def areaCircle(radius):
    return 22/7*radius*radius
r=int(input('Enter radius of circle:'))
res=areaCircle(r)
print('Area of Circle=',res)
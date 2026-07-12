#WAP to calculate area of triangle and rectangle

#Take base and height of triangle
base=float(input('Enter Base of Triangle:'))
height=float(input("Enter Height of Triangle:"))

#Calculate area of triangle
area_triangle=(base*height)/2

#Take length and breadth of rectangle
length=float(input('Enter Length of Rectangle:'))
breadth=float(input('Enter Breath of Rectangle:'))

#Calculate area of rectangle
area_rectangle=length*breadth

#Display Result
print(f'Area of Triangle is {area_triangle} and Area of Rectangle is {area_rectangle}.')

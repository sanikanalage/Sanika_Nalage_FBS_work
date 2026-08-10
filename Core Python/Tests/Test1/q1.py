#1.Write a program to find the area and perimeter of following figure(Accept the length,breadth and radius from user)


l=int(input('Enter length:'))
b=int(input('Enter breadth:'))
r=int(input('Enter radius:'))
area=(l*b)+(0.5*(22/7)*r*r)
perimeter=l+l+b+(22/7*r)
print('Area =',area)
print('Perimeter =',perimeter)
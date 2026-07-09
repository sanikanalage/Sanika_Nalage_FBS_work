#Write program to find the Roots of a Quadratic Equation.
#Take input for a,b,and c
a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
c=int(input('Enter value of c:'))

#Calculate Discriminant
d=b*b-4*a*c

#Calculate Roots
r1=(-b+(d**0.5))/(2*a)
r2=(-b-(d**0.5))/(2*a)

#Display Result
print(f'Roots of Quadratic Equation is {r1} and {r2}.')


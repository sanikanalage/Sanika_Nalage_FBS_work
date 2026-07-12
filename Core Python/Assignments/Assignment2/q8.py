#write a program to swap two numbers using third variable

#Take two numbers 
m=int(input('Enter number 1:'))
n=int(input('Enter number 2:'))

print(f'Before Swapping: m={m} and n={n}')

#perform operation
t=m
m=n
n=t

#Display result
print(f'After Swapping: m={m} and n={n}')
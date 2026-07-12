#Write a program to swap two numbers without using third variable

#Take two numbers
m=int(input('Enter number 1:'))
n=int(input('Enter number 2:'))

print(f'Before Swapping: m={m} and n={n}')

#perform operation
m=m+n
n=m-n
m=m-n

#Display result
print(f'After Swapping: m={m} and n={n}')
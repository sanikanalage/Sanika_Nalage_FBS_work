#Que9. Write a program to create three lists of numbers,their squares and cubes.

numbers = [1, 2, 3, 4, 5]

squares = []
cubes = []

for i in numbers:
    squares.append(i ** 2)
    cubes.append(i ** 3)

print("Numbers =", numbers)
print("Squares =", squares)
print("Cubes =", cubes)
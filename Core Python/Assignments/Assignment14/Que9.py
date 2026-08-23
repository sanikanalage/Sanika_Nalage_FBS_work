#Que9.Write a python program to find all the unique combinations of 3 numbers from a given list of numbers,adding up 
# to a target number.

numbers = [2, 4, 7, 9, 3, 6, 5, 8]
target = 18
print('List of Numbers:',numbers)
print('Target:',target)
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):

            if numbers[i] + numbers[j] + numbers[k] == target:
                print(numbers[i], numbers[j], numbers[k])
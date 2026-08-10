#Que11. Write a program to print all numbers which are divisible by m and n in list.

li=[10,30,12,15,28,21,16,36]
m=int(input('Enter m:'))
n=int(input('Enter n:'))
print(f'Numbers divisible by {m} and {n}:')
for i in range(0,len(li)):
    if(li[i]%m==0 and li[i]%n==0):
        print(li[i])
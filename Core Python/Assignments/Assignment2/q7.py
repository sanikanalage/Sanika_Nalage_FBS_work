#Find the sum of three-digit number

#take three-digit number
num=int(input('Enter Three-Digit Number:'))
#store original num in another variable
temp=num

#Find digits
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
num=num//10

#Calulate sum
sum=d1+d2+d3

#Display result
print(f'The Sum of {temp} is {sum}.')
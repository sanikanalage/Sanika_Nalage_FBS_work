#write a program to reverse three-digit number

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

#Perform Operation
reverse=(d1*100)+(d2*10+d3)

#Display Result
print(f'Reverse of {temp} is {reverse}.')


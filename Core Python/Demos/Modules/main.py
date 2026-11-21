# #1)direct import-import module name
# import calculator        
# num1=int(input('Enter number 1:'))
# num2=int(input('Enter number 2:'))
# calculator.add(num1,num2)
# calculator.sub(num1,num2)
# calculator.mul(num1,num2)
# calculator.div(num1,num2)
# print(calculator.x)

# #2.from modulename import member
# from calculator import add
# num1=int(input('Enter number 1:'))
# num2=int(input('Enter number 2:'))
# add(num1,num2)

# #3.from modulename import multiple members
# from calculator import add,sub,x
# num1=int(input('Enter number 1:'))
# num2=int(input('Enter number 2:'))
# add(num1,num2)
# sub(num1,num2)
# print(x)

# #4.from modulename import all things
# from calculator import *
# num1=int(input('Enter number 1:'))
# num2=int(input('Enter number 2:'))
# add(num1,num2)
# sub(num1,num2)
# mul(num1,num2)
# div(num1,num2)
# print(x)


#5.By using alice name
import calculator as c
c.add(10,2)
print(c.x)


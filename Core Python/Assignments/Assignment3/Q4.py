#Write  a program to input all sides of a triangle and check whether triangle is valid or not

first_side=int(input('Enter First side of Triangle:'))
second_side=int(input('Enter Second side of Triangle:'))
third_side=int(input('Enter Third side of Triangle:'))
if((first_side+second_side>third_side) and (first_side+third_side>second_side) and
   (second_side+third_side>first_side)):
    print('Triangle is Valid.')
else:
    print('Triangle is not Valid.')
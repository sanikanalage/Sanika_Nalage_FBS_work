#Write a program to check whether the triangle is equilateral,isoscales or scalene triangle

first_side=int(input('Enter First side of Triangle:'))
second_side=int(input('Enter Second side of Triangle:'))
third_side=int(input('Enter Third side of Triangle:'))
if(first_side==second_side==third_side):
    print('Triangle is Equilateral.')
elif((first_side==second_side) or (first_side==third_side) or (second_side==third_side)):
    print('Triangle is Isoscales.')
else:
    print('Triangle is Scalene.')
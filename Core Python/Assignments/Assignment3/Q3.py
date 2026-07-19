#Write a program to input angle of a triangle and check whether triangle is valid or not

first_angle=int(input('Enter First Angle of Triangle:'))
second_angle=int(input('Enter Second Angle of Triangle:'))
third_angle=int(input('Enter Third Angle of Triangle:'))
if((first_angle+second_angle+third_angle)==180):
    print('Triangle is Valid.')
else:
    print('Triangle is not Valid.')
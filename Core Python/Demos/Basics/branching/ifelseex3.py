first_angle=int(input('Enter First Angle of Triangle:'))
second_angle=int(input('Enter Second Angle of Triangle:'))
third_angle=int(input('Enter Third Angle of Triangle:'))
sum=first_angle+second_angle+third_angle
if(sum==180):
    print('The Triangle is Valid.')
else:
    print('The Triangle is not Valid.')
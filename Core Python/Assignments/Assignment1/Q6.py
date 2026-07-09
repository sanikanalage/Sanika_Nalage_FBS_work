#Write program to input two angles from user and find third angle of the triangle
#Take input first and second angle

FA=int(input('Enter First angle of triangle:'))
SA=int(input('Enter Second angle of triangle:'))

#Perform Operation
Third_angle=180-(FA+SA)

#Display Result
print(f'Third angle of the Triangle is {Third_angle}.')
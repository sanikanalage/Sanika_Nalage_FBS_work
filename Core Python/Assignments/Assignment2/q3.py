#Convert distant given in feet and inches into meter and centimeter

#Take feet and inches
feet=int(input('Enter Feet:'))
inches=int(input('Enter Inches:'))

#Perform Operation
#Calculate Total Inches
total_inches=(feet*12)+inches
#Convert inches into meter and centimeter
meter=total_inches*0.0254
centimeter=meter*100

#Display Result
print(f'Meter={meter} and Centimeter={centimeter}')
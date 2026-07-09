#Write program to convert days into years,weeks and days.
#Take days
Days=int(input('Enter Days:'))


#calculate years
Years=Days//365
#calculate remaining days
Days=Days%365
#calculate weeks
Weeks=Days//7
#calculate left days
Days=Days%7

#Display Result
print(f'Years={Years},Weeks={Weeks} and Days={Days}')
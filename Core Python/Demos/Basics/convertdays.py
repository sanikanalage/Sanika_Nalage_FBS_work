#Take days
Days=int(input('Enter Days:'))


#Perform Operation
Years=Days//365
Days=Days%365
Weeks=Days//7
Days=Days%7

#Display Result
print(f'Years={Years},Weeks={Weeks} and Days={Days}')
#Write program to enter P,T,R and calculate Simple Interest.
#Take input P,R,T
P=int(input('Enter Principal amount:'))
R=int(input('Enter Rate of interest:'))
T=int(input('Enter Time of years:'))

#Perform Operation
SI=(P*R*T)/100

#Display Result
print('Simple Interest:',SI)
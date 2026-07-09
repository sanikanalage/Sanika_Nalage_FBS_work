#Write program to enter P,T,R and calculate Compound Interest.
#Take input P,R,T
P=int(input('Enter Principal amount:'))
R=int(input('Enter Rate of interest:'))
T=int(input('Enter Time of years:'))

#Perform Operation
Amount=P*(1+R/100)**T
CI=Amount-P

#Display Result
print('Compound Interest:',CI)
print(f'Compound Interest:'+str(CI))
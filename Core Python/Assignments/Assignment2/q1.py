#Convert the time entered in hh,min,sec into seconds

#Take input hours,minutes and seconds
hours=int(input('Enter Hours:'))
minutes=int(input('Enter Minutes:'))
seconds=int(input('Enter Seconds:'))

#Perform Operation
total_seconds=(hours*3600)+(minutes*60)+seconds

#Display Result
print(f'Total Seconds is {total_seconds}.')
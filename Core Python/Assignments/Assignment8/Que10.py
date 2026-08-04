# Que10.Write a program to check if entered year is leap year or not

def chkLeap(year):
    if((year%400==0)or(year%4==0 and year%100!=0)):
        print(f'{year} is a Leap Year.')
    else:
        print(f'{year} is not Leap Year.')
year=int(input('Enter Year:'))
chkLeap(year)
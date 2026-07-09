#Write a program to calculate the percentage of student based on marks of any 5 subjects
#Take input marks of 5 subjects
sub1=int(input('Enter marks of Subject 1:'))
sub2=int(input('Enter marks of Subject 2:'))
sub3=int(input('Enter marks of Subject 3:'))
sub4=int(input('Enter marks of Subject 4:'))
sub5=int(input('Enter marks of Subject 5:'))

#Perform Operation
#Calculate Total marks of all subjects
total=sub1+sub2+sub3+sub4+sub5

#Calculate Percentage
#Percentage=total/subjects
percentage=total/5

#display result
print(f'Percentage is {percentage}.')
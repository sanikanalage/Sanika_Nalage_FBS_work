#Input 5 Subject marks from user and display grade(e.g.First Class,second class,....)

s1=int(input('Enter Marks in Subject1:'))
s2=int(input('Enter Marks in Subject2:'))
s3=int(input('Enter Marks in Subject3:'))
s4=int(input('Enter Marks in Subject4:'))
s5=int(input('Enter Marks in Subject5:'))
total=s1+s2+s3+s4+s5
percentage=total/500*100

if(percentage>=60):
    print('First Class')
elif(percentage>=50):
    print('Second Class')
elif(percentage>=40):
    print('Third Class')
elif(percentage>35):
    print('Pass Class')
else:
    print('Fail')

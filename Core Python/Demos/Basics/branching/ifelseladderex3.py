s1=int(input('Enter Marks in Subject1:'))
s2=int(input('Enter Marks in Subject2:'))
s3=int(input('Enter Marks in Subject3:'))
s4=int(input('Enter Marks in Subject4:'))
s5=int(input('Enter Marks in Subject5:'))
percentage=(s1+s2+s3+s4+s5)/500*100
print(percentage)

if(percentage>=85):
    print('First Class')
elif(percentage>=65):
    print('Second Class')
elif(percentage>35):
    print('Third Class')
else:
    print('Fail')

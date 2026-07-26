#Enter number of students from user.for those many students accept marks of 5 subject marks 
# from user and calculate percentage and average percentage of students

n=int(input('Enter Number of Students:'))
total_per=0
for i in range(1,n+1):
    print('Student',i)
    total=0
    for j in range(1,6):
        marks=int(input(f'Enter Marks of Subject {j}:'))
        total=total+marks
    per=total/500*100
    print('Percentage=',per)
    total_per=total_per+per
average=total_per/n
print('Average Percentage=',average)

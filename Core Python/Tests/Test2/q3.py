#Que3 Write a program to accpet basic salary of n  emp.(n should be accepted from user.)If basic salary is below 20000
#  then da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%.Based on this calculate the total salary of each 
# emp and also total salary of all emp.


n=int(input('Enter n emp:'))
total_all=0
for i in range(1,n+1):
    basic_salary=int(input(f'Enter Basic salary of employee {i}:'))
    if basic_salary<20000:
        da=basic_salary*10/100
        ta=basic_salary*12/100
        hra=basic_salary*15/100
        total_salary=basic_salary+da+ta+hra        
    else:
        da=basic_salary*15/100
        ta=basic_salary*18/100
        hra=basic_salary*20/100
        total_salary=basic_salary+da+ta+hra
    total_all+=total_salary
    print(f'Total Salary of emp{i}={total_salary}')
print(f'Total Salary of all employee={total_all}')
        
    

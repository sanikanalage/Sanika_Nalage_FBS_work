#WAP calculate total salary of employee based on basic,da=10% of basic,ta=12% of basic,hra=15%of basic.

#Take basic salary of employee
basic=float(input('Enter Basic Salary:'))

#Calculate total salary
da=basic*10/100
ta=basic*12/100
hra=basic*15/100
total_salary=basic+da+ta+hra

#Display Result
print(f'Total Salary of Employee is {total_salary}.')

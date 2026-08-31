# Que 3. A list contains sublist with Emp information as follows :
# Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
# [210,”Tannu”,14000],[320,”Suresh”,35000]]
# Write a program to sort the list based on salary.

data = [[101,"Seema",45000],[340,'Rajan',13000],[210,"Tannu",14000],[320,"Suresh",35000]]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i][2]>data[j][2]:
            data[i][2],data[j][2]=data[j][2],data[i][2]
print(data)
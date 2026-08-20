def emp(id,name,sal,dept):
    data='ID: ' + str(id) +'\n'
    data+='NAME: ' + str(name) + '\n'
    data+='SAL: ' + str(sal) + '\n'
    data+='DEPARTMENT: ' + str(dept) + '\n'
    return data
res=emp(name='Sanika',id=101,dept='AI Engineer',sal=35000)
print(res)
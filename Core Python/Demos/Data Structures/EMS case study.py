def addEmp(id,name,salary,dept):
    if(id not in all_emp_details):
        all_emp_details[id]=[id,name,salary,dept]
        return 'Employee added Successfully.'
    else:
        return 'ID already Exist.'

def showAllEmp():
    print("-" * 60)
    print(f"{'ID':<10}{'NAME':<15}{'SALARY':<15}{'DEPARTMENT':<15}")
    print("-" * 60)

    for emp in all_emp_details.values():
        print(f"{emp[0]:<10}{emp[1]:<15}{emp[2]:<15}{emp[3]:<15}")

    print("-" * 60)

def updateEmp(id):
    print("NOTE: If don't want to change leave field blank.")
    emp=all_emp_details.get(id)
    if(emp):
        name = input(f'Enter New NAME({emp[1]}):') or emp[1]
        sal=input(f'Enter New SALARY({emp[2]}):') or emp[2]
        dept = input(f'Enter New DEPARTMENT({emp[3]}):') or emp[3]
        all_emp_details[id] = [id,name,sal,dept]
        return 'Employee Updated Successfully.'
    else:
        return 'ID not found.'

def deleteEmp(id):
    emp=all_emp_details.pop(id,None)
    if(emp):
        return 'Employee Deleted Successfully.'
    else:
        return 'ID not found'

def searchEmp(id):
    emp=all_emp_details.get(id)
    if(emp):
        return emp
    else:
        return 'ID not Found.'

def empManage():
    print('#####Employee Manage#####')
    ch=0
    while(ch != '6'):
        print('''Please select option from below:
        1.Add employee
        2.Show all employee
        3.Update employee
        4.Delete employee
        5.Search employee
        6.Logout
        ''')
        ch=input('Enter choice:')
        if(ch == '1'):
            while True:
                id=input('Enter ID:')
                if id.isdigit():  
                    break
                else:
                    print('ID only allowed in digit')
            name=input('Enter NAME:')
            while True:
                salary=input('Enter SALARY:')
                if salary.isdigit():  
                    break
                else:
                    print('Salary only allowed in number')
            dept=input('Enter DEPARTMENT:')
            res=addEmp(id,name,salary,dept)
            print(res)
        elif(ch == '2'):
            showAllEmp()
        elif(ch == '3'):
            print('ID not allowed to update...')
            id=input('Enter ID:')
            res=updateEmp(id)
            print(res)
        elif(ch == '4'):
            id=input('Enter ID:')
            res=deleteEmp(id)
            print(res)
        elif(ch == '5'):
            id=input('Enter ID:')
            res=searchEmp(id)
            print(res)
        elif(ch == '6'):
            print('Logged Out....')
        else:
            print('Invalid choice...')        

def login():
    print('#####Login Page#####')
    uid='admin'
    passw='1234'
    username=input('Enter USERNAME:')
    password=input('Enter PASSWORD:')
    if(uid == username and passw == password):
        print('Logged in Successful...')
        empManage()
    else:
        print('Invalid Credentials...')

def main():
    ch=0
    while(ch != '2'):
        print('#####DASHBOARD#####')
        print('''Please select option from below:
        1.Login(Admin)
        2.Exit
        ''')
        ch=input('Enter choice:')
        if (ch == '1'):
            login()

        elif(ch == '2'):
            print('Thank you for choosing us!')
        else:
            print('Invalid Choice...')


all_emp_details = {}
main()


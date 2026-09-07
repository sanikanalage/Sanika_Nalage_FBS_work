from empmanage import EmployeeManagement
class Login:
    def login():
        emg=EmployeeManagement()
        uid='admin'
        passw='1234'
        username=input('Enter USERNAME:')
        password=input('Enter PASSWORD:')
        if(uid == username and passw == password):
            print('Logged in Successful...')
            while True:
                print('Enter 1 for Add Emp')
                print('Enter 2 for Display Emp')
                print('Enter 3 for Search Emp')
                print('Enter 4 for Update Emp')
                print('Enter 5 for Delete Emp')
                print('Enter 6 for Exist')
                ch=int(input('Enter the Choice='))
                if ch==1:
                    emg.addEmp()
                elif ch==2:
                    emg.displayEmp()
                elif ch==3:
                    emg.SearchEmp()
                elif ch==4:
                    emg.UpdateEmp()
                elif ch==5:
                    emg.deleteEmp()
                elif ch==6:
                    print("Thank You")
                    break
                else:
                    print("Invalid Choice")
        else:
            print('Invalid Credentials...')
Login.login()
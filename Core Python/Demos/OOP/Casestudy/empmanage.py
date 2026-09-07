from hr import Hr
from dev import Dev
from emp import Emp
class EmployeeManagement:
    def __init__(self):
        self.edetails={}
    def addEmp(self):
        empid=int(input("Enter the Id of Emp:"))
        if empid in self.edetails:
            print("Emp Allready Exist.")
            return
        else:
            name=input('Enter Name of Emp:')
            salary=float(input('Enter Salary of Emp:'))
            print('1. HR')
            print('2. Developer')
            choice=int(input('Enter Your Choice='))
            if choice==1:
                com=float(input('Enter the Commission of HR:'))
                emp=Hr(empid,name,salary,com)
            elif choice==2:
                bonus=float(input('Enter the Bonus of Developer:'))
                emp=Dev(empid,name,salary,bonus)
            else:
                print("Invalid Choice...")
                return
            self.edetails[empid]=emp
            print("Employee Added Successfully")

    def displayEmp(self):
        if len(self.edetails)==0:
            print("Employee not Exist...")
        else:
            for emp,empobj in self.edetails.items():
                print(emp,empobj)

    def SearchEmp(self):
        if len(self.edetails)==0:
            print("Employee not Exist...")
        else:
            eid=int(input('Enter the Id of Employee:'))
            if eid in self.edetails:
                print("EmpDetail=",self.edetails[eid])
            else:
                print(f"Employee with {eid} is not Present")
                
    def UpdateEmp(self):
        if len(self.edetails)==0:
            print("Employee not Exist...")
        else:
            eid=int(input('Enter the Id of Employee:'))
            if eid in self.edetails:
                print("1. Update Name")
                print("2. Update Salary")
                print("3. Update Commission/Bonus")


                ch = int(input("Enter Your Choice:"))

                if ch == 1:
                    name = input("Enter New Name:")
                    self.edetails[eid].setName(name)

                elif ch == 2:
                    salary = float(input("Enter New Salary:"))
                    self.edetails[eid].setSal(salary)

                elif ch == 3:
                    emp = self.edetails[eid] 
                    if emp.__class__.__name__ == "Hr": 
                        com = float(input("Enter New Commission:")) 
                        emp.setCommission(com)
                    else: 
                        bonus = float(input("Enter New Bonus:")) 
                        emp.setBonus(bonus)

                else:
                    print("Invalid Choice...")
                    return

                print("Employee Updated Successfully")

            else:
                print(f"Employee with {eid} is not Present")
                
    def deleteEmp(self):
        if len(self.edetails)==0:
            print("Employee not Exist...")
        else:
            eid=int(input('Enter the Id of Employee:'))
            if eid in self.edetails:
                del self.edetails[eid] 
                print("Employee Deleted Successfully")
            else:
                print(f"Employee with {eid} is not Present")




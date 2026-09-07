#Que1. Create a derived class from Student as EnggStudent with :
#  a. data members as:
#       i.Branch
#       ii.InternalMarks
#  b.   Add the following methods:
#       i.Parameterized constructor
#       ii.Display
#       iii.Accept
#       iv.override Method CalculateRank
#       v.Override__str__Method

class Student:
    def __init__(self,studentid,name,age,percentage):
        self.studentid=studentid
        self.name=name
        self.age=age
        self.percentage=percentage

    def accept(self):
        self.studentid=int(input('Enter Student ID:'))
        self.name=input('Enter Name of Student:')
        self.age=int(input('Enter Age of Student:'))
        self.percentage=float(input('Enter Percentage:'))

    def getStudentID(self):
        return self.studentid
    def setStudentID(self,newStudentID):
        self.studentid=newStudentID

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getAge(self):
        return self.age
    def setAge(self,newAge):
        self.age=newAge

    def getPercentage(self):
        return self.percentage
    def setPercentage(self,newPercentage):
        self.percentage=newPercentage


    def display(self):
        print(f'ID:{self.studentid}\nName:{self.name}\nAge:{self.age}\nPercentage:{self.percentage}\nRank:{self.CalculateRank()}')

    def CalculateRank(self):
        if self.percentage>=75:
            return "Distinction"
        elif self.percentage>=60:
            return "First Class"
        elif self.percentage>=45:
            return "Second Class"
        elif self.percentage>=35:
            return "Third Class"
        else:
            return "Fail"

    def __str__(self):
        return f'\nID:{self.studentid}\tName:{self.name}\tAge:{self.age}\tPercentage:{self.percentage}'

class EnggStudent(Student):
    def __init__(self, studentid, name, age, percentage, branch, internalMarks):
        super().__init__(studentid, name, age, percentage)
        self.branch=branch
        self.internalMarks=internalMarks

    def accept(self):
        super().accept()
        self.branch=input("Enter Branch:")
        self.internalMarks=int(input('Enter Internal Marks:'))
    
    def getBranch(self):
        return self.branch
    def setBranch(self,newBranch):
        self.branch=newBranch

    def getInternalMarks(self):
        return self.internalMarks
    def setInternalMarks(self,newInternalMarks):
        self.internalMarks=newInternalMarks

    def display(self):
        super().display()
        print(f"Branch:{self.branch}\nInternal Marks:{self.internalMarks}")

    def CalculateRank(self):
        return super().CalculateRank()

    def __str__(self):
        return super().__str__()+f"\tBranch:{self.branch}\tInternal Marks:{self.internalMarks}"

# s1=Student(101,"Sanika",21,88)
# s1.display()
# print(s1.CalculateRank())
# print(s1)  

# s2=Student(0,"",0,0)
# s2.accept()
# s2.display()

e1=EnggStudent(106,"Sumit",18,75,"CS",89)
e1.display()
print(e1)

e2=EnggStudent(0,"",0,0,"",0)
e2.accept()
e2.display()

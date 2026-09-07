#Que1. Create a class MedicalStudent inherited from Student with following :
#  a. data members:
#       i.Specialization
#       ii.MarksOfInternship
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

class MedicalStudent(Student):
    def __init__(self, studentid, name, age, percentage, specialization, marksOfInternship):
        super().__init__(studentid, name, age, percentage)
        self.specialization=specialization
        self.marksOfInternship=marksOfInternship

    def accept(self):
        super().accept()
        self.specialization=input("Enter Specialization:")
        self.marksOfInternship=int(input('Enter Marks of Internship:'))
    
    def getSpecialization(self):
        return self.specialization
    def setSpecialization(self,newSpecialization):
        self.specialization=newSpecialization

    def getmarksOfInternship(self):
        return self.marksOfInternship
    def setmarksOfInternship(self,newmarksOfInternship):
        self.marksOfInternship=newmarksOfInternship

    def display(self):
        super().display()
        print(f"Specialization:{self.specialization}\nMarks Of Internship:{self.marksOfInternship}")

    def CalculateRank(self):
        return super().CalculateRank()

    def __str__(self):
        return super().__str__()+f"\tSpecialization:{self.specialization}\tMarks of Internship:{self.marksOfInternship}"

# s1=Student(101,"Sanika",21,88)
# s1.display()
# print(s1.CalculateRank())
# print(s1)  

# s2=Student(0,"",0,0)
# s2.accept()
# s2.display()

m1=MedicalStudent(106,"Sumit",18,75,"CS",89)
m1.display()
print(m1)

m2=MedicalStudent(0,"",0,0,"",0)
m2.accept()
m2.display()

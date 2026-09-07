# Que 4. Create a class Collage which has collection of students. Add the following methods:
#    a. Parameterized constructor for number of students.
#    b. AddStudent
#    c. GetStudent
#    d. RemoveStudent
#    e. Override __str__ Method

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
        return f'ID:{self.studentid}\tName:{self.name}\tAge:{self.age}\tPercentage:{self.percentage}'

class Collage:
    def __init__(self,numberOfStudents):
        self.numberOfStudents=numberOfStudents
        self.students=[]

    def AddStudent(self,student):
        self.students.append(student)

    def GetStudent(self,id):
        for s in self.students:
            if s.studentid==id:
                return s
        return None

    def RemoveStudent(self,id):
        for s in self.students:
            if s.studentid==id:
                self.students.remove(s)
                return

    def __str__(self):
        result=""
        for s in self.students:
            result=result+str(s)+"\n"
        return result

c=Collage(3)

s1=Student(101,"Sanika",22,89)
s2=Student(102,"Reva",25,65)
s3=Student(103,"Sumit",19,78)

c.AddStudent(s1)
c.AddStudent(s2)
c.AddStudent(s3)
print(c)

print(c.GetStudent(102))

c.RemoveStudent(103)
print(c)

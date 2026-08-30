class Student:
    def __init__(self,rollno,name):
        self.__rollno=rollno
        self._name=name
    def getRollNo(self):
        return self.__rollno
    def setRollNo(self,NewRollNo):
        self.__rollno=NewRollNo
    def __str__(self):
        return f"RollNo={self.__rollno}\t Name={self._name}"
    def __del__(self):
        print('OOP ends')
    
class MedicalStudent(Student):
    def __init__(self, rollno, name, marks):
        super().__init__(rollno, name)
        self.__marks=marks
    def __str__(self):
        return super().__str__()+f"\t Marks={self.__marks}"

    
s=Student(18,"Sanika")
# m=MedicalStudent(24,"Disha",480)

# print(m.__name)
# print(m)
# print(s)
# m.setRollNo(1)
# print(m)
# print(m.getRollNo())
# m._name="Reva"
print(s)
        
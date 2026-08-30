class Student:
    def __init__(self,roll_no,name,address):
        self.roll_no=roll_no
        self.name=name
        self.address=address

    def getRollNo(self):
        return self.roll_no
    def setRollNo(self,newRollNo):
        self.roll_no=newRollNo

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getAddress(self):
        return self.address
    def setAddress(self,newAddress):
        self.address=newAddress
       
    def disply(self):
        print(f"Roll_No={self.roll_no} Name={self.name} Address={self.address}")

s1=Student(18,"Sanika","Satara")
s2=Student(63,'Sharvari','Pune')
print(s1.getAddress())
print(s2.getName())
print(s1.getRollNo())
s2.setName('Aryan')
s1.setRollNo(22)
s1.disply()
s2.disply()
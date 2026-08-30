class FBSstudent:
    stCount=0
    def __init__(self,frnno,name,batch):
        self.frnno=frnno
        self.name=name
        self.batch=batch
        FBSstudent.stCount+=1

    def getFrnNo(self):
        return self.frnno
    def setFrnNo(self,NewFrnNo):
        self.frnno=NewFrnNo

    def getName(self):
        return self.name
    def setName(self,NewName):
        self.name=NewName

    def getBatch(self):
        return self.batch
    def setBatch(self,NewBatch):
        self.batch=NewBatch

    def disply(self):
        print(f"FRN_No={self.frnno},Name={self.name},Batch={self.batch}")
# FBS Student ENds.......
class PlStudent(FBSstudent):
    def __init__(self, frnno, name, batch,cName):
        super().__init__(frnno, name, batch)
        self.cName=cName

    def getCName(self):
        return self.cName
    def setCName(self,NewCName):
        self.cName=NewCName

    def disply(self):
        super().disply()
        print(f"CName={self.cName}")


f1=FBSstudent(18,"Sanika","June Python Data Science 2026")
f2=FBSstudent(20,'Sumit','May Data Analytics 2026')
f3=PlStudent(18,'Virat','July2025','One8')
print(FBSstudent.stCount)
f3.disply()
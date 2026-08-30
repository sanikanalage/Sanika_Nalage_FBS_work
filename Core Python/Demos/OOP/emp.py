class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getSal(self):
        return self.sal
    def setSal(self,newSal):
        self.sal=newSal


    
    def disply(self):
        print(f"ID={self.id} Name={self.name} Salary={self.sal}")

e1=Emp(101,"sanika",60000)
e1.disply()
print(e1.getName())
e1.setName('sumit')
print(e1.getName())
e1.disply()
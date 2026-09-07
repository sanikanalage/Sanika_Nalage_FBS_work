from abc import ABC,abstractmethod
class Emp(ABC):
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

    @abstractmethod
    def calsal(self):
        pass

    def __str__(self):
        return f"ID={self.id}\tName={self.name}\tSalary={self.sal}"
   
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

    
    def __str__(self):
        return f"ID={self.id}\tName={self.name}\tSalary={self.sal}"
    

# Emp class ends Here .......

class Hr(Emp):
    def __init__(self, id, name, sal,commission):
        super().__init__(id, name, sal)
        self.commission=commission

    def getCommission(self):
        return self.commission
    def setCommission(self,newCommission):
        self.commission=newCommission

    

    def __str__(self):
        return super().__str__()+f"\tCommission={self.commission}"
    
#Hr class Ends Here.....
class Dev(Emp):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus=bonus

    def getBonus(self):
        return self.bonus
    def setBonus(self,newBonus):
        self.bonus=newBonus

    

    def __str__(self):
        return super().__str__()+f"\tBonus={self.bonus}"

e1=Emp(1,'Sanika',30000)
h1=Hr(2,'sumit',40000,10000)
d1=Dev(4,'Arya',20000,5000)
print(e1)
print(h1)
print(d1)

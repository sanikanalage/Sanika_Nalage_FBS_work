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


class JrHr(Hr):
    def __init__(self, id, name, sal, commission):
        super().__init__(id, name, sal, commission)
        print('I am Junior HR ')
    def __str__(self):
        return super().__str__()+"\t Jr HR"

class SrHr(Hr):
    def __init__(self, id, name, sal, commission):
        super().__init__(id, name, sal, commission)
        print('I am Senior HR ')
    def __str__(self):
        return super().__str__()+"\t Sr HR"


class Admin(Emp):
    def __init__(self, id, name, sal, insentive):
        super().__init__(id, name, sal)
        self.insentive=insentive
    def getInsentive(self):
        return self.insentive
    def setInsentive(self,newInsentive):
        self.insentive=newInsentive
    def __str__(self):
        return super().__str__()+f"\tInsentive={self.insentive}"

class TrianingAdmin(Admin):
    def __init__(self, id, name, sal, insentive):
        super().__init__(id, name, sal, insentive)
        print('I am Trianing Admin')
    def __str__(self):
        return super().__str__()+'\t Trianing Admin'

class PlacementAdmin(Admin):
    def __init__(self, id, name, sal, insentive):
        super().__init__(id, name, sal, insentive)
        print('I am Placement Admin')
    def __str__(self):
        return super().__str__()+'\t Placement Admin'

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

class JrDev(Dev):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal, bonus)
        print('I am Junior Develper')
    def __str__(self):
        return super().__str__()+"\t Jr Developer"

class SrDev(Dev):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal, bonus)
        print('I am Senior Develper')
    def __str__(self):
        return super().__str__()+"\t Sr Developer"
    
# d1=SrDev(1,'Sanika',30000,6000)
# h1=SrHr(2,'sumit',40000,10000)
# a1=PlacementAdmin(5,'Arya','500000','40000')
d1=JrDev(4,'Arya',20000,5000)
print(d1)
# print(a1)
# print(d1)

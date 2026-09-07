from emp import Emp
class Hr(Emp):
    def __init__(self, id, name, sal,commission):
        super().__init__(id, name, sal)
        self.commission=commission

    def getCommission(self):
        return self.commission
    def setCommission(self,newCommission):
        self.commission=newCommission

    def calsal(self):
        return self.commission+self.sal

    def __str__(self):
        return super().__str__()+f"\tCommission={self.commission}"
    
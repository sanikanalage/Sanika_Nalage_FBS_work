from emp import Emp
class Dev(Emp):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus=bonus

    def getBonus(self):
        return self.bonus
    def setBonus(self,newBonus):
        self.bonus=newBonus

    def calsal(self):
        return self.bonus+self.sal

    def __str__(self):
        return super().__str__()+f"\tBonus={self.bonus}"

class Player:

    def __init__(self,jrNo,name):
        self.jrNo=jrNo
        self.name=name

    def getJrNo(self):
        return self.jrNo
    def setJrNo(self,NewJrNo):
        self.jrNo=NewJrNo

    def getName(self):
        return self.name
    def setName(self,NewName):
        self.name=NewName

    def __str__(self):
        return f"JRNO={self.jrNo}\t Name={self.name}"

class CricketPlayer(Player):

    def __init__(self, jrNo, name,runs):
        super().__init__(jrNo, name)
        self.runs=runs

    def getRuns(self):
        return self.runs
    def setRuns(self,NewRuns):
        self.runs=NewRuns

    def __str__(self):
        return super().__str__()+f"\tRuns={self.runs}"

p1=CricketPlayer(45,"Rohit",120907)
print(p1)


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
    def __init__(self, jrNo, name, runs):
        super().__init__(jrNo, name)
        self.runs=runs
    def getRuns(self):
        return self.runs
    def setRuns(self,NewRuns):
        self.runs=NewRuns 
    def __str__(self):
        return super().__str__()+f"\t Runs={self.runs}"

class InternationalPlayer(CricketPlayer):
    def __init__(self, jrNo, name, runs,country):
        super().__init__(jrNo, name, runs)
        self.country=country
    def getCountry(self):
        return self.country
    def setCountry(self,NewCountry):
        self.country=NewCountry
    def __str__(self):
        return super().__str__()+f"\t Country={self.country}"

class IPLPlayer(CricketPlayer):
    def __init__(self, jrNo, name, runs,team):
        super().__init__(jrNo, name, runs)
        self.team=team
    def getTeam(self):
        return self.team
    def setTeam(self,NewTeam):
        self.team=NewTeam
    def __str__(self):
        return super().__str__()+f"\t Team={self.team}"


    

class KabaddiPlayer(Player):
    def __init__(self, jrNo, name, raidPoint):
        super().__init__(jrNo, name)
        self.raidPoint=raidPoint
    def getRaidPoint(self):
        return self.raidPoint
    def setRaidPoint(self,NewRaidPoint):
        self.raidPoint=NewRaidPoint
    def __str__(self):
        return super().__str__()+f"\t RaidPoint={self.raidPoint}"

class InternationalKabPlayer(KabaddiPlayer):
    def __init__(self, jrNo, name, raidPoint,country):
        super().__init__(jrNo, name, raidPoint)
        self.country=country
    def getCountry(self):
        return self.country
    def setCountry(self,NewCountry):
        self.country=NewCountry
    def __str__(self):
        return super().__str__()+f"\t Country={self.country}"

class PKLPlayer(KabaddiPlayer):
    def __init__(self, jrNo, name, raidPoint,team):
        super().__init__(jrNo, name, raidPoint)
        self.team=team
    def getTeam(self):
        return self.team
    def setTeam(self,NewTeam):
        self.team=NewTeam
    def __str__(self):
        return super().__str__()+f"\t Team={self.team}"

# p1=Player(45,"Rohit")
# print(p1)
# c1=CricketPlayer(45,"Rohit",20000)
# print(c1)
# ic1=InternationalPlayer(18,"Virat",28000,"India")
# print(ic1)
# iplp1=IPLPlayer(77,"Shubhaman",12000,"Gujrat Giants")
# print(iplp1)
# k1=KabaddiPlayer(8,'Aslam',1400)
# print(k1)
# ik1=InternationalKabPlayer(12,"Pavan",300,"India")
# print(ik1)
pklp=PKLPlayer(5,"Mohit",250,"Puneri Palatan")
print(pklp)
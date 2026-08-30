class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec

    def getHr(self):
        return self.hr
    def setHr(self,NewHr):
        self.hr=NewHr
    def getMin(self):
        return self.min
    def setMin(self,NewMin):
        self.minr=NewMin
    def getSec(self):
        return self.sec
    def setSec(self,NewSec):
        self.sec=NewSec

    def __add__(self, other):
        totalsec=self.sec+other.sec
        remmin=totalsec//60
        totalsec=totalsec%60
        totalmin=self.min+other.min+remmin
        remhr=totalmin//60
        totalmin=totalmin%60
        totalhr=self.hr+other.hr+remhr
        return Time(totalhr,totalmin,totalsec)

    def __str__(self):
        return f"Hours:{self.hr}\t Minutes:{self.min}\t Seconds:{self.sec}"

t1=Time(12,30,49)
t2=Time(11,92,68)

print(t1+t2)

                

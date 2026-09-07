# Que1. Create a class Distance with data members as km,m and cm and add following methods:
# a. Contructor
# b. Destructor
# c. Overload + ,- operator

class Distance:

    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm

    def getKm(self):
        return self.km
    def setKm(self,newKm):
        self.km=newKm

    def getM(self):
        return self.m
    def setM(self,newm):
        self.m=newm

    def getCm(self):
        return self.cm
    def setCm(self,newCm):
        self.cm=newCm

    def __add__(self, other):
        totalcm=self.cm+other.cm
        remcm=totalcm//100
        totalcm=totalcm%100
        totalm=self.m+other.m+remcm
        remm=totalm//1000
        totalm=totalm%1000
        totalkm=self.km+other.km+remm
        return Distance(totalkm,totalm,totalcm)

    def __sub__(self, other):
        totalcm=self.cm-other.cm
        remcm=totalcm//100
        totalcm=totalcm%100
        totalm=self.m-other.m+remcm
        remm=totalm//1000
        totalm=totalm%1000
        totalkm=self.km-other.km+remm
        return Distance(totalkm,totalm,totalcm)        

    def __str__(self):
        return f"KiloMeter={self.km}\tMeter={self.m}\tCentiMeter={self.cm}"

    def __del__(self):
        print("Object Destroyed")

d1=Distance(8,800,200)
d2=Distance(5,600,90)
print(d1+d2)
print(d1-d2)
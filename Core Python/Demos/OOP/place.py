class Place:
    def __init__(self,place_ID,name,location):
        self.placeID=place_ID
        self.name=name
        self.location=location

    def getPlaceID(self):
        return self.placeID
    def setPlaceID(self,newPlaceID):
        self.placeID=newPlaceID

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getLocation(self):
        return self.location
    def setLocation(self,newLocation):
        self.location=newLocation

    def disply(self):
        print(f'Place_ID={self.placeID} Place_Name={self.name} Location={self.location}')

p1=Place(11883,"Kas Pathar","Satara,Maharashtra")
p2=Place(12086,'Saras Bag','Pune,Maharashtra')

print(p1.getPlaceID())
print(p1.getLocation())
print(p2.getName())
p1.setPlaceID('11002')
p2.setName('Shaniwar Wada')
p1.disply()
p2.disply()

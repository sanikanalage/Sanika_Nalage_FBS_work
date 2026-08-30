class Vehicle:
    def __init__(self,VehicleID,brand,model,price):
        self.VehicleID=VehicleID
        self.brand=brand
        self.model=model
        self.price=price

    def getVehicleId(self):
        return self.VehicleID
    def setVehicleId(self,newId):
        self.VehicleID=newId

    def getBrand(self):
        return self.brand
    def setBrand(self,newBrand):
        self.brand=newBrand

    def getModel(self):
        return self.model
    def setModel(self,newModel):
        self.model=newModel

    def getPrice(self):
        return self.price
    def setPrice(self,newPrice):
        self.price=newPrice
    
    def disply(self):
        print(f"Vehicle_ID={self.VehicleID} Brand={self.brand} Model={self.model} Price={self.price}")

v1=Vehicle(287738901,'Toyota','Fortuner',3500000)
print(v1.getModel())
v1.setModel('BMW')
print(v1.getModel())
v1.disply()
        
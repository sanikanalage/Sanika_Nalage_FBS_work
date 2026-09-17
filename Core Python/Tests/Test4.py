# Write a program which calculates toll calculation on some location following
# is data provided:
# Many vehicles goes through the toll every vehicle has to pay the basic
# toll + extra charges if any.
# two wheelers have to pay basic toll Rs 20 three wheelers have to pay
# 30 and four wheelers have to pay 40
# heavy veheicles i.e. Vehicles having wheels more than four, have to
# pay 60 Rs as basic toll
# extra charges :
# for two wheelers if no. of persons are more than two extra charge
# =10/person
# for three wheelers if no. of persons are more than 3 extra charge
# =20/person
# for four wheelers if no. of persons are more than 4 extra charge
# =40/person
# for heavy vehicle if no. of person are more than 6 extra charges
# =100/person.
# Show polymorphic behaviour in main. Main module should be
# designed in such way that toll should easily operate it through
# interactive menu driven program .
# Object of vehicle class should not be possible.

from abc import ABC,abstractmethod
class Vehicle(ABC):
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

    @abstractmethod
    def caltoll(self):
        pass
    
    def __str__(self):
        return f"Vehicle_ID={self.VehicleID}\t Brand={self.brand}\t Model={self.model}\t Price={self.price}"


class TwoWheelers(Vehicle):
    def __init__(self, VehicleID, brand, model, price,persons):
        super().__init__(VehicleID, brand, model, price)
        self.person=persons

    def getPersons(self):
        return self.person
    def setPersond(self,NewPersons):
        self.person=NewPersons

    def caltoll(self):
        toll=20

        if self.person>2:
            toll=toll+(self.person-2)*10

        return toll

    def __str__(self):
        return super().__str__()+f"\tNo of Persons={self.person}"

class ThreeWheelers(Vehicle):
    def __init__(self, VehicleID, brand, model, price,persons):
        super().__init__(VehicleID, brand, model, price)
        self.person=persons

    def getPersons(self):
        return self.person
    def setPersond(self,NewPersons):
        self.person=NewPersons

    def caltoll(self):
        toll=30

        if self.person>3:
            toll=toll+(self.person-3)*20

        return toll

    def __str__(self):
        return super().__str__()+f"\tNo of Persons={self.person}"

class FourWheelers(Vehicle):
    def __init__(self, VehicleID, brand, model, price,persons):
        super().__init__(VehicleID, brand, model, price)
        self.person=persons

    def getPersons(self):
        return self.person
    def setPersond(self,NewPersons):
        self.person=NewPersons

    def caltoll(self):
        toll=40

        if self.person>4:
            toll=toll+(self.person-4)*40

        return toll

    def __str__(self):
        return super().__str__()+f"\tNo of Persons={self.person}"

class HeavyWheelers(Vehicle):
    def __init__(self, VehicleID, brand, model, price,persons):
        super().__init__(VehicleID, brand, model, price)
        self.person=persons

    def getPersons(self):
        return self.person
    def setPersond(self,NewPersons):
        self.person=NewPersons

    def caltoll(self):
        toll=60

        if self.person>6:
            toll=toll+(self.person-6)*100

        return toll

    def __str__(self):
        return super().__str__()+f"\tNo of Persons={self.person}"

t1=TwoWheelers(101,"Hero Honda","Passion",120000,5)
print(t1)
print(t1.caltoll())

t1=ThreeWheelers(102,"Bajaj","Auto",250000,4)
print(t1)
print(t1.caltoll())

f1=FourWheelers(103,"Toyota","Fortuner",350000,6)
print(f1)
print(f1.caltoll())

h1=HeavyWheelers(104,"Tata","Truck",800000,8)
print(h1)
print(h1.caltoll())


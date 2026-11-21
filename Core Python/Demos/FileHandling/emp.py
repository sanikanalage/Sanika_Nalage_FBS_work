import pickle
class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def getId(self):
        return self.id
    def setId(self,NewId):
        self.id=NewId

    def getName(self):
        return self.name
    def setName(self,NewName):
        self.name=NewName

    def getSal(self):
        return self.sal
    def setSal(self,NewSal):
        self.sal=NewSal

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSalary={self.sal}")

    def __str__(self):
        return f"Id={self.id}\tName={self.name}\tSalary={self.sal}"

# e1=Emp(101,"Sanika",40000)
# # print(type(str(e1)))
# f=open("emp.txt","a+")
# # f.write(str(e1))
# f.seek(0)
# d=f.read()
# print(d)
# # print(type(d))
# print(e1)
# e1.display()
# d.display()

e1=Emp(101,"Sanika",40000)
e2=Emp(102,"Sumit",60000)
f=open("emp.dat","wb")
pickle.dump(e1,f)
pickle.dump(e2,f)
f=open("emp.dat","rb")
d=pickle.load(f)
d1=pickle.load(f)
print(d)
print(d1)
# print(type(d))
# print(type(d1))
d.display()
d1.display()

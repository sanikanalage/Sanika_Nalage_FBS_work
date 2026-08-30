class Mechanical:
    def __init__(self):
        print("I am from Mechanical")
    def __str__(self):
        return "Mec Object"
    def getBranch(self):
        print("Mec Branch")

class Electrical:
    def __init__(self):
        print("I am from Electrical")
    def __str__(self):
        return "Ele Object"
    def getBranch(self):
        print("Ele Branch")

class Mecatronics(Mechanical,Electrical):
    def __init__(self):
        super().__init__()
        print('constructor of macatronix get called')
    def __str__(self):
        return super().__str__()+f"\t Objet of Mecatronix"
    def getBranch(self):
        print('I am From Mechatronics')
        return super().getBranch()


m=Mecatronics()
# print(m)
m.getBranch()
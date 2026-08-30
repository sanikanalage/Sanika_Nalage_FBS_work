#Que1. Create a class Book with members as bid,bname,price and author.
# Add following methods-
# a)constructor (support both parameterized and parameterless)
# b)destructor
# c)showBook

class Book:

    #Constructor
    def __init__(self,bid=0,bname="",price=0,author=""):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

    # Getter and Setter
    def getBID(self):
        return self.bid
    def setBID(self,NewBID):
        self.bid=NewBID

    def getBName(self):
        return self.bname
    def setBName(self,NewBName):
        self.bname=NewBName

    def getPrice(self):
        return self.price
    def setPrice(self,NewPrice):
        self.price=NewPrice

    def getAuthor(self):
        return self.author
    def setAuthor(self,NewAuthor):
        self.author=NewAuthor

    #showbook
    def showBook(self):
        print(f"BID={self.bid}\t Book_Name={self.bname}\t Price={self.price}\t Author={self.author}")

    #Destructor
    def __del__(self):
        print('Book Object Destroyed')

#Parameterized
b1=Book(1043,"Shyamachi Aai",349,"Sane Guruji")
b1.showBook()
#Parameterless
b2=Book()
b2.showBook()
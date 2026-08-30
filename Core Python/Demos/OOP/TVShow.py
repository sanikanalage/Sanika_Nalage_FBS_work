class TVShow:
    def __init__(self,ShowID,title,lan,genre):
        self.ShowID=ShowID
        self.title=title
        self.lan=lan
        self.genre=genre

    def getShowID(self):
        return self.ShowID
    def setShowID(self,NewShowID):
        self.ShowID=NewShowID

    def getTitle(self):
        return self.title
    def setTitle(self,NewTitle):
        self.title=NewTitle

    def getLanguage(self):
            return self.lan
    def setLanguage(self,NewLanguage):
            self.lan=NewLanguage

    def getGenre(self):
        return self.genre
    def setGenre(self,NewGenre):
        self.genre=NewGenre

    def disply(self):
        print(f"Show_ID={self.ShowID} Title={self.title} Language={self.lan} Genre={self.genre}")

t1=TVShow(105,'Dangal','Hindi','Sports-Drama')
t2=TVShow(2045,'Laughter Chef','Hindi','Comedy and Cooking Show')
print(t1.getTitle())
print(t2.getGenre())
t1.setShowID('23967')

t1.disply()
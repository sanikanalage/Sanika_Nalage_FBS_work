import demo1
def useit():
    print("I am in Useit")
    print(__name__)
    demo1.add()
if __name__=="__main__":
    useit()
class MyException(Exception):
    def __init__(self, *args):
        print("I am from MyException")
    def __str__(self):
        return "MyException Object"
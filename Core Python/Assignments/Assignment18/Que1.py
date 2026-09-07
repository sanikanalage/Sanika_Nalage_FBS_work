# Que1. Create a class Complex Number with data members as real and imag and add following methods:
# a. Contructor
# b. Destructor
# c. Overload + ,- operator

class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def getReal(self):
        return self.real
    def setReal(self,newReal):
        self.real=newReal

    def getImag(self):
        return self.imag
    def setImag(self,newImag):
        self.imag=newImag

    def __add__(self, other):
        real=self.real+other.real
        imaginary=self.imag+other.imag
        return ComplexNumber(real,imaginary)

    def __sub__(self, other):
        real=self.real-other.real
        imaginary=self.imag-other.imag
        return ComplexNumber(real,imaginary)

    def __str__(self):
        return f"Real={self.real}\tImaginary={self.imag}i"

    def __del__(self):
        print('Object is Destroyed')

c1=ComplexNumber(10,20)
c2=ComplexNumber(5,10)
print(c1+c2)
print(c1-c2)
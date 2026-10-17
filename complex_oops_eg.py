class ComplexNumber:
    def __init__(self,real=0.0,imag=0.0): #magic methods in python start and end with double score and are called by default when class is initialized
        self.real=real
        self.imag=imag

    def __str__(self):
        if self.imag<0:
            s=f"({self.real} {self.imag}i)"
        s=f"({self.real}+{self.imag}i)" #magic method used for printing, returns string
        return s  
    
    def __add__(self,other):
        resultReal=0
        resultImag=0

        resultReal=self.real+other.real
        resultImag=self.imag+other.imag

        ans=ComplexNumber(resultReal,resultImag)
        return ans
    
    def __sub__(self,other):
        resultReal=0
        resultImag=0

        resultReal=self.real-other.real
        resultImag=self.imag-other.imag

        ans=ComplexNumber(resultReal,resultImag)
        return ans
    
    def __mul__(self, other):
        resultReal=0
        resultImag=0

        resultReal=(self.real * other.real)-(self.imag*other.imag)
        resultImag=(self.real * other.imag)+(other.real * self.imag)
        ans=ComplexNumber(resultReal,resultImag)
        return ans

    def __truediv__(self, other):
        resultReal=0
        resultImag=0

        resultReal=((self.real*other.real+self.imag*other.imag)/(other.real*other.real+other.imag*other.imag))
        resultImag=((self.imag*other.real-self.real*other.imag)/(other.real*other.real+other.imag*other.imag))
        ans=ComplexNumber(resultReal,resultImag)
        return ans


    def conjugate(self):
        ans=ComplexNumber(self.real,-1.0*self.imag)
        return ans
    
c1=ComplexNumber(6,-2)
c2=ComplexNumber(4,3)
print("Custom class")
print(c1*c2)
print(c1/c2)
print(c1-c2)
print(c1.conjugate())
print(c1+c2)

print("Actual Class")
s1=6-2j
s2=4+3j
print(s1*s2)
print(s1/s2)
print(s1-s2)
print(s1.conjugate())
print(s1+s2)



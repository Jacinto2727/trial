'''
In multi level inheritance child class can only access its own parent class 
Multiple inheritance creates ambiguity in java and therefore is not allowed
ClassName.mro() provides sequence of calls'''

class A:
    def __init__(self):
        self.value='A'

class B(A):
    def __init__(self):
        super().__init__()
        self.value='B'

class C(A):
    def __init__(self):
        super().__init__()
        self.value='C'

class D(B,C):
    def __init__(self):
        super().__init__()

obj=D()
print(obj.value)
print(D.mro()) # prints sequence 

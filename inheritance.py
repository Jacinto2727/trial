''' 
 We inherit 1) non private attributes
 2) non private methods
 3) constructor(other magic methods)
 
 We cannot access private attributes or methods of our parent class
 
 Parent class cannot inherit from child, only child inherits from parent class'''

class User:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def login(self):
        print("logged in")
    
    def __logout(self):
        print("logged out")

class Student(User):
    # inheriting User Class features
    def play(self):
        print("playing")

    def __init__(self,marks,rollNumber,name,id,age,passCode):

        super().__init__(name,id) #super is used for method overriding
        self.age=age
        self.passCode=passCode
        self.marks=marks
        self.rollNumber=rollNumber

    def login(self):
        print("OTP sent")
        super().login()   ##alternative User.login(self) 

s1=Student(19,27,"Mayank",21,23,"xyz")
s1.login()
s1.play()
# s1.__logout() ## will throw error because private methods are name-mangled and not accessible from outside the class

''' Super Keyword is used to access methods of parent class
1) Cannot be used outside 
2) Can only access methods and not attribute
'''


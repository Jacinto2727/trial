class Student:
    numberOfStudents=0  #class variable and can be invoked by className.VariableName
    __schoolName="xyz"
    __passcode="1728"

    def __init__(self,name,rollNumber,marks):
        self.rollNumber=rollNumber                            #instance variable and can be invoked by objectName.variableName
        self.name=name
        self.__marks=marks                                    #private variable __variableName, cannot be acccessed and changed eg: s1.marks=45 will throw an error
        self.numberOfStudents=Student.numberOfStudents+1
        Student.numberOfStudents=Student.numberOfStudents+1
    
    #getter
    def getMarks(self):
        return self.__marks                     #enables viewing marks 
    
    #setter                                     #getter and setter are used for private variables adding extra layer of authentication
    def setMarks(self,newMarks,passcode):
        if (passcode==Student.__passcode):
            self.__marks=newMarks
            return self.__marks
        else:
            print("Invalid credentials,Try again!")

    @staticmethod
    def getSchoolName():
        return Student.__schoolName   # static method can be directly accessed by classname.functionname() and objectname.functioname() both
    
    def getStudentSchoolName(self):
        return Student.__schoolName  # can only be accessed by object

    def study(self):
        print("I am"+ str(self.rollNumber)+" and I am studying")
    
    def play(self):
        print("Padh liya, now going to play")

s1=Student("Mayank",20,50)
s2=Student("ravi",50,60)
print(s1.numberOfStudents)
print(s2.numberOfStudents)
print(Student.numberOfStudents)
print(s1.getMarks())
s1.setMarks(70,"1728")
print(s1.getMarks())
#Student.getStudentSchoolName() throws error 
print(s1.getStudentSchoolName())
print(Student.getSchoolName())

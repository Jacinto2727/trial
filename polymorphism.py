'''
In python we achieve polymorphism by 
1. Method Overriding
2.Method Overloading
3.Operator Overloading '''


#Method Overloading
class User:

    '''def __init__(self,name,mobileNumber,address=""):
        if(address==""):
            self.C1(name,mobileNumber)
        else:
            self.C2(name,mobileNumber,address)
This snippet solves method overloading issue caused in python although java and c++ dont cause any problem'''  
    def __init__(self,name,mobileNumber): # replace by c1
        self.name=name
        self.mobileNumber=mobileNumber

    def __init__(self,name,mobileNumber,address): # replace by c2
        self.name=name
        self.mobileNumber=mobileNumber
        self.address=address

obj=User("Mayank",887910463,"xyzz")
print(obj.name)
print(obj.mobileNumber)
print(obj.address)

'''obj1=User("dora",7789462) # throws error since python reads the latest constructor accepting address as an argumrnt
print(obj.name)
print(obj.mobileNumber)'''

# Method Overriding
class Animal:
    def sound(self):
        return 'Some sound'
    
class Dog(Animal):
    def sound(self):
        return 'Bark'
obj=Dog()
print(obj.sound())  #Here childclass has overriden features of parent class

obj1=Animal()
print(obj1.sound())


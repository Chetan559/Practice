# here w'll see object oriented programming in python
# class and object
# class is a blueprint for creating objects it defines a set of attributes and methods that the objects created from the class will have (silmillar to structure in c used for creating user defined data types)
# object is an instance of a class it is created from the class and has its own unique set of attributes and methods
#  lcasses allows you to create your own data type in python this is the primary feature of oop
#  it allows you to create your own data types and define their behavior

# to declre a class in python we use the keyword class followed by the name of the class and a colon

class Student1:
    #here we've created a class named Student1
    ...
    
class Student:    #here we've created a class named Student
    # ...  we can just leave a class with '...' notation if we don't want to define any attributes or methods in the class
    # classses comes with certian functions called methods
    # these methods are used to define the behavior of the class and its attributes
    def __init__(self, name, house, stable= None): # here we'he created dunctor of the class Student
        # the parameter self is given to the constructor to refer to the object itself
        # it is used to access the attributes and methods of the class
        # the constructor is used to initialize the attributes of the class in python __init__ is the constructor of the class
        if not name:
            raise ValueError("Name cannot be empty") # python has built in exceptions that can be used to raise an error if the value is not valid. user can raise their own exceptions using the raise keyword when something unexpected happens
            # we can treate the ValueError or any other exeptions as a function and pass the message to it
        if house not in ["Ravenclaw", "Gryffindor", "Hufflepuff", "Slytherin"]:
            raise ValueError("House must be one of the following: Ravenclaw, Gryffindor, Hufflepuff, Slytherin") 
        self.name = name
        self.house = house
        
    def __str__(self): # if you define this function in your class than python will call this function Automaticall whenever some other fuction wants to see your object as string  {dunder str method}
        # for e.g. print(student) will try to seethe object as a string and if you dont define this function than print will restund a string like <__main__.Student object at 0x7f8c8c8c8c8c> which is not useful which is location of the object in memory
        return f"{self.name} from {self.house} this is returned by __str__ method" # here we're returning a string that contains the name and house of the student object

    
def main():
    student = get_student()
    print(f"{student.name} lives in {student.house}")
    student = get_student2()
    print(f"{student.name} lives in {student.house}")
    print(student) # here we're calling the __str__ method of the class Student and printing the object as a string
    # print(f"{student["name"]} lives in {student["house"]}")
    
def get_student():
    student = Student1()  # here we've created an object of the class Student and assigned it to the variable student
    #if class in blueprint than object is a house created from the blueprint
    # another name of object is instance of the class
    student.name = input("Enter your name: ")   # here we are creating an object of the class Student and assigning it to the variable student we can then access the attributes of the object using the dot notation
    student.house = input("Enter your house: ") # here we are assigning a value to the attribute house of the object student
    return student
    
def get_student2():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Student( name, house) # here we're passing the values to the constructor of the class Student and creating an object of the class Student returning it

'''
def get_student():
    student = {}
    student["name"] = input("Enter your name: ")
    student["house"] = input("Enter your house: ")
    return student
'''
'''
---------------------------------------------------------------------------------------------------------------
'''
class Wizard:
    def __init__(self, name):
        self.name= name
    
    @property  # this is a decorator that allows you to define a method as a property of the class
    # this means that you can access the method as an attribute of the class without calling it as a method
    def name(self):  # this is getter method to get name of student
        return self._name # _ is used to indicate that this is a private attribute of the class
    # instead of using self.name we can use self._name to access the private attribute of the class because the python interpreter will get confussed if both attribute and method are of same name so to assess attribute we use self._name "_" is used to indicate that this is a private attribute of the class
    
    @name.setter # this is a decorator that allows you to define a method as a setter method of the class
    # this means that you can set the value of the attribute using this method
    def name(self, name): #everytime anywhere in code student.name is used it will call this method and set the value of the attribute name of the class Student2
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name
        # here we're using the setter method to set the value of the attribute name of the class Student2


class Professor(Wizard): # here we're creating a class Professor that inherits from the class Wizard
    def __init__(self, name, subject):  
        super().__init__(name)
        # here we're calling the constructor of the class Wizard using the super() function and passing the name to it
        # this is used to initialize the attributes of the class Wizard in the constructor of the class Professor
        self.subject = subject
    
    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        subject = input("Enter your subject: ")
        return cls(name, subject)

class Student2(Wizard):
    def __init__(self, name, house, petronus=None):
        super().__init__(name)
        self.house = house   # even here we've called setter methos insead of directly assigning the value to the attribute house of the class Student2 this way we can validate the value of the attribute house of the class Student2 using the setter method
        self.petronus = petronus
        
    def __str__(self):
        return f"{self.name} from {self.house} " 
    
    
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Ravenclaw", "Gryffindor", "Hufflepuff", "Slytherin"]:
            raise ValueError("House must be one of the following: Ravenclaw, Gryffindor, Hufflepuff, Slytherin")
        self._house = house
    
    def charm(self):
        match self.petronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Dog":
                return "🐶"
            case _:
                return "Expecto Patronum!"
    
    @classmethod # this is a decorator that allows you to define a method as a class method of the class
    #this method will get exectude before creating any new instance of the class
    #class method are methods associated with  whole clsss and not with the instance of the class
    def get(cls):  # here cls refers to the class itself and not the object of the class
        name = input("Enter your name: ")
        house = input("Enter your house: ")
        petronus = input("Enter your petronus: ")
        return cls(name, house, petronus)  # here we're passing the values to the constructor of the class Student2 and creating an object of the class Student2 returning it via cls() method 
        

def main2():
    student = Student2("Harry", "Gryffindor", "Stag")
    print(student)
    print(student.charm(),end="\n\n")
    student = Student2("Hermione", "Gryffindor", "Otter")
    print(student)
    print(student.charm(),end="\n\n")
    student = Student2("Ron", "Gryffindor", "Dog")
    print(student)  
    print(student.charm(),end="\n\n")
    student = Student2("Draco", "Slytherin")
    print(student)
    print(student.charm(),end="\n\n")
    student = Student2.get()  # here we're calling the class method get of the class Student2 and creating an object of the class Student2 using the class method get and assigning it to the variable student
    print(student)
    print(student.charm(),end="\n\n")
    proffessor = Professor.get()  # here we're calling the class method get of the class Professor and creating an object of the class Professor using the class method get and assigning it to the variable professor
    print(proffessor)
    print(proffessor.subject,end="\n\n")
        
'''
unlike java python doesn't have access modifiers like public, private, protected etc. but we can use _ to indicate that this is a private attribute of the class and it should not be accessed outside the class
it use the houner system to indicate that this is a private attribute of the class and it should not be accessed outside the class

wher the varible starts with _ it is considered as private and should not be accessed outside the class no one should touch it and __ indiactes more private than _
but it is not enforced by python it is just a convention and should be followed by the user of the class

'''



if __name__ == "__main__":
    # main()
    main2()
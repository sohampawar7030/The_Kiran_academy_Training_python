class collage :
    def __init__(self,name,branch):
        self.__name=name
        self.__branch=branch

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

    def get_branch(self):
        return self.__branch
    def set_branch(self,branch):
        self.__branch=branch
    

    def display(self):
        print(f"the collage name is : {self.__name}")
        print(f"the branch is : {self.__branch}")

class Student(collage) : 
    def __init__(self,name,branch,StudentName,id):
        super().__init__(name,branch)
        self.StudentName = StudentName
        self.id=id
    def display(self):
        print(f"the collage name is : {self.get_name()}")
        print(f"the branch is : {self.get_branch()}")
        print(f"the Student name is : {self.StudentName}")
        print(f"the Id is : {self.id}")

c1=Student("acem","AIML","soham",2)
c1.display()




'''                      🔍 Highlights:
OOP                                  Concept Example Used
Class	                             class Collage, class Student
Object	                             c1 = Student(...)
Constructor	                         __init__ in both classes
Encapsulation	                     __name, __branch + getter/setter
Abstraction	                         Access to private data via methods
Inheritance	                         class Student(Collage)
Polymorphism	                     Overridden display() method
Super Keyword	                     super().__init__(...)

 '''
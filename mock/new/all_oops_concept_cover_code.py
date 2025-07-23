class College:
    # Constructor (with encapsulation)
    def __init__(self, name, year):
        self.__name = name          # Encapsulated attribute
        self.__year = year

    # Getter and Setter methods for encapsulated attributes
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    # Instance Method
    def display(self):
        print(f"The college name is {self.__name}")
        print(f"The academic year is {self.__year}")

    # Class Method
    @classmethod
    def college_info(cls):
        print("This is the base class for all colleges.")

    # Static Method
    @staticmethod
    def welcome():
        print("Welcome to the college portal!")


# Inherited class (Inheritance + Method Overriding + Polymorphism)
class Branch(College):
    def __init__(self, name, year, branch_name, branch_id):
        super().__init__(name, year)
        self.branch_name = branch_name
        self.branch_id = branch_id

    # Overridden method
    def display(self):
        super().display()
        print(f"The branch name is {self.branch_name}")
        print(f"The branch ID is {self.branch_id}")

    # Polymorphic method
    def describe(self):
        print(f"Branch: {self.branch_name}, ID: {self.branch_id}")


# Object creation (Object-oriented instantiation)
c1 = Branch("Alard College", "2025", "AIML", "002")

# Static and class method call
College.welcome()
College.college_info()

# Access display (Polymorphism + Overriding)
c1.display()

# Calling describe() to demonstrate polymorphism
c1.describe()

# Accessing private variables using getter (Encapsulation)
print("Accessing encapsulated data:")
print("College Name:", c1.get_name())
print("Academic Year:", c1.get_year())


'''Summary of OOP Concepts in This Code
OOp Concept	                                                         Where Used
Class	                                                          College, Branch
Object	                                                          c1 = Branch(...)
Constructor	                                                      __init__() in both classes
Inheritance	                                                      Branch(College)
Encapsulation	                                                  __name, __year with getters/setters
Abstraction	                                                      display() and describe() methods hide internal details
Polymorphism	                                                  describe() could be redefined in other subclasses
Method Overriding	                                              display() in Branch overrides College.display()
Class Method	                                                  college_info()
Static Method	                                                  welcome()

Let me know if you want me to add a student class with multi-level inheritance, or real input from the user.








'''
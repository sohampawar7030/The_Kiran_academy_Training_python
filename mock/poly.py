# 						##  Practices Question on polymorphism overriding   ##
 

# # 1. Create a base class Animal with a method make_sound() that prints "Some sound". Override this method in the derived class Dog to print "Bark" instead.

# class Animal :
#     def make_sound(self):
#         print("Some sound")
# class Dog :
#     def make_sound(self):
#         print("bark")


# a1=Dog()
# a1.make_sound()



# 2. Create a parent class Shape with a method area(). Override it in the subclasses Circle and Rectangle to calculate and return the area specific to each shape.
# class Shape :
#     def area(self,value):
#         print(f"the area is {value}")
# class Circle(Shape) :
#     def __init__(self,pie,radius):
#         self.pie=pie
#         self.radius=radius
#     def display(self):
#         print(f"The pie is : {self.pie}")
#         print(f"the radius is : {self.radius}")
#         area_value=self.pie*self.radius*self.radius
#         super().area(area_value)
        
# # cl=Circle(pie=3.14,radius=10)
# # cl.display()

# class Rectangle(Shape) :
#     def __init__(self,breadth,height):
#         self.breadth=breadth
#         self.height=height
    
#     def display(self):
#         print(f"the breadth is  : {self.breadth}")
#         print(f"the height is : {self.height}")
#         area_value=1/2*self.breadth*self.height
#         super().area(area_value)

# cl=Circle(pie=3.14,radius=10)
# c2=Rectangle(breadth=20,height=23)
# cl.display() 
# c2.display()     

        

# 3. Create a base class Employee with a method get_role(). Create two child classes Manager and Developer, and override the get_role() method to return appropriate roles.
# class Employee :
#     def get_role(self):
#         print("employee")
# class Manager(Employee):
#     def get_role(self):
#         super().get_role()
#         print("manager")
        
# class Developer(Employee):
#     def get_role(self):
#         super().get_role()
#         print("Developer")

# cl=Manager()
# cl.get_role()

# c2=Developer()
# c2.get_role()


# 4. Create a class Person with a method introduction(). Override it in the subclasses Student and Teacher. Then, write a function that accepts an object of type Person and calls its introduction() method.

# class Person:
#     def introduction(self):
#         print("Hello guys")
# class Student :
#     def introduction(self):
#         print("Hello")

# class Teacher :
#     def introduction(self):
#         print("Hello Student")
# cl=Teacher()
# cl.introduction()





# 5. Implement a base class Notification with a method send_message(). Override it in the subclasses EmailNotification, SMSNotification, and PushNotification. Use polymorphism to call the overridden method based on the object type.

# class Notification :
#     def send_message(self):
#         print("recived Sucessfully !!!!!")
# class EmailNotification(Notification) :
#     def send_message(self):
#         print("Email")
#         super().send_message()

# class SMSNotification(Notification):
#     def send_message(self):
#         print("SMS")
#         super().send_message()

# class PushNotification(Notification):
#     def send_message(self):
#         print("Push Notification")
#         super().send_message()

# c1=EmailNotification()
# c1.send_message()

# c2=SMSNotification()
# c2.send_message()

# c3=PushNotification()
# c3.send_message()
        


# 6. Write a program where method overriding is combined with type checking using isinstance() to filter and process only objects of a specific subclass.
# class ABC :
#     def display(name):
#         print("display name")

# class BCD(ABC) :
#     def display(name):
#         print("display name")

# print(isinstance(BCD,ABC))
# print(isinstance(ABC,BCD))


# 7. Create a system with a base class Report and subclasses PDFReport, ExcelReport, and WordReport. Each class should override the generate() method. Write a function that takes a list of report objects and calls their generate() methods using polymorphism.

# class Report:
#     def generate(self):
#         print("Generate the Report")
#         l1=[1,2,3,4,5,6,7,8,9,0]
#         print(l1)

# class PDFReport(Report) :
#     def generate(self):
#         super().generate()
#         print("PDF Report is Sucessfully Generated !!!!")

# class ExcelReport(Report):
#     def generate(self):
#         super().generate()
#         print("EXCEL Report is Sucessfully Generated !!!!")
    
# class WordReport(Report):
#     def generate(self):
#         super().generate()
#         print("Word Report is Sucessfully Generated !!!!")


# c1=PDFReport()
# c1.generate()

# c2=ExcelReport()
# c2.generate()

# c3=WordReport()
# c3.generate()








# 8. Write a program where method overriding is combined with class type checking using issubclass() to filter and identify specific subclasses derived from a base class.

class ABC :
    def display(name):
        print("display name")

class BCD(ABC) :
    def display(name):
        print("display name")

print(issubclass(BCD,ABC))
print(issubclass(ABC,BCD))


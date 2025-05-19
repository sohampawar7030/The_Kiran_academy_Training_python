# Write a Java program to create a class Employee with attributes name, id, and salary. Add methods to display employee detail

class Employee :
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print(f"the name is : {self.name}")
        print(f"the id is : {self.id}")
        print(f"salary is : {self.salary}")
c1=Employee("soham",1,20000)
c1.display()

        
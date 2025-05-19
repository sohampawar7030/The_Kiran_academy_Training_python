# # 										##  Practices Question on Inheritance  ##

# # 1. 	Create a class Person with variables: name, age, gender, address.
# #  	Create a constructor and methods to display the data.
# #  	Inherit it in a class Student with additional variables: rollNo, branch, percentage.
# #  	Add appropriate methods to Student to display all details.


# class person:
#     def __init__(self,name,age,gender,address):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.address=address
#     def display(self):
#         print(f" the name is : {self.name} ")
#         print(f" the age is : {self.age} ")
#         print(f" the gender is : {self.gender} ")
#         print(f" the address is : {self.address} ")
# class student(person) :
#     def __init__(self,name,age,gender,address,roll_no,branch,persentage):
#         super().__init__(name,age,gender,address)
#         self.roll_no=roll_no
#         self.branch=branch
#         self.persentage=persentage

#     def display_student(self):
#         self.display()
#         print(f" the roll no  is : {self.roll_no} ")
#         print(f" the branch is : {self.branch} ")
#         print(f" the Persentage is : {self.persentage} ")


# s1=student("soham",20,"male","pune",1,"AIML","96")
# s1.display_student()



# 2.     Create a class Vehicle with variables: brand, model, color, price.
#  	Create a constructor and display method.
# 	Create a subclass Car which adds: fuelType, transmission.
#  	Create another subclass ElectricCar which adds: batteryCapacity, chargingTime.
# #  	Call constructors and methods at each level to print complete car info.

# class vehicle :
#     def __init__(self,brand,model,color,price):
#         self.brand=brand
#         self.model=model
#         self.color=color
#         self.price=price



#     def display(self):
#         print(f"the brand is : {self.brand}")
#         print(f"the model is : {self.model} ")
#         print(f"the color is : {self.color}")
#         print(f"the price is : {self.price}")




# class FuelType(vehicle) :
#     def __init__(self,brand,model,color,price,fuel_type,Transmission):
#         super().__init__(brand,model,color,price)
#         self.fuel_type=fuel_type
#         self.Transmission=Transmission
#     def display_fuel(self):

#         super().display()
#         print(f"the fuel type is : {self.fuel_type}")
#         print(f"the transmission is : {self.Transmission}")

# class Electric_Car(FuelType) :
#     def __init__(self,brand,model,color,price,fuel_type,Transmission, batteryCapacity, chargingTime):
#         super().__init__(brand,model,color,price,fuel_type,Transmission)
#         self.batteryCapacity=batteryCapacity
#         self.chargingTime=chargingTime
#     def display_car(self):
#         super().display_fuel()
#         print(f"the battery capicity is : {self.batteryCapacity}")
#         print(f"the chaging time is : {self.chargingTime}")



# s1=Electric_Car("honda","xyz","black",20000,"desial","yes","20mh","4hr")
# s1.display_car()

        


        

        





















# # 3.   Create a base class Animal with variables: name, type, age, color.
# #       Add a constructor and methods to show info and makeSound().
# #       Create Dog and Cat classes that inherit Animal.
# #       Override makeSound() method in both child classes with specific messages.

# class Animal :
#     def __init__(self,name,type,age,color):
#         self.name=name
#         self.type=type
#         self.age=age
#         self.color=color
#     def display(self):
#         print(f"the name is : {self.name}")
#         print(f"the type is : {self.type}")
#         print(f"the age is : {self.age}")
#         print(f"the color is : {self.color}")
#     def makesound(): 
#         print("some generaric sound")
# class Dog(Animal) :
#     def makesound(self):
#         print("Bhoooooo")
# class cat(Animal) :
#     def makesound(self):
#         print("meuuuuuuu")

# s1=cat("cat","xyz",20,"black")
# s1.makesound()
# s2=Dog("cat","xyz",31,"white")
# s2.makesound()        


# 4. 	Create base class Appliance with brand, power_rating, weight, color, warranty.
# 	Child WashingMachine adds capacity, type (front/top load).
# 	Child SmartWashingMachine adds WiFi_enabled, voice_controlled.
# 	Each class should have display methods and constructors.



# class Appliances :
#     def __init__(self,brand,power_rating,weight,color,company):
#         self.brand=brand
#         self.power_rating=power_rating
#         self.weight=weight
#         self.color=color
#         self.company = company
#     def display(self):
#         print(f"brand is : {self.brand}")
#         print(f"the power_rating is {self.power_rating}")
#         print(f"the weight is : {self.weight}")
#         print(f"the color is : {self.color}")
#         print(f"the company is : {self.company}")
        
# class Washing_machine(Appliances):
#     def __init__(self,brand,power_rating,weight,color,company,capacity,type):
#         super().__init__(brand,power_rating,weight,color,company)
#         self.capacity=capacity
#         self.type=type
#     def display(self):
#         super().display()
#         print(f"the capicity is : {self.capacity}")
#         print(f"the type is : {self.type}")
# class SmartWashingMachine(Washing_machine):
#     def __init__(self, brand, power_rating, weight, color, company, capacity, type,Wifi_enabled,voice_controlled):
#         super().__init__(brand, power_rating, weight, color, company, capacity, type)
#         self.Wifi_enabled=Wifi_enabled
#         self.voice_controlled=voice_controlled
#     def display2(self):
#         super().display()
#         print(f"support for wifi : {self.Wifi_enabled}")
#         print(f"support for voice_controlled : {self.voice_controlled}")
# s1=SmartWashingMachine("LG","4","30kg","Black","LG","2","Washing","True","False")
# s1.display2()
    






        

# 5. 	Class Employee has emp_id, name, department, salary, contact.
# 	Class Manager adds team_size, project_name.
# 	Class Developer adds skills, experience_years.
# 	Use methods like show_details(), update_salary(amount), and print_role().

class Employee:
    def __init__(self, emp_id, name, department, salary, contact):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.contact = contact

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ₹{self.salary}")
        print(f"Contact: {self.contact}")

    def update_salary(self, amount):
        self.salary += amount
        print(f"Updated salary: ₹{self.salary}")

    def print_role(self):
        print("Role: Employee")

class Manager(Employee):
    def __init__(self, emp_id, name, department, salary, contact, team_size, project_name):
        super().__init__(emp_id, name, department, salary, contact)
        self.team_size = team_size
        self.project_name = project_name

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")
        print(f"Project Name: {self.project_name}")

    def print_role(self):
        print("Role: Manager")

class Developer(Employee):
    def __init__(self, emp_id, name, department, salary, contact, skills, experience_years):
        super().__init__(emp_id, name, department, salary, contact)
        self.skills = skills  # should be a list
        self.experience_years = experience_years

    def show_details(self):
        super().show_details()
        print(f"Skills: {', '.join(self.skills)}")
        print(f"Experience: {self.experience_years} years")

    def print_role(self):
        print("Role: Developer")

# Example usage:
print("--- Manager Example ---")
m1 = Manager(101, "Amit Sharma", "HR", 80000, "9876543210", 10, "Recruitment Automation")
m1.show_details()
m1.update_salary(5000)
m1.print_role()

print("\n--- Developer Example ---")
d1 = Developer(102, "Soham Pawar", "IT", 60000, "8765432109", ["Python", "Django", "React"], 3)
d1.show_details()
d1.update_salary(7000)
d1.print_role()


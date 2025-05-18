class car :
    def model(self,name,Model1):
        self.name=name
        self.Model1=Model1
    def display(self): 
         print("The name of car is {self.name} the model is {self.Model1}")
class price (car) :
    def part(self,color,price):
        self.color=color
        self.price=price
    def Display(self):
        print(f"the color is {self.color} and price is : {self.price}")

C1=price()

C1.model("xyz","abc")
C1.part("balck",202020)

C1.display()
C1.Display()

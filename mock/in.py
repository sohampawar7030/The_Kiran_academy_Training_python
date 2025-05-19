class parent :
    def display(self):
        print("This is parent class")

class mother :
    def display(self):
        print("this is mother class")
class child(parent,mother):
    def display2(self):
        super().display()
        print("This is child class ")



c1=child()
c1.display2()


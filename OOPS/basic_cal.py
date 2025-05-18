history=[]
class calculator :
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        c=self.a+self.b
        print("* * " * 39)
        print("the addition is :",c)
        history.append(f"Addtion : :{self.a}+{self.b} = {c}")

    def sub(self):
        substract=self.a-self.b
        print("* * " * 39)
        print("The substraction is : ",substract)
        history.append(f"Substraction :{self.a}-{self.b} = {substract}")
    def mul(self):
        multi=self.a*self.b
        print("* * " * 39)
        print("the answer is :",multi)
        history.append(f"Multiplication :{self.a}*{self.b} = {multi}")
    def div(self):
        if self.b == 0 :
            print("Error")
        else:
            div=self.a/self.b
            print("* * " * 39)
            print("the answer is:",div)
            history.append(f" Division : {self.a}/{self.b} = {div}")

while True :
    print("* * " * 39)
    print("""
    1. Calculator
    2. History
    3. clear
    4. exit""")
    print("* * " * 39)

    choices=int(input("Enter the choice :"))

    if choices >=4:
        print("thank you visit again !!!!")
        break

    if choices == 1 :
# INPUT FOROM USER 
        while True:
            print("* * " * 39)
            print("""Enter the choices : 
                  
                1. addition 
                2. Substraction
                3. multiplication 
                4. division
                5. Exit""")
            print("* * " * 39)
            choice=int(input("Enter the choice : "))
            print("* * " * 39)

            if choice >=5 :
                print("Exiting the calculator")
                print(history)
                break

            a=int(input("Enter the no :"))
            b=int(input("Enter the no :"))


            calc=calculator(a,b)

            if choice == 1 :
                calc.addition()
            elif choice == 2 :
                calc.sub()
            elif choice == 3 :
                calc.mul()
            elif choice == 4 :
                calc.div()
            elif choice == 5 :
                print("exit")
    elif choices == 2 :
        print("History ")
        print(history)
    elif choices == 3:
        print("* * " * 39)
        print("Are you conform to clear history !!!!")
        print(""""
              1.yes
              2.no""")
        
        print("* * " * 39)
        choice=int(input("Enter the choice :"))
        if choice == 1 :
            history.clear()
            print("clear history",history)
        else :
            print(history)
    else :
        break

        

          
        
            
            

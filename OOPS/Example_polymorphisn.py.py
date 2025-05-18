class student :
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(f"full name is : {self.fname} {self.lname}")

class collage(student) :
    
    def __init__(self,fname,lname,collage_name,year):
        super().__init__(fname,lname)
        self.collage_name=collage_name
        self.year=year
        super().display()       
    def display(self):
        print(f"the student is {self.fname} : {self.lname}  The collage is : {self.collage_name} year :{self.year}")

cls=collage("soham","pawar","acem","BE")
cls.display()


        



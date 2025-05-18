class paitent :
    cla="the kiran acadamy"
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def p1(self):
        print(f"the name is : {self.fname} {self.lname}")

class address(paitent) :
    
    def __init__(self,fname,lname,city,pincode):
        self.city=city
        self.pincode=pincode
        print(super().cla)
        paitent.__init__(self,fname,lname)

    
    def p2(self):
        print(f"the name is {self.fname} {self.lname} address is : {self.city} {self.pincode}")

        
clss =address("soham","pawar","pune",41306)
clss.p2()
# cls=paitent("soham","pawar")
# cls.p1()



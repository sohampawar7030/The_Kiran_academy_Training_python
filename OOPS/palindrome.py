# code on palindrome 

str=input("enter the word : ")
class abc :
    def __init__(self,str):
        self.str=str
        str=self.str
    def pal(self):
        if self.str == str[::-1]:
            print(f"{str} this is palindrome ")
        else:
            print("this is not palindrome")
cal=abc(str)
cal.pal()

        
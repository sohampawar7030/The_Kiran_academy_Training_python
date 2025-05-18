year = int(input("Enter the year"))
class leap_year :
    def __init__(self,year):
        self.year=year
    def Year(self):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("this is leap year")
        else:
            print("this is not leap year ")

call=leap_year(year)
call.Year()
        
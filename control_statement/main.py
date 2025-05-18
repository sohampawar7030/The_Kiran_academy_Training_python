#control Statement 

# 1. if statement
# 2. if else statement
# 3. if elif else statement

# 1. if statement
# WAP check the word are palindrome or not.
# word=input("Enter the word: ")
# if(word==word[::-1]):
#     print("This is Plindrome")
# else:
#     print("This is not a palindrome")

# Write a Python program that checks whether a given number is positive or negative or Zero.

# no = int(input("Enter The No :"))

# if (no > 0 ):
#     print("This is Positive no ")
# else:
#     print("This Is Negitive No:")

# Write a Python program that checks whether a given number is even or odd.

# no = int(input("Enter the First no:"))
# if (no % 2 ==0 ):
#     print("This is Even No")
# else:
#     print("This is odd")



# Write a Python program that takes a student’s score as input and outputs their grade based on the following scale:
#                Score 90 or above: "A"
#                Score 80-89: "B"
#                Score 70-79: "C"
#                Score 60-69: "D"
#                Below 60: "F"

# score = int(input("Enter the marks :"))
# if(score > 90):
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>60:
#     print("D")
# else:
#     print("F")

# Write a Python program that checks if a year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it's also divisible by 400.
# year = int(input("Enter the Year : "))
# if year % 4 == 0 and year % 100 !=0 or (year % 400 ==0) :
#     print("This is leap Year")
# else:
#     print("this is not leap year")

# Write a Python program that checks the temperature and outputs the appropriate suggestion:
#                 If the temperature is below 0°C, print "It's freezing !"
#                 If the temperature is between 0°C and 15°C, print "It's cold !"
#                 If the temperature is between 16°C and 25°C, print "It's a nice day !"
# #                 If the temperature is above 25°C, print "It's hot !"

# temp = int(input("Enter the Temp :"))
# if temp < 0 :
#     print("This Is freezing ")
# elif temp > 0 and temp < 15 :
#     print("It is cold ")
# elif temp >16 and temp < 25 :
#     print("It's a nice day")
# else  :
#     print("its hot")





# Write a Python program that takes Four numbers as input  and outputs the largest of the Four.

num1=int(input("enter the no :"))
num2=int(input("enter the no :"))
num3=int(input("enter the no :"))
num4=int(input("enter the no :"))

if num1 > num2 and num1 > num3 and num1>num4:
    print("num1 is grater")
elif num2 > num1 and num2 > num3 and num2>num4:
    print("num2 is grater ")
elif num3 >num1 and num3 >num2 and num2>num4:
    print("num3 is grater")
else:
    print("num4 is grater")

# Write a Python program that takes the three sides of a triangle as input and checks if it is an equilateral, isosceles, or scalene triangle.
#               Equilateral: All three sides are equal.
#               Isosceles: Two sides are equal.
#               Scalene: All three sides are different.

# Write a Python program that checks if a person is eligible for a loan based on their age and salary:
#            The person must be at least 18 years old.
#            The salary must be at least 3000.

# Write a Python program that checks whether a given letter is uppercase or lowercase.

# Write a Python program that checks if a given word is a palindrome (the word is the same forward and backward).

# Write a Python program that checks if a given character is a vowel or consonant.

# Write aPython program that calculates tax based on the salary:
#             If the salary is above 100,000, tax is 20%.
#             If the salary is between 50,000 and 100,000, tax is 10%.
#             If the salary is below 50,000, no tax.

# Write a Python program that sorts a list and checks if the list was already sorted.

# Write a Python program that Takes a list of numbers as input. Checks if there are any duplicate numbers in the list. If duplicates exist, remove them. Sorts the list and prints the sorted list.







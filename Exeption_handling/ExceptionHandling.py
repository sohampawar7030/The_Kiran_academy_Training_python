def DivideNo():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        
        if num2 == 0:
            raise ZeroDivisionError("Denominator must not be 0")
        
        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter only numbers.")
    
    except ZeroDivisionError as e:
        print("Error!", e)
    
    else:
        print("Result:", result)
    
    finally:
        print("Operation is completed.")

DivideNo()

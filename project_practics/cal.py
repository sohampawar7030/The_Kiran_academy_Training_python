history=[]
# wap calculator
while True:
    print(""" Choose Your Option :
        1. Calculator 
        2. History
         """)
    print("*"*159)
    option=int(input("Choose your Options :"))

    if option>=5:
        print("Invalid No ")
    else:
        pass
    # result=None
    
    if option == 1 :
        while True:
            print("""Enter the Choice :
                1. addition 
                2. Substraction 
                3. Division
                4. Multilpication
                5. Exit""")
            print("*"*159)
            choice=int(input("Enter the Choices :"))
            if choice==5:
                break



            def calculator():
                    if choice >=6:
                        print("Invalid choices")
                        return
                    
                    num1=int(input("Enter the first no :"))
                    num2=int(input("Enter the Second  no :"))
                    
                    result=""
                    operation=""

                    if choice ==1:
                        result=num1+num2
                        operation=f"Addition  : {num1}+{num2}={result}"
                        print("Addition is : ",result)
                        print("*"*159)
                       
                        
                    elif choice == 2:
                        result=num1-num2
                        operation=f"Substraction  :{num1}-{num2}={result}"
                        print("substraction is : ",result)
                        print("*"*159)
                        
                    elif choice == 3:
                        result=num1/num2
                        operation=f"Division  : {num1}/{num2}={result}"
                        print("Division is : ",result)
                        print("*"*159)
                        
                    elif choice == 4:
                        result=num1*num2
                        operation=f"Multiplication :{num1}*{num2}={result}"
                        print("Multiplication is : ",result)
                        print("*"*159)
                        
                    
                    else:
                        return
                        
                    
                
                        

                    history.append(operation) 
            
                
                
            calculator()
        
    elif option == 2:
        print("Calculator History")
        if not history :

            print("history is not avaliable")
            
        else:
            for entry in history:
                
                print(entry)
            
        break






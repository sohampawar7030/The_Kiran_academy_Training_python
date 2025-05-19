l1=[]

start_no = 3 
end_no = int(input("Enter the last no : "))


for num in range(2,end_no):
    for i in range(2,int(num * 0.5 )+1):
        if num % i == 0 :  
         break
        
    else :
        # print(num,end=' ')
        l1.append(num)
print(l1)


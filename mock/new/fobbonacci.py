# #fobbanacci series :
# no = 10
# a,b = 0,1
# l1=[]

# for _ in range(no):
#     l1.append(str(a))
#     a,b=b ,a+b 
# print("+".join(l1))






l1=[]
try:
    no=int(input("Enter the no :"))
    a,b=0,1
    for _ in range(no):
        l1.append(str(a))
        a,b=b , a+b
    print(" + ".join(l1))
except ValueError:
    print("invalid !!! please Enter the no only ")

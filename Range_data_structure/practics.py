# # 1.	WAP to create a list of integer value and print it on the screen using for loop
# l1=[1,2,3,4,5,6,7,8,9,0]
# for i in l1:
#     print(i)

# 2.	WAP to create a list of float value and print it on the screen using for loop
# l1=[1.1,1.2,1.3,1.4]
# for i in l1:
#     print(i)
# # 3.	WAP to create a dict of key and  value pair and print it on the screen using for loop
# dict1={"name":"soham","year":"be","branch":"aiml"}
# for i in dict1.keys():
    # print(i ,end=" ")
# 4.	WAP to create a dict of key and  value pair and print only the keys on the screen using for loop
dict1={"name":"soham","year":"be","branch":"aiml"}
for i in dict1.keys():
    print(i)
    
# 5.	WAP to print all the even numbers between 1 to 20
# for i in range(0,21,2):
#     print(i,end=" ")
# 6.	WAP to print all the odd numbers between 1 to 20
for i in range(1,20):
    if(i%2!=0):
       print(i,end=" ")

# 7.	WAP to print the multiple of 7 between 1 to 100
for i in range(7,100,7):
    print(i,end="")
# 8.	WAP to print 100 t0 50 in reverse
for i in range(100,50,-1):
    print(i)
# 9.	Wap to print even numbers from 20 to 10 in reverse
for i in range(20,10,-1):
    if(i%2==0):
        print(i)
# 10.	WAP to create a list of numbers from 1 to 10.

li=[]
for i in range(10):
   
    li.append(i)
print(li)

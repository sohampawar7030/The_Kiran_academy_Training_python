no = int(input("Enter the No :"))

if no < 1 :
    print("this is not prime no ")
elif no == 2 :
    print("this is a prime no ")
else :
    for i in range(2,int(no * 0.5)+1):
        if no % i ==0 :
            print("this is not prime no ")
            break
    else :
        print("this is prime no ")
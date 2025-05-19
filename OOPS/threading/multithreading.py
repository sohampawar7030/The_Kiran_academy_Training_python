'''
#threading :
    

#multithreading 
        it is machanism of 

'''
import time
import threading
from threading import Thread


def square(*l1):
    print("The Thread is Started !!!!")
    time.sleep(3)
    for i in l1 :
        sq=i**2
        print(sq)
l1=[1,2,3,4,5]

s1=threading.Thread(target=square,args=(l1))
s1.start()
s1.join()
print("thread is stopped !!!!")






    
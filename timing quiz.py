import time
def down(t):
    while t>0:
        print(t)
        t-=1
        time.sleep(1)
    print("time up")    
seconds=int(input("enter the number"))

down(seconds)
